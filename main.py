import tkinter as tk
import fnmatch 
import os
from pygame import mixer
from pygame.music import play
canvas = tk.Tk();
canvas.title("Music Player")
canvas.geometry("600x600")
canvas.config( bg = 'black')

rootpath = "F:\\python project\Music_Player"
pattern = "*.mp3"

prev_img = tk.PhotoImage(file ="prev_img.png")
stop_img = tk.PhotoImage(file ="stop_img.png")
play_img = tk.PhotoImage(file ="play_img.png")
pause_img = tk.PhotoImage(file ="pause_img.png")
next_img = tk.PhotoImage(file ="next_img.png")


def select():
    label.config(text =listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def pause_song():
    if pauseButton['text'] == "pause":
        mixer.music.pause()
        pauseButton['text'] = "play"
        else:
            mixer.music.unpause()
            pauseButton["text"] ="pause"




listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100 , font =('poppins',17))
listBox.pack(padx =15 , pady =15) 

label = tk.Label(canvas, text = '' , bg = 'black' , fg ='yellow' ,font = ('poppins', 18 ))
label.pack(pady =15 )

top = tk.Frame(canvas,bg ="black")
top.pack(padx = 10 ,pady =5 , anchor ='center')

prevButton = tk.Button ( canvas ,text="prev" ,image = prev_img , bg= 'black', borderwidth=0 )
prevButton.pack( pady= 15, in_ = top ,side ='left') 

stopButton = tk.Button(canvas,text="stop")
stopButton.pack ( pady= 15, in_ = top ,side ='left', image = stop_img , bg= 'black', borderwidth=0 ,command = stop) 

playButton = tk.Button(canvas,text="play")
playButton.pack(pady= 15, in_ = top ,side ='left', image = play_img , bg= 'black', borderwidth=0 ,command = select ) 

nextButton = tk.Button(canvas,text="next")
nextButton.pack(pady= 15, in_ = top ,side ='left' ,image = next_img , bg= 'black' ,borderwidth=0 ) 

pauseButton = tk.Button(canvas,text="pause")
pauseButton.pack(pady= 15, in_ = top ,side ='left' ,image = pause_img , bg= 'black' ,borderwidth=0 command = pause_song ) 

for root ,dirs ,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)

# listBox.insert(0,"Vinesh List")

canvas.mainloop()
