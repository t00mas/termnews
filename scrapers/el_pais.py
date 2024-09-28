from config import EL_PAIS_ES_URL
from scrapers.utils import fetch_soup

def scraper():
    soup = fetch_soup(EL_PAIS_ES_URL)
    headlines = soup.find_all('h2')
    headlines_and_contents = [
        (f"El Pais: {headline.text}", "")
        for headline in headlines
    ]
    return headlines_and_contents
