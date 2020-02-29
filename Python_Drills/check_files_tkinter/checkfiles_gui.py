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
import checkfiles_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,200) #(Height, Width)
        self.master.maxsize(500,200)  #with max size same as minsize, the user cannot change size of window
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        self.folder_path = StringVar()
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        #self.master.protocol("WM_DELETE_WINDOW",lambda: checkfiles_func.ask_quit(self))
        #arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        load_gui(self)


def load_gui(self):
    #settin up the grid - left buttons
    self.btn_browse = tk.Button(self.master,width=15,height=1,text='Browse...',command=lambda: checkfiles_func.browse_button(self))
    self.btn_browse.grid(row=1,column=1,rowspan=1,padx=(20,0),pady=(20,0),sticky=E+N)
    self.btn_browse = tk.Button(self.master,width=15,height=1,text='Browse...')#,command=lambda: browse_button(self))
    self.btn_browse.grid(row=2,column=1,rowspan=1,padx=(20,0),pady=(20,0),sticky=E+N)
    self.btn_check = tk.Button(self.master,width=15,height=2,text='Check for files...')#,command=lambda: checkfiles_func.check_button(self))
    self.btn_check.grid(row=3,column=1,rowspan=2,padx=(20,0),pady=(20,0),sticky=E+N)

    #right blank boxes
    self.txt_browse = tk.Entry(self.master,width=50,textvariable=self.folder_path)
    self.txt_browse.grid(row=1,column=2,rowspan=1,columnspan=15,padx=(20,0),pady=(20,0),sticky=S+W)
    self.txt_browse = tk.Entry(self.master,width=50,text='')
    self.txt_browse.grid(row=2,column=2,rowspan=1,columnspan=15,padx=(20,0),pady=(20,0),sticky=S+W)

    #close button
    self.btn_close = tk.Button(self.master,width=15,height=2,text=' Close Program ')#,command=lambda: checkfiles_func.ask_quit(self))
    self.btn_close.grid(row=3,column=15,rowspan=2,columnspan=3,padx=(20,0),pady=(20,0),sticky=W+N)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
