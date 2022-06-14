from tkinter import *
from tkinter import messagebox
from argparse import FileType
# from stegano import lsb
from tkinter.filedialog import *
from PIL import ImageTk,Image
# from stegano.lsbset import generators
# from stegano import lsb
from tkinter import font as tkFont
# from stegano import exifHeader as aaa
import os
# from subprocess import Popen
import audioencode
import audiodecode
import imgendecode
import videoendecode 



CURRENTDIR=os.getcwd() 

    
    
def encodeimgfun():  
    main.destroy()  
    global encodeimgpage
    encodeimgpage=Tk()

    encodeimgpage.attributes("-fullscreen", True)
    # encodeimgpage.wm_attributes('-transparentcolor')
    img=ImageTk.PhotoImage(Image.open("bb1.jpg"))
    fontl = tkFont.Font(family='Algerian', size=32)
    label1=Label(encodeimgpage,image=img)
    label1.pack()

    LabelTitle=Label(text="ENCODE IMAGE",bg="red",fg="white",width=20)
    LabelTitle['font']=fontl
    LabelTitle.place(relx=0.6, rely=0.1)
    fileopen=StringVar()
    imagee=''
    def openfile():
        nonlocal fileopen
        nonlocal imagee

        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="~/Pictures",title="select file",filetypes=(("jpeg,png files","*jpg *png"),("all files","*.*"))) 
        img=Image.open(fileopen)
        img=img.resize((200,200))
        imagee=ImageTk.PhotoImage(img)

        Labelpath=Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width= 600)# 450)

        Labelimg=Label(image=imagee)
        Labelimg.place(relx=0.7, rely=0.3, height=200, width=200)


        
    Button2 = Button(text="openfile",command=openfile)
    Button2.place(relx=0.7, rely=0.2, height=31, width=94)
       

    Label1 =Label(text="Enter message")
    Label1.place(relx=0.6, rely=0.6, height=21, width=104)
    entrysecmes=Entry()
    entrysecmes.place(relx=0.7, rely=0.6, relheight=0.05, relwidth=0.200)
    
    Label2 =Label(text="File Name")
    Label2.place(relx=0.6, rely=0.70, height=21, width=104)    
    entrysave=Entry()
    entrysave.place(relx=0.7, rely=0.70, relheight=0.05, relwidth=0.200)
    
    def encode():
        inimage=fileopen
        response=messagebox.askyesno("popup","do you want to encode")
        if response==1:
            imgendecode.encodeimage(inimage,entrysecmes.get(),entrysave.get())
            messagebox.showinfo("popup","successfully encode"+entrysave.get()+'.png')               
                

    def back():
        encodeimgpage.destroy()
        HomePage()
       
    
    Button2=Button(text="ENCODE",command=encode)
    Button2.place(relx=0.7, rely=0.8, height=31, width=94)

    Buttonback = Button(text="Back",command=back)
    Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)
    
    encodeimgpage.mainloop()
                
def encodeaudiofun():
    main.destroy()
    global encodeaudiopage
    encodeaudiopage=Tk()
    encodeaudiopage.attributes("-fullscreen", True)
    # encodeaudiopage.wm_attributes('-transparentcolor')
    img=ImageTk.PhotoImage(Image.open("bb1.jpg"))
    fontl = tkFont.Font(family='Algerian', size=32)
    label1=Label(encodeaudiopage,image=img)
    label1.pack()

    LabelTitle=Label(text="ENCODE AUDIO",bg="red",fg="white",width=20)
    LabelTitle['font']=fontl
    LabelTitle.place(relx=0.6, rely=0.1)
    fileopen=StringVar()
    def openfile():
        nonlocal fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="~/Music",title="select file",filetypes=(("mp3,wav files","*mp3 *wav"),("all files","*.*"))) 

        Labelpath=Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width=600)

    Button2 = Button(text="openfile",command=openfile)
    Button2.place(relx=0.7, rely=0.2, height=31, width=94)
    
    Label1 =Label(text="Enter message")
    Label1.place(relx=0.6, rely=0.6, height=21, width=104)
    entrysecmes=Entry()
    entrysecmes.place(relx=0.7, rely=0.6, relheight=0.05, relwidth=0.200)
    
    Label2 =Label(text="File Name")
    Label2.place(relx=0.6, rely=0.70, height=21, width=104)    
    entrysave=Entry()
    entrysave.place(relx=0.7, rely=0.70, relheight=0.05, relwidth=0.200)
    
    def encode():
        inimage=fileopen
        response=messagebox.askyesno("popup","do you want to encode")
        if response==1:
            audioencode.encodeAudio(inimage,entrysecmes.get(),entrysave.get())
            messagebox.showinfo("popup","successfully encode "+entrysave.get()+'.wav')               
                
                
    def back():
        encodeaudiopage.destroy()
        HomePage()
        
        
    
    Button2=Button(text="ENCODE",command=encode)
    Button2.place(relx=0.7, rely=0.8, height=31, width=94)

    Buttonback = Button(text="Back",command=back)
    Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)
    
    encodeaudiopage.mainloop()

