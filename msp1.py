from tkinter import *
import pygame
import os
from tkinter import messagebox as tsmg
from tkinter.filedialog import askopenfilename
pygame.init()
pygame.mixer.init()
root=Tk()
root.title("music player by avi")
root.geometry("300x150")
root.wm_iconbitmap("icon.ico")

play=PhotoImage(file="pla.png")
stop=PhotoImage(file="stop.png")
pause=PhotoImage(file="pause.png")
rewind=PhotoImage(file="rewind.png")
speaker=PhotoImage(file="speaker.png")
mute=PhotoImage(file="mute.png")

def add():
    global file
    file=askopenfilename()

    player()

def exits():
    a=tsmg.askquestion("QUIT","are you sure you want to quit")
    if a=="yes":
        root.destroy()

def remove():

    pass

def helps():

    tsmg.showinfo("ABOUT US","This music player is created by avi")

def player():

    global paused
    if paused:

        sbar['text'] = "resumed"
        pygame.mixer_music.unpause()
        paused=False
    else:
        paused=True
        try:
            sbar['text']="playing music:  "+os.path.basename(file)
            text = Label(root, text=file).pack()

            pygame.mixer_music.load(file)
            pygame.mixer_music.play()

        except:

            tsmg.showerror("ERROR 404","please first add the music and then try again")

def stopper():
    sbar['text']="stopped"

    pygame.mixer_music.stop()

paused=False
def pauser():
    global paused
    paused=True
    sbar['text']="paused"
    pygame.mixer_music.pause()

def shower():
    a = pygame.mixer.Sound(file)
    length = a.get_length()
    print(length)
def vol(val):
    volume=int(val)/100
    pygame.mixer_music.set_volume(volume)
def rewinder():
    player()
    sbar['text']="music replayed"

muted=False
def muter():
    global muted
    if muted:
        pygame.mixer_music.set_volume(0.5)
        b4.configure(image=speaker)
        s.set(50)
        muted=False

    else:
        pygame.mixer_music.set_volume(0)
        val = 0
        s.set(val)
        b4.configure(image=mute)
        muted=True
if __name__ == '__main__':

    f=Frame(root)
    f.pack()
    sbar = Label(root, text="welcome", relief=SUNKEN,bg="yellow")
    sbar.pack(side=BOTTOM, fill=X)
    b = Button(f, image=rewind, bg="yellow", command=rewinder).pack(side=LEFT)
    b1 = Button(f, image=pause, bg="yellow", command=pauser,padx=10).pack(side=LEFT)
    b2=Button(f,image=play,bg="black",command=player,padx=10).pack(side=LEFT)
    b3=Button(f,image=stop,bg="yellow",command=stopper,padx=10).pack(side=LEFT)
    b4=Button(f,image=speaker,bg="yellow",command=muter,padx=10)
    b4.pack(side=BOTTOM,anchor="sw")

    s=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=vol)
    val=50
    s.set(val)
    s.pack()


    mainmenu=Menu(root)
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="add",command=add)
    m1.add_command(label="remove",command=remove)
    m1.add_command(label="exit",command=exits)

    mainmenu.add_cascade(label="music",menu=m1)

    m2 = Menu(mainmenu, tearoff=0)
    m2.add_command(label="about", command=helps)
    mainmenu.add_cascade(label="Help", menu=m2)

    root.config(menu=mainmenu)

    root.mainloop()