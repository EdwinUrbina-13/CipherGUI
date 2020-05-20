# CipherGUI
import tkinter as tk
import tkinter.scrolledtext as tkScroll
from tkinter import filedialog
import os

from DoubleTranspositionCipher import *
from MorseCodeCipher import *

global root
root = tk.Tk()
root.title('Cipher Buddy')


def menuBar():
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    fileMenu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=lambda: os.startfile(r'CipherGUI.py'))
    fileMenu.add_command(label="Open", command=selectFile)
    fileMenu.add_command(label="Save as...", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=root.destroy)

    editMenu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Undo", command=lambda: executeText.edit_undo())
    editMenu.add_command(label="Redo", command=lambda: executeText.edit_redo())
    editMenu.add_command(label="Cut", command=lambda: root.focus_get().event_generate('<<Cut>>'))
    editMenu.add_command(label="Copy", command=lambda: root.focus_get().event_generate('<<Copy>>'))
    editMenu.add_command(label="Paste", command=lambda: root.focus_get().event_generate('<<Paste>>'))

    helpMenu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Help", menu=helpMenu)
    helpMenu.add_command(label="About...", command=lambda: infoProgram(1))
    helpMenu.add_command(label="How does it work?", command=lambda: infoProgram(2))

    cipherInfoMenu = tk.Menu(menubar, tearoff=0)

    helpMenu.add_cascade(label="Cipher Options Info", menu=cipherInfoMenu)
    cipherInfoMenu.add_command(label="Morse Code", command=lambda: cipherInfo(1))
    cipherInfoMenu.add_command(label="Double Transposition", command=lambda: cipherInfo(2))


def selectFile():
    fileName = tk.filedialog.askopenfilename(title="Select a file", filetypes=[("txt Files", "*.txt")])
    fileEntry.delete(0, "end")
    fileEntry.insert(0, fileName)


def saveFile():
    fileSave = tk.filedialog.asksaveasfile(mode='w', defaultextension=[("txt Files", "*.txt")])
    fileSave.write("Original text: \n")
    fileSave.write(executeText.get("1.0", "end") + "\n")
    fileSave.write("Encrypted or Decrypted text: \n")
    fileSave.write(answerText.get("1.0", "end"))


def insertFile():
    aFile = open(fileEntry.get())
    fileText = aFile.read()
    executeText.delete("1.0", "end")
    executeText.insert("1.0", fileText)

    aFile.close()


def infoProgram(choice):
    infoWindow = tk.Tk()

    if choice == 1:
        about = tk.Label(infoWindow, text="""This application was built in order to facilitate a user friendly encryption program.
        It was created as well to show how to create an intermidiate level GUI Applcation using Tkinter. Feel free to update, add to, or
        incorporate this program however you see fit. Hope you enjoy using it as much as me enjoyed making it.\n\n
        CREATORS: Edwin Urbina   Luis Alcaraz   Paola Guadalupe""")
        about.pack()

    else:
        howTo = tk.Label(infoWindow, text="""STEP 1: Load a text file from the 'File Menu' or write the path, and insert it;
        or write a text into the first entry box.\n
        STEP 2: Select a cipher option from the drop down menu and press 'Select'\n
        STEP 3: Press either the 'Encrypt' or 'Decrypt' option button.\n
        STEP 4: Save the resulting text in a text file with the 'Save as...' option from the 'File Menu'""")
        howTo.pack()


def cipherInfo(choice):
    infoWindow = tk.Tk()

    if choice == 1:
        morseCodeInfo = tk.Label(infoWindow, text="""A Morse Code is the method of writing
        with dots and dashes to encrypt letters and symbols. This was created in order send
        messages through the telegraph created by Samuel Morse, to which this style of encryption is named after.""")
        morseCodeInfo.pack()

    elif choice == 2:
        dtInfo = tk.Label(infoWindow, text="""A Double Transposition Cipher is the application of a Columnar Transposition twice.
        You start by picking two key words. Your text is converted into a matrix where its number of columns is dipicted by the letters in your key word.
        Then it starts transposing your matrix by column in alphabetical order. Then it does this process again with the next key word. The decryption
        method is just the opposite where your matrix's first column is the key word and you transpose the rows in the order of the key word.\n\n
        For purpose of this cipher GUI, the key word is set to lower case and the redundant letters are removed after the first appearnce.\n\n
        Alert *THE DECRYPTION OPTION ONLY WORKS WITH FILES ENCRYPTED BY THIS TOOL*""")
        dtInfo.pack()


def mainWindow():
    menuBar()

    HEIGHT = 500
    WIDTH = 700

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    entryLabel = tk.Label(root, text='Enter text or load a text file:')
    entryLabel.place(x=50, y=60)

    fileLabel = tk.Label(root, text='File:')
    fileLabel.place(x=50, y=80)

    global fileEntry
    fileEntry = tk.Entry(root)
    fileEntry.place(x=80, y=78)

    fileButton = tk.Button(root, text="Insert", command=insertFile)
    fileButton.place(x=210, y=70)

    optionLabel = tk.Label(root, text="Cipher Options:")
    optionLabel.place(x=275, y=78)

    option = tk.StringVar()
    option.set("Choose")

    dropMenu = tk.OptionMenu(root, option, "Morse Code", "Double Transposition")
    dropMenu.place(x=370, y=70)

    optionButton = tk.Button(root, text="Select", command=lambda: cipherWindows(option.get()))
    optionButton.place(x=530, y=72)

    global executeText
    executeText = tkScroll.ScrolledText(root, undo=True)
    executeText.place(x=50, y=100, height=150, width=600)

    global answerText
    answerText = tkScroll.ScrolledText(root, undo=True)
    answerText.place(x=50, y=325, height=150, width=600)

    encryptButton = tk.Button(root, text="Encrypt", command=lambda: encryptText(option.get()))
    encryptButton.place(x=295, y=260)

    decryptButton = tk.Button(root, text="Decrypt", command=lambda: decryptText(option.get()))
    decryptButton.place(x=355, y=260)


def cipherWindows(option):
    tempFrame = tk.Frame(root, height=70, width=250)
    tempFrame.place(x=49, y=255)

    key1Label = tk.Label(tempFrame, text='Key 1:')
    global key1Entry
    key1Entry = tk.Entry(tempFrame)

    key2Label = tk.Label(tempFrame, text='Key 2:')
    global key2Entry
    key2Entry = tk.Entry(tempFrame)


    if option == "Double Transposition":
        key1Label.place(x=0, y=0)
        key1Entry.place(x=40, y=0)

        key2Label.place(x=0, y=20)
        key2Entry.place(x=40, y=20)

    else:
        tempFrame.destroy


def encryptText(choice):
    aText = executeText.get("1.0", "end")
    aText = aText[:-1]

    if choice == "Double Transposition" and aText != "":
        encryptedText = DoubleTranspositionCipher(aText, key1Entry.get(), key2Entry.get())

    elif choice == "Morse Code" and aText != "":
        encryptedText = MorseCodeCipher(aText)

    answerText.delete("1.0", "end")
    answerText.insert("1.0", encryptedText.encrypt())


def decryptText(choice):
    aText = executeText.get("1.0", "end")
    aText = aText[:-1]

    if choice == "Double Transposition" and aText != "":
        decryptedText = DoubleTranspositionCipher(aText, key1Entry.get(), key2Entry.get())

    elif choice == "Morse Code" and aText != "":
        decryptedText = MorseCodeCipher(aText)

    answerText.delete("1.0", "end")
    answerText.insert("1.0", decryptedText.decrypt())


def main():
    mainWindow()
    root.mainloop()


main()