def encodevideofun():
    main.destroy() 
    global encodevideopage
    encodevideopage=Tk()
    encodevideopage.attributes("-fullscreen", True)

    img=ImageTk.PhotoImage(Image.open("bb1.jpg"))
    fontl = tkFont.Font(family='Algerian', size=32)
    label1=Label(encodevideopage,image=img)
    label1.pack()
    
    LabelTitle=Label(text="ENCODE VIDEO",bg="red",fg="white",width=20)
    LabelTitle['font']=fontl
    LabelTitle.place(relx=0.6, rely=0.1)
    fileopen=StringVar()

    
    def openfile():
        nonlocal fileopen
        fileopen=StringVar()       
        fileopen=askopenfilename(initialdir="~/Videos",title="select file",filetypes=(("MP4 Files","*mp4"),("all files","*.*"))) 


        Labelpath=Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width=600)


    
    Button2 = Button(text="openfile",command=openfile)
    Button2.place(relx=0.7, rely=0.2, height=31, width=94)
    
    Label1 =Label(text="Enter message")
    Label1.place(relx=0.6, rely=0.6, height=21, width=104)
    entrysecmes=Entry()
    entrysecmes.place(relx=0.7, rely=0.6, relheight=0.05, relwidth=0.200) 
    
    Label2 =Label(text="File Name")
    Label2.place(relx=0.6, rely=0.70, height=21, width=104)    
    entrysave=Entry()
    entrysave.place(relx=0.7, rely=0.70, relheight=0.05, relwidth=0.200)
    
    def encode():
        inimage=fileopen
        response=messagebox.askyesno("popup","do you want to encode")
        if response==1:
            videoendecode.encodeVideo(inimage,entrysecmes.get(),entrysave.get()+'.mp4')
            messagebox.showinfo("popup","successfully encode "+entrysave.get()+'.mp4')               

    def back():
        encodevideopage.destroy()
        HomePage()
        
    Button2=Button(text="ENCODE",command=encode)
    Button2.place(relx=0.7, rely=0.8, height=31, width=94)

    Buttonback = Button(text="Back",command=back)
    Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)
    
    encodevideopage.mainloop()
  
      
def decodeimgfun():
    main.destroy()  
    global decodeimgpage
    decodeimgpage=Tk()
    
    decodeimgpage.attributes("-fullscreen", True)
    # decodeimgpage.wm_attributes('-transparentcolor')  
    img=ImageTk.PhotoImage(Image.open("bb2.jpg"))
    fontl = tkFont.Font(family='Algerian', size=32)
    label1=Label(decodeimgpage,image=img)
    label1.pack()
    

    LabelTitle=Label(text="DECODE IMAGE",bg="blue",fg="white",width=20)
    LabelTitle['font']=fontl
    LabelTitle.place(relx=0.6, rely=0.1)
    
    # secimg=StringVar()
    # radio1=Radiobutton(text='jpeg',value='jpeg',variable=secimg)
    # radio1.place(relx=0.7, rely=0.57)
    
    # radio2=Radiobutton(text='png',value='png',variable=secimg)
    # radio2.place(relx=0.8, rely=0.57)
    fileopen=StringVar()
    imagee=''
    def openfile():
        nonlocal fileopen
        nonlocal imagee
        
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir=CURRENTDIR,title="select file",filetypes=(("jpeg files, png file","*jpg *png"),("all files","*.*")))
        img=Image.open(fileopen)
        img=img.resize((200, 200))
        imagee=ImageTk.PhotoImage(img)
        
        Labelpath=Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width=600)
        
        Labelimg=Label(image=imagee)
        Labelimg.place(relx=0.7, rely=0.3, height=200, width=200)
	
    def deimg():   
        response=messagebox.askyesno("popup","do you want to decode")
        if  response==1:      
            messag=imgendecode.decode_text(fileopen)	
                
            Label2=Label(text=messag)
            Label2.place(relx=0.7, rely=0.7, height=21, width=450)
    
    Button2 = Button(text="Openfile",command=openfile)
    Button2.place(relx=0.7, rely=0.2, height=31, width=94)
    
    Button2 = Button(text="DECODE", command=deimg)
    Button2.place(relx=0.7, rely=0.8, height=31, width=94)
    
    def back():
        decodeimgpage.destroy()
        HomePage()


    Buttonback = Button(text="Back",command=back)
    Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)
    
    decodeimgpage.mainloop()

  
