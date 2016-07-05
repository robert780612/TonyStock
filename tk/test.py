# from tkinter import *
#
# counter = 0
#
# def update():
#     global counter
#     counter = counter + 1
#     menu.entryconfig(0, label=str(counter))
#
# root = Tk()
#
# menubar = Menu(root)
#
# menu = Menu(menubar, tearoff=0, postcommand=update)
# menu.add_command(label=str(counter))
# menu.add_command(label="Exit", command=root.quit)
#
# menubar.add_cascade(label="Test", menu=menu)
#
#
# root.config(menu=menubar)
# menu.pack()
#
# root.mainloop()

from tkinter import *
import random

def About():
    print('This')

def update():
    a = random.random()
    countmenu.entryconfig(0, label=str(a))

root=Tk()
menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label="About...", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

count = IntVar()
count.set(0)
countmenu = Menu(menubar, postcommand=update)
countmenu.add_command(label='Value')
menubar.add_cascade(label='Count', menu=countmenu)


root.config(menu=menubar)
root.mainloop()