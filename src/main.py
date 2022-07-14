import backend
import curses
import sys

# TODO:
# * Login for text which contains more than one line

def main(stdscr):
    new_text = True
    loop = True
    while loop:
        if new_text:
            text = backend.create_text(' ', 10)
            stdscr.addstr(0, 0, text)
            stdscr.getch()

        stdscr.clear()

        stdscr.addstr(0, int((curses.COLS - 12) / 2) , "/TypeMachine")
        stdscr.addstr(2, int((curses.COLS - len(text)) / 2), text)

        mistakes, duration, words_in_text = backend.get_input(stdscr, text)
        backend.calculate_results(stdscr, mistakes, duration, words_in_text, len(text))

        loop, new_text, mistakes, duration, words_in_text = backend.command(stdscr)

        stdscr.refresh()
        
curses.wrapper(main)
