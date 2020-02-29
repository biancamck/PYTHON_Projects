#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.8.1
#
# Author:       Bianca McKenzie
#
# Purpose:      File Checker. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.

import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk



# Be sure to import our other modules 
# so we can have access to them

import checkfiles_gui


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

        

#askdirectory on browse button
def browse_button(self):
    foldername = filedialog.askdirectory()
    self.folder_path.set(foldername)


    print(foldername)
    return foldername

"""
root = Tk()
v = StringVar()
button2 = Button(text="Browse", command=browse_button).grid(row=0, column=3)

mainloop()
"""

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
