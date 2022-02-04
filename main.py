import curses
from curses import wrapper
import time


def main(stdscr):
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, GREEN_AND_BLACK)

    for i in range(50):
        pad.refresh(0, i, 5, 5, 10, 25)
        time.sleep(0.1)

    stdscr.getch()


wrapper(main)
