# Category Products Scraper API

## Overview

This project is a simple Flask-based server that provides a REST API to scrape product information from a retailer's category page. Given a URL, the API will scrape details about products listed on that page, including product ID, title, brand, rating, number of reviews, URL, price, currency, and category name.

## Features

- **Scraper API**: A single endpoint that takes a category page URL and returns scraped product data in JSON format.
- **Jupyter Notebook**: A notebook is provided to call the API and save the scraped data to a CSV file.
- **Proxy Support**: Use a proxy server to make requests.
- **Conda Environment**: The project is set up to use a Conda environment.

## Technologies

- Python 3.12
- Flask
- Requests
- Parsel
- JSON
- Pandas

### Prerequisites

- Python 3.12 installed
- Conda installed for environment management

### Recreate the Conda Environment

To recreate the Conda environment used for this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Mennaahady/scraper-task.git
   ```

2. Create the Conda environment:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```bash
   conda activate scraper-env
   ```

4. Run the Flask server and Jupyter Notebook as described above.
    ```bash
    python -m flask --app server run
    ```
5. Send request
    You can either use postman sending a post request with the url as follows
    ```bash
    {
    "url": "https://www.bol.com/nl/nl/l/audio-hifi/10714/"
    }
    ```
    on the url 127.0.0.1:5000/scrape
    or you can use the jupyter file included within the repo and run all cells
