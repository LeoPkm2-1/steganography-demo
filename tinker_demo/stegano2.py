from tkinter import *
from tkinter import messagebox
from argparse import FileType

from tkinter.filedialog import *
from PIL import ImageTk,Image

from stegano import lsb
from tkinter import font as tkFont
from stegano import exifHeader as aaa
import os
from subprocess import Popen

def encode():
    pass

#main program
main=Tk()
main.title('Enc & Dec Panel ')
main.geometry("1300x750")
# main.attributes("-fullscreen", True)
fontl = tkFont.Font(family='Algerian', size=30)

global image1
image1=ImageTk.PhotoImage(Image.open("i.jpg"))
label=Label(main,text="lalal",image=image1)
label.pack()

encbutton = Button(text='Encode',fg='white',bg='black',width=20,command=encode)
encbutton['font'] =fontl 
encbutton.place(relx=0.6,rely=0.3)

decbutton=Button(text='Decode',fg='white',bg='black',width=20)
decbutton['font']=fontl
decbutton.place(relx=0.6,rely=0.5)

def exit():
    main.destroy()
    
closebutton=Button(text='EXIT',fg="white",bg="red",width=20,command=exit)
closebutton['font'] =fontl 
closebutton.place(relx=0.6,rely=0.7)
main.mainloop()