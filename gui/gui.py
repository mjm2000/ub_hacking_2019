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

        stdscr.clear()

        if key == curses.KEY_ENTER or key in [10, 13]:
            if searching == False:
                searching = True
            else:
                searching = False
                search = "Type name here: "
                search_len = 0

        elif key == curses.KEY_EXIT:
            break

        #search function
        if searching == True:
            if search_len < maxlen - 1:
                if (key >= ord('A') and key <= ord('Z')) or (key >= ord('a') and key <= ord('z')):
                    search += chr(key)
                    search_len += 1
                elif key == ord(' '):
                    search += ' '
                    search_len += 1

            if key == curses.KEY_BACKSPACE:
                if search_len > 0:
                    search = search[:-1]
                    search_len -= 1
            
                
            
            stdscr.clear()
            stdscr.addstr(0,0,search)
            stdscr.refresh()

        stdscr.refresh


curses.wrapper(main)