from tkinter import *
from tkinter .messagebox import showinfo
from tkinter .filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title('Untitled - Notepad')
    file = None
    textArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file =='':
        file=None
    else:
        root.title(os.path.basename(file)+' - Notepad')
        textArea.delete(1.0,END)
        f = open(file,'r')
        textArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file== None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt', filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        if file == '':
            file = None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()
def quitApp():
    root.destroy()

def cut():
    textArea.event_generate('<<Cut>>')

def copy():
    textArea.event_generate('<<Copy>>')

def paste():
    textArea.event_generate('<<Paste>>')

def about():
    showinfo('Notepad','Developed by Vipashana')


if __name__ == '__main__':
    root = Tk()
    root.title('Untitled - Notepad')
    root.wm_iconbitmap('notepad_47704.ico')
    root.geometry('645x766')

    #Text Area
    textArea = Text(root, font='lucida 13')
    file = None
    textArea.pack(expand=True,fill=BOTH)

    #Menuabar
    menuBar = Menu(root)

    #File menu Starts
    fileMenu = Menu(menuBar, tearoff=0)
    #To open new file
    fileMenu.add_command(label = 'New', command = newFile)
    #To open already  existing file
    fileMenu.add_command(label='Open',command=openFile)
    #To save the current file
    fileMenu.add_command(label='Save',command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit',command=quitApp)
    menuBar.add_cascade(label='File',menu=fileMenu)
    #file menu ends

    #Edit menu starts
    editMenu = Menu(menuBar, tearoff=0)
    #Adding cut, copy and paste features
    editMenu.add_command(label='Cut',command=cut)
    editMenu.add_command(label='Copy',command=copy)
    editMenu.add_command(label='Paste',command=paste)
    menuBar.add_cascade(label='Edit',menu=editMenu)
    #Edit menu ends

    #Help menu starts
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label='About Notepad',command=about)
    menuBar.add_cascade(label='Help',menu=helpMenu)
    #Help menu ends

    root.config(menu=menuBar)

    #Adding ScrollBar
    scrollBar = Scrollbar(textArea)
    scrollBar.pack(fill=Y,side=RIGHT)
    scrollBar.config(command=textArea.yview)
    textArea.config(yscrollcommand=scrollBar.set)


    root.mainloop()