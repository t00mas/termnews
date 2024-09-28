import requests

from config import NEWS_API_URL
from scrapers.utils import fetch_json


def scraper():
    try:
        news_data = fetch_json(NEWS_API_URL)
        articles = news_data.get('articles', [])
        headlines_and_contents = [
            (f"API: {article['title']}", article['content'] or "")
            for article in articles
        ]
        return headlines_and_contents
    except requests.RequestException as e:
        return [("Error fetching news", str(e))]