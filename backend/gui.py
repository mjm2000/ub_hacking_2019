import curses
import search
import ytdl
import os

def main(stdscr):
    h, w = stdscr.getmaxyx()


    #used to help what is labeled
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    searching = False
    albums = False

    alb_list = {}
    alb_idx = 0
    alb_idx_title = ""

    # song_list = ["general", "kenobi"]
    # song_idx = 0


    #used to help build the search bar
    header = "Type album name here: "
    srch = ""
    maxlen = w - len(header)
    search_len = 0


    while True:
        key = stdscr.getch()

        stdscr.clear()

        #track key navigation conmmands
        if searching == False and key == ord('/'):
            searching = True
            if albums:
                albums = False


        if (key == curses.KEY_ENTER or key in [10, 13]):
            if searching and srch != "":
                alb_list = search.yt_search(srch)
                searching = False 
                albums = True

            elif albums:
                if alb_idx_title != "":
                    v = alb_list[alb_idx_title]
                    ytdl.get_desc(v, alb_idx_title)
                    albums = False
                    searching = True

        if (key == curses.KEY_UP or key == ord('k'))  and albums:
            if alb_idx > 0:
                alb_idx -= 1
    
        if (key == curses.KEY_DOWN or key == ord('j')) and albums:
            if alb_idx < len(alb_list) - 1:
                alb_idx += 1
        if key == ord('q'):
            stdscr.clear()
            searching = False
           # stdscr.erase()
            stdscr.refresh()
        if (albums or searching) and key == ord('z'):
           albums = False
           searching = False
           srch = ""
           stdscr.refresh

        if key == curses.KEY_EXIT:
            break

        #search function
        if searching:
            stdscr.addstr("(press ENTER to search)\n", curses.A_BOLD)
            stdscr.addch('\n')

            if search_len < maxlen - 1:
                if (key >= ord('A') and key <= ord('Z')) or (key >= ord('a') and key <= ord('z')):
                    srch += chr(key)
                    search_len += 1

                elif key == ord(' '):
                    srch += ' '
                    search_len += 1
            #deletes characters
            if key == curses.KEY_BACKSPACE:
                if search_len > 0:
                    srch = srch[:-1]
                    search_len -= 1
            bar = header + srch
            stdscr.addstr(bar)

            curses.curs_set(1)
        
        #parse through albums
        elif albums:
            stdscr.clear()
            stdscr.addstr(srch + '\n')
            for i in range(0,w-1):
                stdscr.addch('*',curses.color_pair(2))
            stdscr.addch('\n')
                
            line = 2
            for a in alb_list:
                idx = line - 2
                if line >= h-2:
                    break
                elif idx == alb_idx:
                    stdscr.addstr(a + '\n', curses.color_pair(1))
                    alb_idx_title = a
                else:
                    stdscr.addstr(a+'\n')

                line += 1
            for i in range(0,w-1):
                stdscr.addch('*',curses.color_pair(3))
            stdscr.addch('\n')
            stdscr.addstr("Use UP and DOWN to navigate, ENTER to download, and z to return to downloads\n", curses.A_BOLD)
            curses.curs_set(0)
        else:
            stdscr.clear()

            for i in range(0,w-1):
                stdscr.addch('*')
            stdscr.addch('\n')
            stdscr.addch('\n')
            
            files_info = os.listdir('backend/data') 
            for title in files_info:
                stdscr.addstr(title + '\n') 
            curses.curs_set(0)

            for i in range(0,w-1):
                stdscr.addch('*')
            stdscr.addch('\n')
            stdscr.addch('\n')
            stdscr.addstr("press '/' to search", curses.A_BOLD)

        # elif appState == "albums"
        # elif appState == "songs"


        stdscr.refresh


curses.wrapper(main)
