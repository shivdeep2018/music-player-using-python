from tkinter import *
from PIL import Image,ImageTk
import os
import time
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
mixer.init()

class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        
        self.root.title('Music_Player')
        
        self.root.geometry('600x400')
        self.root.resizable(0,0)

        self.root.configure(background='white')

        def Openfile():
            global filename
            filename=filedialog.askopenfilename()

        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)
      
        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='File',menu=self.submenu)
        self.submenu.add_command(label='Open',command=Openfile)
        self.submenu.add_command(label='Exit',command=self.root.destroy)
               
        self.submenu2=Menu(self.menubar,tearoff=0)
              
        self.filelabel=Label(text='Select And Play',bg='black',fg='white',font=22)
        self.filelabel.place(x=5,y=30)
      
        def songinf():
            self.filelabel['text']='Current Music :-' + os.path.basename(filename)

        self.photo=ImageTk.PhotoImage(file='music2.png')
        photo=Label(self.root,image=self.photo,bg='white').place(x=200,y=60)
        
        self.label1=Label(self.root,text='Lets Play It.',bg='black',fg='white',font=20)
        self.label1.pack(side=BOTTOM,fill=X)
  
        def playmusic():
            try:
                paused
            except NameError:
                try:
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text']='Music_Playing..'
                    songinf()
                    length_bar()
                    
                    
                    self.imglabel=Label(self.root,bg='white')
                    self.imglabel.place(x=5,y=60)
               
                except:
                    tkinter.messagebox.showerror('Error','File Could Not Found, Please Try Again...')
            
            else:
                mixer.music.unpause()
                
                self.imglabel=Label(self.root,bg='white')
                self.imglabel.place(x=5,y=60)
                self.label1['text']='Music_Playing..'   
                

                self.imglabel=Label(self.root,bg='white')
                self.imglabel.place(x=5,y=60)

        def length_bar():

            current_time=mixer.music.get_pos()/1000
         
            convert_current_time=time.strftime('%M:%S',time.gmtime(current_time))
           
            song_mut=MP3(filename)
           
            song_mut_length=song_mut.info.length
            convert_song_mut_length=time.strftime('%M:%S',time.gmtime(song_mut_length))
            self.lengthbar.config(text=f'Total_Length:-{convert_current_time}:{convert_song_mut_length}')
            self.lengthbar.after(1000,length_bar)

        self.lengthbar=Label(self.root,text='Total_Length:-00:00',font=20,bg='black',fg='white')
        self.lengthbar.place(x=5,y=270)

        self.photo_B1=ImageTk.PhotoImage(file='3.jpeg')
        photo_B1=Button(self.root,image=self.photo_B1,bd=0,bg='white',command=playmusic).place(x=5,y=300)        

        def pausemusic():
            global paused
            paused=TRUE
            mixer.music.pause()
            self.label1['text']='Music_Paused'
            self.photo=ImageTk.PhotoImage(file='music2.png')
            photo=Label(self.root,image=self.photo,bg='white').place(x=5,y=60)

        self.photo_B2=ImageTk.PhotoImage(file='4.jpeg')
        photo_B2=Button(self.root,image=self.photo_B2,bd=0,bg='white',command=pausemusic).place(x=85,y=300)        
        
        def stopmusic():
            mixer.music.stop()
            self.label1['text']='Music_Stoped'
            self.photo=ImageTk.PhotoImage(file='music2.png')
            photo=Label(self.root,image=self.photo,bg='white').place(x=5,y=60)
            
        self.photo_B3=ImageTk.PhotoImage(file='5.jpeg')
        photo_B3=Button(self.root,image=self.photo_B3,bd=0,bg='white',command=stopmusic).place(x=165,y=300)        
        

        def mute():
            self.scale.set(0)
            self.mute=ImageTk.PhotoImage(file='mute.jpeg')
            mute=Button(self.root,image=self.mute,command=unmute,bg='white',bd=0).place(x=280,y=290)
            self.label1['text']='Music_Mute'
            
        def unmute():
            self.scale.set(30)
            self.volimg=ImageTk.PhotoImage(file='6.jpeg')
            volimg=Button(self.root,image=self.volimg,command=mute,bg='white',bd=0).place(x=280,y=290)
            self.label1['text']='Music_Playing'
       
        self.volimg=ImageTk.PhotoImage(file='6.jpeg')
        volimg=Button(self.root,image=self.volimg,command=mute,bg='white',bd=0).place(x=280,y=290)

        def volume_(vol):
            volume= int(vol)/100
            mixer.music.set_volume(volume)
        
        self.scale=Scale(self.root,from_=0,to=100,bg='cyan',
                        orient=HORIZONTAL,length=120,command=volume_)
        self.scale.set(30)
        self.scale.place(x=330,y=290)
       

root=Tk()
obj=musicplayer(root)
root.mainloop()
