#Dependencies
from tkinter import *
from os.path import isfile , isdir
from os import system , chdir , getlogin
from validators import url
from requests import get

user=getlogin()

root=Tk()
root.title('App Image Manager')
root.geometry('400x400')

canvas=Canvas(root , width=400 , height=80)
canvas.pack(side="top")

button1=Button(root , text='Install')
canvas.create_window(150 , 45, window=button1)

button2=Button(root , text='Uninstall')
canvas.create_window(250 , 45, window=button2)

prcsexit=None

class Install():
    def from_path(file):
        pathexists=isfile(file)
        if pathexists==True:
            system(f'cp {file} ~/appimage-manager')
        else:
           return FileNotFoundError;prcsexit==int(1)

    def from_link(link , filename):
        global prcsexit
        urlistrue=url(link)
        if urlistrue==True:
            chdir(f'/home/{user}/appimage-manager')
            file=get(link)
            appimage=open(filename , 'wb')
            appimage.write(file.content)
            system(f"chmod +x {filename}")
            prcsexit=int(0)
        else:
            return ValueError;prcsexit==int(1)

class Install_Dialog():
    def __init__():
        global GUI
        GUI=Tk()
        GUI.title('Installation Mode:-')
        GUI.geometry('300x150')

        Install_Dialog.elements_load()            
        GUI.mainloop()
    
    def elements_load():
        global canvasdb , buttononline , buttonoffline
        canvasdb=Canvas(GUI , width=300 , height=150)
        canvasdb.pack()
        canvasdb.create_window(150 , 30, window=Label(canvasdb , text="Select Install Mode:-"))

        buttononline=Button(GUI , text='Online Install')
        buttonoffline=Button(GUI , text='Offline Install')
        canvasdb.create_window(150 , 75, window=buttononline)
        canvasdb.create_window(150 , 115, window=buttonoffline)

        buttononline.configure(command=InstallType_dialogs.online)

class InstallType_dialogs():
    def online():
        global onlinedb
        GUI.destroy()
        onlinedb=Tk()
        onlinedb.title('Installing Appimage:-')
        onlinedb.mainloop()

def check_on_startup():
    direxists=isdir(f'/home/{user}/appimage-manager')
    if direxists==True:
        pass
    else:
        system('mkdir appimage-manager')

button1.configure(command=Install_Dialog.__init__)

check_on_startup()
root.mainloop()
