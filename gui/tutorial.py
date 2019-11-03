import curses
from curses.textpad import Textbox, rectangle


def main(stdscr):
    h, w = stdscr.getmaxyx()
    searching = False
    search = "Type name here: "
    maxlen = w - len(search)
    search_len = 0

    #set up info for albums
    alb_index = 0
    alb_height = 40
    alb = curses.newpad(alb_height, w)

    #set up info for songs
    song_index = 0
    song_height = 20
    songs = curses.newpad(song_height, w)

    while True:
        key = stdscr.getch()
        stdscr.clear
        alb.clear
        alb.addstr(0,0,"hello")
        alb.refresh
        stdscr.refresh


curses.wrapper(main)