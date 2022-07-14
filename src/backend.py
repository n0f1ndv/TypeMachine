import curses
from timeit import default_timer
from random import randrange

def get_input(window, text):
    TEXT_CENTERED = int((curses.COLS - len(text)) / 2)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    GOOD = curses.color_pair(1)
    WRONG = curses.color_pair(2)

    words_in_text = len(text.split())
    mistakes = 0
    start_timer = True
    start = None

    window.move(2, TEXT_CENTERED)
    i = 0
    while i < len(text):
        try:
            key = window.getkey()
        except:
            key = None

        if key == text[i]:
            if start_timer:
                start = default_timer()
                start_timer = False

            window.addstr(2, TEXT_CENTERED + i, text[i], GOOD)
            window.move(2, TEXT_CENTERED + i + 1)
            i += 1
        elif key == 'KEY_BACKSPACE' and i != 0:
            i -= 1
            window.addstr(2, TEXT_CENTERED + i, text[i])
            window.move(2, TEXT_CENTERED + i)
        else:
            if start_timer:
                start = default_timer()
                start_timer = False

            window.addstr(2, TEXT_CENTERED + i, text[i], WRONG)
            window.move(2, TEXT_CENTERED + i + 1)
            i += 1
            mistakes += 1

    duration = default_timer() - start

    return mistakes, duration, words_in_text

def calculate_results(window, mist, dur, wit, txtlen):
    accuracy = round(((txtlen - mist) / txtlen) * 100, 1)
    acc_info = f"Accuracy: {str(accuracy)}"
    window.addstr(4, int((curses.COLS - len(acc_info)) / 2), acc_info)

    wpm = round(wit / dur * 60)
    wpm_info = f"WPM: {str(wpm)}"
    window.addstr(5, int((curses.COLS - len(str(wpm_info))) / 2), wpm_info)

def create_text(punc_mark, text_len):
    text = str()
    common_words = list()

    if punc_mark != ' ':
        punc_mark += ' '

    with open('res/common_words.txt', 'r') as file:
        common_words = file.read()[:-1]
        i = 0
        while i < text_len:
            text += common_words.split('\n')[randrange(0, 1000)]
            text += f'{punc_mark}'

            i += 1
            if i % 10 == 0 and text_len != 10:
                text += '\n'

    return text[:-(len(punc_mark))]

def command(window):
    state = window.getkey()
    new_text, loop = bool(), bool()

    if state == 'r':
        new_text = False
        loop = True
    elif state == 'n':
        new_text = True
        loop = True
    elif state == 'q':
        loop = False
    else:
        loop = False
        
    return loop, new_text, 0, 0, 0
