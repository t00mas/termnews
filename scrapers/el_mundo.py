from config import EL_MUNDO_ES_URL
from scrapers.utils import fetch_soup

def scraper():
    soup = fetch_soup(EL_MUNDO_ES_URL)
    articles = soup.find_all('article')
    headlines_and_contents = []
    for article in articles:
        header = article.find('header')
        headlines_and_contents.append((f"El Mundo: {header.text}", ""))
    return headlines_and_contents
