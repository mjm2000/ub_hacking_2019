import curses
from curses import wrapper

stdscr = curses.initscr

##Global variables

#set up the window
begin_x = 20; begin_y = 7
height = 5; width = 40
window = curses.newwin(height, width, begin_y, begin_x)

#pad to set up the albums
alb_width = 40
alb_height = 2
albums = curses.newpad(alb_height, alb_width)
albums.refresh(0,0,0,0,2,40)

#pad to set up the songs
song_width = 40
song_height = 3
songs = curses.newpad(song_height, song_width)
songs.refresh(0,0,3,0,5,40)

#lists to store the albums and songs
abl_list = []
song_list = []

#now to run functionality
while True:
