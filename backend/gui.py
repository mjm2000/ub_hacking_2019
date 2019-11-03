import curses
import search
import ytdl


def main(stdscr):
    h, w = stdscr.getmaxyx()


    #used to help what is labeled
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    searching = False
    albums = False

    alb_list = []
    alb_idx = 0

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
        if key == ord('/') or key in [10, 13]:
            if searching == False:
                searching = True

            elif searching and srch != "":
                alb_list = search.yt_search(srch).items
                searching = False
                albums = True
            elif albums:
                k, v = alb_list[alb_idx]
                ytdl.get_desc(v)

        elif (key == curses.KEY_UP or key == ord('k'))  and albums:
            if alb_idx > 0:
                alb_idx -= 1
    
        elif (key == curses.KEY_DOWN or key == ord('j')) and albums:
            if alb_idx < len(alb_list) - 1:
                alb_idx += 1
        elif key == curses.KEY_EXIT:
            break

        #search function
        if searching:
            if search_len < maxlen - 1:
                if (key >= ord('A') and key <= ord('Z')) or (key >= ord('a') and key <= ord('z')):
                    search += chr(key)
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
            stdscr.addstr(0,0,bar)
        
        #parse through albums
        elif albums:
            stdscr.clear()
            stdscr.addstr(srch)
            for i in range(0,w):
                stdscr.addch(1,i,'*',curses.color_pair(2))
                
            line = 2
            for a in range(0,len(alb_list)):
                k,v = alb_list(alb_idx)
                if a >= h-2:
                    break
                elif a == alb_idx:
                    stdscr.addstr(line,0,k, curses.color_pair(1))
                else:
                    stdscr.addstr(line,0,k)

                line += 1

        # elif appState == "albums"
        # elif appState == "songs"


        stdscr.refresh


curses.wrapper(main)