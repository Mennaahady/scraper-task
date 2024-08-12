from flask import Flask, json, request, jsonify
import requests
from parsel import Selector
import re



app = Flask("task")

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.json
        url = data.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        proxies = {
            'http': "http://10.10.10.10:8000",
            'https': "http://10.10.10.10:8000",
        }


        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        html_content = response.text
        selector = Selector(text=html_content)
        products = []
        for product in selector.xpath('//div[@class="product-item__content"]'):
            product_info = {
                'pid': product.xpath('.//a[@class="ui-btn  ui-btn--buy js_floating_basket_btn js_btn_buy js_preventable_buy_action"]/@data-product-id').get(),
                'title': product.xpath('.//a[@class="product-title px_list_page_product_click list_page_product_tracking_target"]/text()').get(),
                'brand': product.xpath('.//a[@data-test="party-link"]/text()').get(),
                'rating': product.xpath('.//div[@class="u-mb--xs"]/@aria-label').re_first(r'Gemiddeld\s([\d\.]+)'),
                'n_reviews': product.xpath('.//div[@class="u-mb--xs"]/@aria-label').re_first(r'uit\s(\d+)\sreviews'),
                'url': product.xpath('.//a[@class="hit-area__link medium--is-hidden list_page_product_tracking_target"]/@href').get(),
                'price': product.xpath('.//meta[@itemprop="price"]/@content').get(),
                'currency':re.search(r'\d+\s+(\w+)',(str(product.xpath('.//div[@class="price-block__price"]//span[@data-test="price-info-srt-text"]/text()').get()))).group(1),
                'category_name': product.xpath('//div[@class="results-area"]/@data-group-name').get(),
            }
            products.append(product_info)

        return jsonify(products)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if "task" == '__main__':
    app.run(debug=True)
