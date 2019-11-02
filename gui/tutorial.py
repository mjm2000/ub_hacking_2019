import curses
from curses.textpad import Textbox, rectangle



search = "Type name here: "

def print_search(stdscrs):
    char = stdscr.getch()
    string = search
    if char != -1:
        if (char >= ord('A') and char <= ord('Z')) or (char >= ord('a') and char <= ord('z')):
            string += chr(key)
    
    stdscr.clear()
    stdscr.addstr(0,0,search)
    stdscr.refresh()

    search = string


def main(stdscr):
    h, w = stdscr.getmaxyx()
    searching = False

    while True:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_ENTER or key in [10, 13]:
            if searching == False:
                searching = True
            else:
                searching = False

        elif key == curses.KEY_DOWN:
            break

        if searching == True:
            print_search(stdscr)

        stdscr.refresh


curses.wrapper(main)