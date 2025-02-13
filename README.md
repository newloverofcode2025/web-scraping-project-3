# web-scraping-project-3
 # Web Scraping Project 3

## Overview
This project demonstrates a web scraping task using Python, requests, and BeautifulSoup. It scrapes book details from a website, including title, price, rating, and image URL, and saves them to a JSON file. The script also handles pagination to scrape multiple pages.

## Project Structure
web-scraping-project-3/
├── src/
│   └── main.py
├── data/
│   └── books.json
└── README.md

## Dependencies
- Python
- requests
- beautifulsoup4

## Setup
1. Clone the repository.
2. Install the required libraries using `pip install requests beautifulsoup4`.
3. Run the script using `python src/main.py`.

## Usage
- The script scrapes book details from the specified website and saves them to `data/books.json`.

## Notes
- Replace the base URL in `main.py` with the website you want to scrape.
- Ensure you have permission to scrape the website and comply with its `robots.txt` file.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Commit and Push Changes:
Open GitHub Desktop.
Make sure your repository is selected.
Click on "Changes" to see the files you've added.
Write a commit message (e.g., "Initial commit with book scraping project").
Click "Commit to main".
Click "Push origin" to push your changes to GitHub.