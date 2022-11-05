#Dependencies 
from tkinter import Canvas , Tk , Entry , Button , Listbox , Label , Scrollbar , END , LEFT , RIGHT , BOTH
from tkinter.messagebox import showinfo , showerror
from os.path import isfile , isdir
from subprocess import check_output
from os import system , chdir , getlogin
from validators import url
from requests import get

user=getlogin()

root=Tk()
root.title('App Image Manager')
root.geometry('400x400')

canvas=Canvas(root , width=400 , height=80)
canvas.pack(side="top")

scbar=Scrollbar(root)
scbar.pack(side = RIGHT, fill = BOTH)

button1=Button(root , text='Install')
canvas.create_window(100 , 45, window=button1)

button2=Button(root , text='Uninstall')
canvas.create_window(200 , 45, window=button2)

button3=Button(root , text="Run")
canvas.create_window(300 , 45, window=button3)

prcsexit=None

class Install():
    def from_path(file):
        pathexists=isfile(file)
        if pathexists==True:
            system(f'cp {file} ~/appimage-manager')
            chdir(f'/home/{user}/appimage-manager')
            system(f'chmod 755 {file}')
            showinfo('Sucess:-' , f'{file} was installed succesfully')
            lbox.forget();show_main();lbox.pack()
        else:
            prcsexit==int(1)
            showerror('Error' , 'The specified  file does not exists')

    def from_link(link , filename):
        global prcsexit , file
        urlistrue=url(link)
        if urlistrue==True:
            chdir(f'/home/{user}/appimage-manager')
            try:
                file=get(link)
                filedownload=True
            except Exception:
                filedownload=False
                showerror("Error" , 'Internet is not connected')

            if filedownload==True:
                appimage=open(filename , 'wb')
                appimage.write(file.content)
                system(f"chmod +x {filename}")
                prcsexit=int(0)
                showinfo("Sucess" , 'AppImage sucessfully installed')
                lbox.forget();show_main();lbox.pack()
                onlinedb.destroy()
            else:
                onlinedb.destroy()
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
        buttonoffline.configure(command=InstallType_dialogs.offline)

class InstallType_dialogs():
    def online():
        global onlinedb , link , filename
        GUI.destroy()
        onlinedb=Tk()
        onlinedb.title('Installing Appimage:-')
        onlinedb.geometry('320x200')
        onlinedbc=Canvas(onlinedb , width=320 , height=200)
        onlinedbc.pack()
        onlinedbc.create_window(150 , 30, window=Label(onlinedb , text="Enter some details:-"))
        onlinedbc.create_window(40 , 70, window=Label(onlinedb , text="Source:-"))
        e1=Entry(onlinedb)
        e2=Entry(onlinedb)
        onlinedbc.create_window(195 , 70 , window=e1)
        onlinedbc.create_window(40 , 100, window=Label(onlinedb , text="FlName:-"))
        onlinedbc.create_window(195 , 100 , window=e2)
        ButtonSbmt=Button(onlinedb , text='Submit' , command=lambda:Install.from_link(link=e1.get() , filename=e2.get()))
        onlinedbc.create_window(150 , 150, window=ButtonSbmt)
        onlinedb.mainloop()

    def offline():
        global offlinedb
        GUI.destroy()
        offlinedb=Tk()
        offlinedb.title('Offline Install')
        offlinedb.geometry('320x100')

        offlinedc=Canvas(offlinedb , width=320 , height=100)
        offlinedc.pack()

        entryoffline=Entry(offlinedb)
        install=Button(offlinedb , text="Install" , command=lambda:Install.from_path(file=entryoffline.get()))
        offlinedc.create_window(40 , 30 , window=Label(offlinedb , text="Path:-"))
        offlinedc.create_window(195 , 30, window=entryoffline)
        offlinedc.create_window(150 , 70, window=install)
        
        offlinedb.mainloop()

class run_appimages():
    def __init__():
        global rundialog  , canvasrun , button , e3

        rundialog=Tk()
        rundialog.title('AppImage Runner')
        rundialog.geometry('300x100')
    
        canvasrun=Canvas(rundialog , width=300 , height=100)
        canvasrun.pack()

        e3=Entry(rundialog)
        canvasrun.create_window(180 , 30, window=e3)

        canvasrun.create_window(30 , 30, window=Label(canvasrun , text="File:-"))

        button=Button(canvasrun , text="Submit" , command=lambda:run_appimages.run_f(file=e3.get()))
        canvasrun.create_window(150 , 75, window=button)

        rundialog.mainloop() 

    def run_f(file):
        rundialog.destroy()
        chdir(f"/home/{user}/appimage-manager")
        fileexitsts=isfile(file)
        appimagetrue='AppImage' in file
        if fileexitsts==True and appimagetrue==True:
            system(f'./{file}')
        else:
            showerror('Error' , f'{file} not found in direcotry or {file} is not an AppImage')

def check_on_startup():
    direxists=isdir(f'/home/{user}/appimage-manager')
    if direxists==True:
        pass
    else:
        system('mkdir appimage-manager')

def show_main():
    global lbox , elements
    chdir(f'/home/{user}/appimage-manager')
    appimages=check_output('ls').decode('utf-8')
    #Converting it to a set
    set=appimages.splitlines()
    elements=len(set)

    lbox=Listbox(root , bg="white" , width=250 , height=300)

    num=0

    lbox.delete(0 , END)

    if elements==int(0):
        pass
    else:
        num=0
        lbox.insert(num , set[0])
        for i in range(num+1 , elements):
            num=num+1
            lbox.insert(num , set[num])        

button1.configure(command=Install_Dialog.__init__)
button3.configure(command=run_appimages.__init__)

show_main()

if elements==int(0):
    lbox.pack(side="left")
else:
    show_main()
    lbox.pack(side="left")

lbox.pack(side = LEFT, fill = BOTH)

lbox.config(yscrollcommand=scbar.set)
scbar.config(command=lbox.yview)

check_on_startup()
root.mainloop()
