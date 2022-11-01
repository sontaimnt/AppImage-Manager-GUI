#Sticky.py
from tkinter import *
from tkinter.messagebox import *
from random import randint
#Program
root=Tk()
root.title('Sticky Notes')
root.geometry('300x300')
#Main Box
text=Text(bg='#f9f06d' , width=300 , height=300 , font=('Comic Sans MS' , 12))
text.pack()
#Functions
def new_note():
    color=randint(1 , 6)
    note=Tk()
    note.geometry('300x300')
    note.title('Sticky Notes')
    text=Text(note , width=300 , height=300 , font=('Comic Sans MS' , 12))
    if color==int(1):
        text.configure(bg='#f9f06d')
    elif color==int(2):
        text.configure(bg='#F86052' , fg='white')    
    elif color==int(3):
        text.configure(bg='#FDBE71')
    elif color==int(4):
        text.configure(bg='#8FF0A3')
    elif color==int(5):
        text.configure(bg='#99C2F0')
    elif color==int(6):
        text.configure(bg='#DC8ADE')
    text.pack()
    menubar=Menu(note ,  bg='#F2F1EF' , fg='#3C3846')
    fileMenu=Menu(note ,  bg='#F2F1EF' , fg='#3C3846')
    fileMenu.add_command(label='New Note' , command=new_note)
    menubar.add_cascade(label='File' , menu=fileMenu)
    note.configure(menu=menubar)                    
    note.mainloop()
#Bold Text
def bold():
    boldtext=True
    text.configure(font=('Comic Sans MS' , 12 , 'bold'))      
#Menu
menubar=Menu(root , bg='#F2F1EF' , fg='#3C3846')
#File Menu
fileMenu=Menu(root ,  bg='#F2F1EF' , fg='#3C3846')
fileMenu.add_command(label='New Note' , command=new_note)
#Format Menu
formatmenu=Menu(root ,  bg='#F2F1EF' , fg='#3C3846')
formatmenu.add_command(label='Bold' , command=bold)
#Configuration
menubar.add_cascade(label='File' , menu=fileMenu)
menubar.add_cascade(label='Format' , menu=formatmenu)
root.configure(menu=menubar)
#Execution
root.mainloop()