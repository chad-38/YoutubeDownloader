# -*- coding: utf-8 -*-
"""
Created on Thu May 27 23:23:38 2021

@author: Chad.Daud
"""
#import the libraries

from __future__ import unicode_literals
import easygui #opens the filebox
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import youtube_dl


root=tk.Tk()
root.geometry('750x750')
bg = PhotoImage(file = "C:\\Users\\Chad.Daud\\Pictures\\CdLife.png")
root.title('Youtube Video Downloader')
label=Label(root, image = bg, font=('ariel',20,'bold'))
label.place(x = 0, y = 0)

def youtube_downloader():
    #import youtube_dl
    d = easygui.enterbox("Type the Directory to save: ")
    os.chdir(d)
    URL = easygui.enterbox("Type or Paste the URL here")
    easygui.msgbox ("You entered " + URL)
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as video:
        video.download([URL])
        
        return youtube_downloader()


Download=Button(root,text="Youtube Downloader",command=lambda: youtube_downloader(),padx=30,pady=5)
Download.configure(background='#364156', foreground='blue',font=('ariel',10,'bold'))
Download.pack(side=TOP,pady=50)



plt.show()

root.mainloop()
    
    
    