
#
# Python Ver:   3.8.1
#
# Author:       Bianca McKEnzie
#
# Purpose:      Check Files. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk


# Be sure to import our other modules 
# so we can have access to them
import checkfiles_gui
#import checkfiles_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,200) #(Height, Width)
        self.master.maxsize(500,200)  #with max size same as minsize, the user cannot change size of window
        # This CenterWindow method will center our app on the user's screen
        #checkfiles_func.center_window(self,600,300)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        #self.master.protocol("WM_DELETE_WINDOW",lambda: checkfiles_func.ask_quit(self))
        #arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        checkfiles_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
