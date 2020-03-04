#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.8.1
#
# Author:       Bianca McKenzie
#
# Purpose:      Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import filedialog
import shutil
import time

#import function file so we can have access to them
#import checkfiles_124_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(650,250) #(Height, Width)
        self.master.maxsize(650,1500)  #with max size same as minsize, the user cannot change size of window
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        self.folder_path1 = StringVar()
        self.folder_path2 = StringVar()
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        #self.master.protocol("WM_DELETE_WINDOW",lambda: checkfiles_func.ask_quit(self))
        #arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        load_gui(self)


def load_gui(self):
    #settin up the grid
    #browse 1
    self.lbl_browse1 = tk.Label(self.master,text='Choose a Source Directory to Browse for .txt files...')
    self.lbl_browse1.grid(row=1,column=1,columnspan=50,padx=(20,0),pady=(20,0),sticky=W)

    self.btn_browse1 = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda: browse_button1(self))
    self.btn_browse1.grid(row=2,column=1,padx=(20,0),sticky=W)

    self.txt_browse1 = tk.Entry(self.master,width=75,textvariable=self.folder_path1)
    self.txt_browse1.grid(row=2,column=2,padx=(20,0),sticky=W)

    #browse 2
    self.lbl_browse2 = tk.Label(self.master,text='Choose a Destination Directory to move the .txt files...')
    self.lbl_browse2.grid(row=6,column=1,columnspan=50,padx=(20,0),pady=(30,0),sticky=W)
    
    self.btn_browse2 = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda: browse_button2(self))
    self.btn_browse2.grid(row=7,column=1,rowspan=1,padx=(20,0),sticky=W)
    
    self.txt_browse2 = tk.Entry(self.master,width=75,textvariable=self.folder_path2)
    self.txt_browse2.grid(row=7,column=2,padx=(20,0),sticky=W)
    
    #check for txt files
    self.btn_check = tk.Button(self.master,width=15,height=2,text='Check for files...',command=lambda: check_button(self))
    self.btn_check.grid(row=11,column=1,rowspan=2,padx=(20,0),pady=(30,0),sticky=W)

    #close button
    self.btn_close = tk.Button(self.master,width=15,height=2,text=' Close Program ',command=lambda: ask_quit(self))
    self.btn_close.grid(row=11,column=2,rowspan=2,columnspan=3,padx=(20,0),pady=(30,0),sticky=E)

   

# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    self.master.destroy()
    os._exit(0)

        

#askdirectory on browse button
def browse_button1(self):
    foldername1 = filedialog.askdirectory()
    self.folder_path1.set(foldername1)
    print(foldername1)
    return foldername1
    

def browse_button2(self):
    foldername2 = filedialog.askdirectory()
    self.folder_path2.set(foldername2)
    print(foldername2)
    
#check for txt files
def check_button(self):
    localfile1 = self.folder_path1.get()
    destination = self.folder_path2.get()
    for file in os.listdir(localfile1):
        if file.endswith(".txt"):
            joinfile = os.path.join(localfile1, file)
            modtime = os.path.getmtime(joinfile)
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modtime))
            print(file, "Last Modified Time : ", modificationTime)
            add_data(file,modificationTime)
            shutil.move(joinfile,destination)
            
            


def create_db():
    conn = sqlite3.connect('db_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_txtfiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_modtime TEXT)")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
   

def add_data(file,modificationTime):
    conn = sqlite3.connect('db_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_txtfiles (col_fname,col_modtime) values(?,?)", (file,modificationTime))
        conn.commit()
    conn.close()

'''
#move function from source to destination (file_path1 to file_path2)

def movefiles():
    source = self.folder_path1.get()
    destination = self.folder_path2.get()
    for files in source:
        if files.endswith(".txt"):
            shutil.copy(files,source)
            shutil.move(files,destination)
            print(files,destination)

'''

if __name__ == "__main__":
    create_db()
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
    
    
