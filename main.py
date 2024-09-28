import curses
import random
import time

from config import FETCH_INTERVAL
from typewriter import typewriter_effect
from scrapers import el_mundo, el_pais, news_api


def fetch_headlines_and_contents(stdscr):
    scrapers = [el_mundo, el_pais, news_api]
    headlines_and_contents = []
    for scraper in scrapers:
        headlines_and_contents += scraper.scraper()
    random.shuffle(headlines_and_contents)
    last_fetch_time = time.time()

    typewriter_effect(stdscr, f"\n\n\n{len(headlines_and_contents)} news articles fetched\n\n\n", indent=0)
    return headlines_and_contents, last_fetch_time


def main(stdscr):
    curses.curs_set(0)    # Hide cursor
    stdscr.nodelay(1)     # Don't block on getch()
    stdscr.scrollok(True) # Enable scrolling
    
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    headlines_and_contents, last_fetch_time = fetch_headlines_and_contents(stdscr)
    while True:
        if len(headlines_and_contents) > 0:
            headline, content = headlines_and_contents.pop(0)
            headline_indent = random.randint(0, 10)
            content_indent = headline_indent + random.randint(0, 10)
            typewriter_effect(stdscr, "\n\n" + headline, indent=headline_indent)
            typewriter_effect(stdscr, "\n" + content + "\n\n", indent=content_indent)
            stdscr.refresh()

        if time.time() - last_fetch_time >= FETCH_INTERVAL:
            headlines_and_contents, last_fetch_time = fetch_headlines_and_contents(stdscr)

        time.sleep(0.1)


if __name__ == "__main__":
    curses.wrapper(main)