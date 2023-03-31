import curses
from curses import wrapper
import random
import time

def start_screen(stdscr):
    #stdscr.clear()
    stdscr.addstr("welcome to typing speed test")
    stdscr.addstr("\npress any key to continue")
    #stdscr.addstr(1,0, "press any key to continue")
    #stdscr.refresh()
    stdscr.getkey()

def load_text():
    with open("target_text.txt", "r") as f:
        lines=f.readlines()
    return random.choice(lines).strip()

def display_text(stdscr,target_text,user_text,wpm):
    stdscr.clear()
    stdscr.addstr("please start typing")
    stdscr.addstr(2,0,target_text, curses.color_pair(3))

    for i,char in enumerate(user_text):
        correct_char=target_text[i]
        if char==correct_char:
            color=curses.color_pair(1)
        else:
            color=curses.color_pair(2)
        stdscr.addstr(2,i,char,color)
    #adding strings f""abc={number}"
    stdscr.addstr(3,0,f"WPM={wpm}")
    #stdscr.refresh()


def typing_test(stdscr):
    target_text=load_text()
    #assigning the user_text as a list
    user_text=[]
    wpm=0
    start_time=time.time()
    #catch error at 54
    stdscr.nodelay(True)

    while True:
        time_elapsed=max(time.time()-start_time,1)
        wpm=round(((len(user_text)/time_elapsed)*60)/5)

        display_text(stdscr,target_text,user_text,wpm)

        if len(user_text)==len(target_text):
        #below command will work if the user types all correct characters
        #if "".join(user_text)==target_text:

        # when text is completed wpm calculation should stop. ie dont wait for the user to stop hitting the keys
            stdscr.nodelay(False)
            break

        try:
            key=stdscr.getkey()
        except:
            continue
        if ord(key)==27:
            break
        if key in ("KEY_BACKSPACE", "\b", "x7f"):
            #if len(user_text)>0:
            user_text.pop()
        elif len(user_text)<len(target_text):
            user_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    start_screen(stdscr)
    while True:
        typing_test(stdscr)

        stdscr.addstr(4,0,"you have completed the test. press any key to continue or 'Esc' to exit")
        key=stdscr.getkey()
        if ord(key)==27:
            break

wrapper(main)