def decodeaudiofun():
    main.destroy() 
    global decodeaudiopage 
    decodeaudiopage=Tk()
    decodeaudiopage.attributes("-fullscreen", True)
    # decodeaudiopage.wm_attributes('-transparentcolor')  
    img=ImageTk.PhotoImage(Image.open("bb2.jpg"))
    fontl = tkFont.Font(family='Algerian', size=32)
    label1=Label(decodeaudiopage,image=img)
    label1.pack()
    

    LabelTitle=Label(text="DECODE AUDIO",bg="blue",fg="white",width=20)
    LabelTitle['font']=fontl
    LabelTitle.place(relx=0.6, rely=0.1)
    

    fileopen=StringVar()
    def openfile():
        nonlocal fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir=CURRENTDIR,title="select file",filetypes=(("mp3,wav files","*mp3 *wav"),("all files","*.*"))) 
        

        Labelpath=Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width=600)
        
	
    def deau():	
        messag=audiodecode.decodeAudio(fileopen)
            
        Label2=Label(text=messag)
        Label2.place(relx=0.7, rely=0.7, height=21, width=450)
    
    Button2 = Button(text="Openfile",command=openfile)
    Button2.place(relx=0.7, rely=0.2, height=31, width=94)
    
    Button2 = Button(text="DECODE", command=deau)
    Button2.place(relx=0.7, rely=0.8, height=31, width=94)
    
    def back():
        decodeaudiopage.destroy()
        HomePage()
        


    Buttonback = Button(text="Back",command=back)
    Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)
    
    decodeaudiopage.mainloop()


def decodevideofun():
    main.destroy()
    global decodevideopage
    decodevideopage=Tk()
    decodevideopage.attributes("-fullscreen", True)

    img=ImageTk.PhotoImage(Image.open("bb2.jpg"))
    fontl = tkFont.Font(family='Algerian', size=32)
    label1=Label(decodevideopage,image=img)
    label1.pack()
    

    LabelTitle=Label(text="DECODE AUDIO",bg="blue",fg="white",width=20)
    LabelTitle['font']=fontl
    LabelTitle.place(relx=0.6, rely=0.1)
    
    fileopen=StringVar()
    def openfile():
        nonlocal fileopen
        
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir=CURRENTDIR,title="select file",filetypes=(("MP4 Files","*mp4"),("all files","*.*"))) 
        Labelpath=Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width=600)
        
    def devid():
        response=messagebox.askyesno("popup","do you want to decode")
        if response==1:
            messag=videoendecode.decode_string(fileopen)
                
            Label2=Label(text=messag)
            Label2.place(relx=0.7, rely=0.7, height=21, width=450)
        
    Button2 = Button(text="Openfile",command=openfile)
    Button2.place(relx=0.7, rely=0.2, height=31, width=94)
    
    Button2 = Button(text="DECODE", command=devid)
    Button2.place(relx=0.7, rely=0.8, height=31, width=94)    

    def back():
        decodevideopage.destroy()
        HomePage()
        


    Buttonback = Button(text="Back",command=back)
    Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)
    
    decodevideopage.mainloop()
    
   
def HomePage():
    # main program
    global main
    main=Tk()
    
    main.title('Enc & Dec Panel')
    # main.geometry('1300x750')
    main.attributes('-fullscreen',True)
    fontl = tkFont.Font(family='Algerian',size=20)


    image1=ImageTk.PhotoImage(Image.open('bb1.jpg'))
    label=Label(main,text='lalal',image=image1)
    label.pack()

    encbutton1=Button(text='Encode Image',fg='white',bg='black',width=15,command=encodeimgfun)
    encbutton1['font'] =fontl 
    encbutton1.place(relx=0.5,rely=0.3)
    
    encbutton2=Button(text='Encode Audio',fg='white',bg='black',width=15 ,command=encodeaudiofun)
    encbutton2['font'] =fontl 
    encbutton2.place(relx=0.5,rely=0.4)
    
    encbutton3=Button(text='Encode Video',fg='white',bg='black',width=15 ,command=encodevideofun)
    encbutton3['font'] =fontl 
    encbutton3.place(relx=0.5,rely=0.5)

    decbutton1=Button(text='Decode Image',fg='white',bg='black',width=15 ,command=decodeimgfun)
    decbutton1['font']=fontl
    decbutton1.place(relx=0.7,rely=0.3)
    
    decbutton2=Button(text='Decode Audio',fg='white',bg='black',width=15 ,command=decodeaudiofun)
    decbutton2['font']=fontl
    decbutton2.place(relx=0.7,rely=0.4)
    
    decbutton3=Button(text='Decode Video',fg='white',bg='black',width=15 ,command=decodevideofun)
    decbutton3['font']=fontl
    decbutton3.place(relx=0.7,rely=0.5)

    def exit():
        main.destroy()

        
        
    closeButton=Button(text='EXIT',fg='white',bg='red',width=20,command=exit)
    closeButton['font']=fontl
    closeButton.place(relx=0.6,rely=0.7)
    main.mainloop()



HomePage()
