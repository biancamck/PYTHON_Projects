#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.5.1
#
# Author:       Daniel A. Christie
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

# Be sure to import our other modules 
# so we can have access to them
import checkfiles_main
#import checkfiles_func



def load_gui(self):
    #settin up the grid - left buttons
    self.btn_browse = tk.Button(self.master,width=15,height=1,text='Browse...')#,command=lambda: checkfiles_func.browse(self))
    self.btn_browse.grid(row=1,column=1,rowspan=1,padx=(20,0),pady=(20,0),sticky=E+N)
    self.btn_browse = tk.Button(self.master,width=15,height=1,text='Browse...')#,command=lambda: checkfiles_func.browse(self))
    self.btn_browse.grid(row=2,column=1,rowspan=1,padx=(20,0),pady=(20,0),sticky=E+N)
    self.btn_check = tk.Button(self.master,width=15,height=2,text='Check for files...')#,command=lambda: checkfiles_func.check(self))
    self.btn_check.grid(row=3,column=1,rowspan=2,padx=(20,0),pady=(20,0),sticky=E+N)

    #right blank boxes
    self.txt_browse = tk.Entry(self.master,width=50,text='')
    self.txt_browse.grid(row=1,column=2,rowspan=1,columnspan=15,padx=(20,0),pady=(20,0),sticky=S+W)
    self.txt_browse = tk.Entry(self.master,width=50,text='')
    self.txt_browse.grid(row=2,column=2,rowspan=1,columnspan=15,padx=(20,0),pady=(20,0),sticky=S+W)

    #close button
    self.btn_close = tk.Button(self.master,width=15,height=2,text=' Close Program ')#,command=lambda: checkfiles_func.ask_quit(self))
    self.btn_close.grid(row=3,column=15,rowspan=2,columnspan=3,padx=(20,0),pady=(20,0),sticky=W+N)



if __name__ == "__main__":
    pass
