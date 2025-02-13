import requests
from bs4 import BeautifulSoup
import json
import os

# Base URL of the website to scrape
base_url = 'http://books.toscrape.com/catalogue/'

# Function to scrape a single page
def scrape_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    books = []

    # Find all book items on the page
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a['title']
        price = article.find('p', class_='price_color').text
        rating = article.find('p', class_='star-rating')['class'][1]
        image_url = base_url + article.find('img')['src'].replace('../', '')

        books.append({
            'title': title,
            'price': price,
            'rating': rating,
            'image_url': image_url
        })

    return books

# Function to scrape multiple pages
def scrape_books(start_page, num_pages):
    books = []
    for i in range(start_page, start_page + num_pages):
        url = f'{base_url}page-{i}.html'
        print(f'Scraping page {i}: {url}')
        books.extend(scrape_page(url))
    return books

# Main function to run the scraper
def main():
    start_page = 1
    num_pages = 5  # Number of pages to scrape
    books = scrape_books(start_page, num_pages)

    # Ensure the data directory exists
    output_dir = '../data'
    os.makedirs(output_dir, exist_ok=True)

    # Save the data to a JSON file
    output_file = os.path.join(output_dir, 'books.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

    print(f'Scraping complete. Data saved to {output_file}')

if __name__ == '__main__':
    main()