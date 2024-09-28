from bs4 import BeautifulSoup
import requests


def fetch_json(url):
    response = requests.get(url)
    return response.json()


def fetch_soup(url):
    headers = {}
    cookies = {}
    session = requests.Session()
    response = session.get(url, headers=headers, cookies=cookies)
    response.raise_for_status()
    return BeautifulSoup(response.content, 'html.parser')