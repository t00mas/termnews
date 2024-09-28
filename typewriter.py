import curses
import random
import textwrap
import time


def fuzzy_delay(delay):
    return delay + random.uniform(-delay / 2, delay / 2)


def typewriter_effect(window, text, delay=0.03, indent=0):
    window.addstr('\n')
    window.refresh()

    glitch_chars = ['@', '#', '$', '%', '&', '*', '+', '-', '=', '?', '!', '^', '~', '|', '/', '\\', '<', '>']
    lines = text.split('\n')
    for line in lines:
        wrapped_lines = textwrap.wrap(line, curses.COLS - 1 - indent)
        for wrapped_line in wrapped_lines:
            if window.getyx()[0] >= curses.LINES - 1:
                window.scroll(1)
                window.move(curses.LINES - 2, 0)
            window.addstr(' ' * indent)
            for char in wrapped_line:
                if random.random() < 0.01:  # 1% chance to insert 1-5 glitch character(s)
                    for _ in range(random.randint(1, 5)):
                        glitch_char = random.choice(glitch_chars)
                        color_pair = random.choice([1, 2, 3])
                        window.addstr(glitch_char, curses.color_pair(color_pair))
                else:
                    # Show green block
                    window.addstr('█', curses.color_pair(1))
                    window.refresh()
                    time.sleep(fuzzy_delay(delay))
                    # Replace with the actual character
                    y, x = window.getyx()
                    try:
                        window.move(y, x - 1)
                    except curses.error:
                        pass
                    window.addstr(char, curses.color_pair(1))
                window.refresh()
                time.sleep(fuzzy_delay(delay))
            window.addstr('\n')
            window.refresh()
