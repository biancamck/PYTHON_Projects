#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.5.1
#
# Author:       Daniel A. Christi#e
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


import os
from tkinter import *
import tkinter as tk

#import function file so we can have access to them
import checkfiles_124_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, foldername1, *args, **kwargs):
        Frame.__init__(self, master, foldername1, *args, **kwargs)

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

    self.btn_browse1 = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda: checkfiles_124_func.browse_button1(self))
    self.btn_browse1.grid(row=2,column=1,padx=(20,0),sticky=W)

    self.txt_browse1 = tk.Entry(self.master,width=75,textvariable=self.folder_path1)
    self.txt_browse1.grid(row=2,column=2,padx=(20,0),sticky=W)

    #browse 2
    self.lbl_browse2 = tk.Label(self.master,text='Choose a Source Directory to move the .txt files...')
    self.lbl_browse2.grid(row=6,column=1,columnspan=50,padx=(20,0),pady=(30,0),sticky=W)
    
    self.btn_browse2 = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda: checkfiles_124_func.browse_button2(self))
    self.btn_browse2.grid(row=7,column=1,rowspan=1,padx=(20,0),sticky=W)
    
    self.txt_browse2 = tk.Entry(self.master,width=75,textvariable=self.folder_path2)
    self.txt_browse2.grid(row=7,column=2,padx=(20,0),sticky=W)
    
    #check for txt files
    self.btn_check = tk.Button(self.master,width=15,height=2,text='Check for files...',command=lambda: checkfiles_124_func.check_button(self))
    self.btn_check.grid(row=11,column=1,rowspan=2,padx=(20,0),pady=(30,0),sticky=W)

    #close button
    self.btn_close = tk.Button(self.master,width=15,height=2,text=' Close Program ')#,command=lambda: checkfiles_124_func.ask_quit(self))
    self.btn_close.grid(row=11,column=2,rowspan=2,columnspan=3,padx=(20,0),pady=(30,0),sticky=E)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
