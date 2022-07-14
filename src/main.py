import backend
import curses

def main(stdscr):
    new_text = True
    loop = True
    while loop:
        stdscr.clear()
        stdscr.addstr(0, 0, 'Press q to quit, anything else to start.')
        if stdscr.getkey() == 'q':
            break

        if new_text:
            punc_mark, text_len = backend.set_options(stdscr)
            text = backend.create_text(punc_mark, text_len)

        stdscr.clear()

        stdscr.addstr(0, int((curses.COLS - 12) / 2) , "/TypeMachine")
        stdscr.addstr(2, int((curses.COLS - len(text)) / 2), text)

        mistakes, duration, words_in_text = backend.get_input(stdscr, text)
        backend.calculate_results(stdscr, mistakes, duration, words_in_text, len(text))

        loop, new_text, mistakes, duration, words_in_text = backend.command(stdscr)

        stdscr.refresh()
        
curses.wrapper(main)
