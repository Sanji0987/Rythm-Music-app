from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import themed_tk as tk
from pygame import mixer
import threading
import os
from mutagen.mp3 import MP3
import time


# about us message in dropdown
def about_us():
    tkinter.messagebox.showinfo("Info", "This is a music player built using Tkinter and Pygame")


# contains full path to file like playlist
playlist = []


# adds file to playlist list and the list with path of song
def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1
    playlistbox.pack()


# opens explorer to choose file
def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)


# removes song from playlistbox and playlist list
def del_file():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)


# setting my window for use , and adding tk.themedtk() for integrating theme
root = tk.ThemedTk()
root.get_themes()
root.set_theme('arc')

# bottom status bar
statusbar = ttk.Label(root, text="Please Select The Music!", relief=SUNKEN, anchor=W)
# relief state of button , anchor is fixing in what direction , example west for w
statusbar.pack(side=BOTTOM, fill=X)  # fills for x-axis , side is for up or top

# creating 2 partitions using left and right frame
leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=20)

# playlist box in left frame
playlistbox = Listbox(leftframe)
playlistbox.pack(pady=10)

# removiung and adding songs in left frame list box
button_add = ttk.Button(leftframe, text='add', command=browse_file)
button_remove = ttk.Button(leftframe, text='remove', command=del_file)
button_add.pack(side=LEFT)
button_remove.pack(side=LEFT)

# right side frame (buttons etc)
rightframe = Frame(root)
rightframe.pack(side=RIGHT)

# right frame top frame ( music details)
topframe = Frame(rightframe)
topframe.pack()

# menu bar
menubar = Menu(root)
root.config(menu=menubar)

# submenu top bar (about me etc)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Open', command=browse_file)
submenu.add_command(label='Exit', command=root.destroy)
submenu.add_command(label='About Us', command=about_us)

mixer.init()  # starting pygame mixer

# designing the window
root.title("Rythm")
root.iconbitmap(r'music.ico')

filetext = ttk.Label(topframe, text="")
filetext.pack()

lengthlabel = ttk.Label(topframe, text="Total Length - --:--")
lengthlabel.pack(pady=10)

currenttime = ttk.Label(topframe, text="Current Length - --:--", relief=GROOVE)
currenttime.pack()


# changes details above the music buttons for telling user
def show_details(play_itt):
    filetext['text'] = "Playing" + '-' + os.path.basename(play_itt)
    file_data = os.path.splitext(play_itt)
    if file_data[1] == '.mp3':
        audio = MP3(play_itt)
        totallength = audio.info.length
    else:
        a = mixer.Sound(play_itt)
        totallength = a.get_length()

    mins, secs = divmod(totallength, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)  # formatting time for display
    lengthlabel['text'] = "Total Length" + '-' + timeformat
    t1 = threading.Thread(target=start_count, args=(totallength,))
    t1.start()


def start_count(t):
    global paused
    # t will become false when it reaches 0 and break, mixer.get_busy checks whether music player is playing or
    # stopped and sends boolean
    while t or mixer.music.get_busy():
        if paused:
            continue
        elif paused == FALSE:
            try:
                mins, secs = divmod(t, 60)
                mins = round(mins)
                secs = round(secs)
                timeformating = '{:02d}:{:02d}'.format(mins, secs)
                currenttime['text'] = "Current Time" + '-' + timeformating
                time.sleep(1)
                t -= 1
            except:
                quit()


paused = FALSE


# function for playing music
def playmusic():
    global paused
    # checks for paused or not
    if paused == FALSE:
        # if user didnt select music file , sends special error
        try:
            global play_it  # declaring so that i can use for elif statement aswell
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = 'Playing music' + '->' + os.path.basename(play_it)
            show_details(play_it)

        except:
            tkinter.messagebox.showerror("Music Play Error", "Please Select The Music File From Dropdown")
    elif paused == TRUE:
        mixer.music.unpause()
        paused = FALSE
        show_details(play_it)


# stops music not pause
def stopmusic():
    mixer.music.stop()
    statusbar['text'] = 'Music stopped'


# changes mixer module volume from slider , val is a value sent automatically by slider
def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)


# pauses music
def pausemusic():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = 'Music paused'


# restarts music
def rewindmusic():
    playmusic()
    statusbar['text'] = 'Rewinded Music'


muted = FALSE


# muting the audio
def mute():
    global muted
    if muted:
        mixer.music.set_volume(0.5)
        volumebtn.configure(image=unmute_photo)
        scale.set(50)
    else:
        mixer.music.set_volume(0)
        volumebtn.configure(image=mute_photo)
        scale.set(0)
        muted = TRUE


# frames for placment of widgets
middle_frame = Frame(rightframe)
middle_frame.pack(padx=10, pady=10)

bottom_frame = Frame(rightframe)
bottom_frame.pack(padx=20, pady=30)

# buttons
player_photo = PhotoImage(file='musical-note.png')
playbtn = ttk.Button(middle_frame, image=player_photo, command=playmusic)
playbtn.grid(row=0, column=0, padx=10)

# stop button
stop_photo = PhotoImage(file='stop.png')
stopbtn = ttk.Button(middle_frame, image=stop_photo, command=stopmusic)
stopbtn.grid(row=0, column=1, padx=10)

# pause button
pause_photo = PhotoImage(file='pause.png')
pausebtn = ttk.Button(middle_frame, image=pause_photo, command=pausemusic)
pausebtn.grid(row=0, column=2, padx=10)

# rewind button
rewind_photo = PhotoImage(file='rewind.png')
rewindbtn = ttk.Button(bottom_frame, image=rewind_photo, command=rewindmusic)
rewindbtn.grid(row=0, column=0)

# mute button
mute_photo = PhotoImage(file='mute.png')
unmute_photo = PhotoImage(file='unmute.png')
volumebtn = ttk.Button(bottom_frame, image=unmute_photo, command=mute)
volumebtn.grid(row=0, column=2)

# audio slider
scale = ttk.Scale(bottom_frame, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(50)
mixer.music.set_volume(0.5)
scale.grid(row=0, column=1)

root.mainloop()  # keeps kinter frames in loop , like a video
