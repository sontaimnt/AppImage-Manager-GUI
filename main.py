#Dependencies
from tkinter import *
from os.path import isfile , isdir
from os import system , chdir , getlogin
from validators import url
from requests import get

prcsexit=None

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
            chdir('/home/{user}/appimage-manager')
            file=get(link)
            appimage=open(filename , 'wb')
            appimage.write(file.content)
            prcsexit=int(0)
        else:
            global prcsexit
            return ValueError;prcsexit==int(1)



def check_on_startup():
    direxists=isdir('appimage-manager')
    if direxists:=True:
        pass
    else:
        system('mkdir appimage-manager')

check_on_startup()
root.mainloop()
