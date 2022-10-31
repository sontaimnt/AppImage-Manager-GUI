#Dependencies
from tkinter import *
from os.path import isfile , isdir
from os import system

root=Tk()
root.title('App Image Manager')
root.geometry('400x400')

canvas=Canvas(root , width=400 , height=80)
canvas.pack(side="top")

button1=Button(root , text='Install')
canvas.create_window(150 , 45, window=button1)

button2=Button(root , text='Uninstall')
canvas.create_window(250 , 45, window=button2)

class Install():
    def from_path(path):
        pathexists=isfile(path)
        #if pathexists==True:

def check_on_startup():
    isdir('.local/appimage-manager')

root.mainloop()
