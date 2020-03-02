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
import sqlite3
import shutil



# Be sure to import our other modules 
# so we can have access to them

import checkfiles_124_gui


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
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
    for file in os.listdir(self.foldername1):
        if file.endswith(".txt"):
           modtime = os.path.getmtime(file)
           modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modtime))
           joinfile = os.path.join(location, file)
           print(file, "Last Modified Time : ", modificationTime)



def create_db(self):
    conn = sqlite3.connect('db_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_txtfile( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_modtime TEXT \
            );")
        # You must commit() to save changes & close the database connection
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_files (col_fname,col_modtime) VALUES (?,?)""", ('bianca.txt','2020-03-02 11:28:03'))
            conn.commit()
    conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root, foldername1)
    root.mainloop()
