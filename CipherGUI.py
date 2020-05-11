# CipherGUI
import tkinter as tk
from tkinter import filedialog
from DoubleTranspositionCipher import *
from MorseCodeCipher import *

global root
root = tk.Tk()


def menuBar():
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    fileMenu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Open", command=selectFile)


def selectFile():
    fileName = tk.filedialog.askopenfilename(title="Select a file", filetypes=[("txt Files", "*.txt")])
    fileEntry.delete(0, "end")
    fileEntry.insert(0, fileName)


def insertFile():
    aFile = open(fileEntry.get())
    fileText = aFile.read()
    executeText.delete("1.0", "end")
    executeText.insert("1.0", fileText)

    aFile.close()


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

    global option
    option = tk.StringVar()
    option.set("Choose")

    dropMenu = tk.OptionMenu(root, option, "Morse Code", "Double Transposition")
    dropMenu.place(x=370, y=70)

    optionButton = tk.Button(root, text="Select", command=cipherWindows)
    optionButton.place(x=530, y=72)

    global executeText
    executeText = tk.Text(root)
    executeText.place(x=50, y=100, height=150, width=600)
    scroll_1 = tk.Scrollbar(executeText)
    scroll_1.pack(side='right', fill='y')
    scroll_1.config(command=executeText.yview)
    executeText.config(yscrollcommand=scroll_1.set)

    encryptButton = tk.Button(root, text="Encrypt", command=encryptText)
    encryptButton.place(x=295, y=260)

    decryptButton = tk.Button(root, text="Decrypt", command=decryptText)
    decryptButton.place(x=355, y=260)

    global answerText
    answerText = tk.Text(root)
    answerText.place(x=50, y=325, height=150, width=600)
    scroll_2 = tk.Scrollbar(answerText)
    scroll_2.pack(side='right', fill='y')
    scroll_2.config(command=answerText.yview)
    answerText.config(yscrollcommand=scroll_2.set)


# def executeAction():

# if executeText != "":

def cipherWindows():
    anOption = option.get()

    tempFrame = tk.Frame(root, height=70, width=250)
    tempFrame.place(x=49, y=255)

    if anOption == "Double Transposition":
        key1Label = tk.Label(tempFrame, text='Key 1:')
        key1Label.place(x=0, y=0)
        global key1Entry
        key1Entry = tk.Entry(tempFrame)
        key1Entry.place(x=40, y=0)

        key2Label = tk.Label(tempFrame, text='Key 2:')
        key2Label.place(x=0, y=20)
        global key2Entry
        key2Entry = tk.Entry(tempFrame)
        key2Entry.place(x=40, y=20)

    else:
        tempFrame.destroy


def encryptText():
    aText = executeText.get("1.0", "end")
    aText = aText[:-1]

    if option.get() == "Double Transposition" and aText != "":
        encryptedText = DoubleTranspositionCipher(aText, key1Entry.get(), key2Entry.get())

    elif option.get() == "Morse Code" and aText != "":
        encryptedText = MorseCodeCipher(aText)

    answerText.delete("1.0", "end")
    answerText.insert("1.0", encryptedText.encrypt())


def decryptText():
    aText = executeText.get("1.0", "end")
    aText = aText[:-1]

    if option.get() == "Double Transposition" and aText != "":
        decryptedText = DoubleTranspositionCipher(aText, key1Entry.get(), key2Entry.get())

    elif option.get() == "Morse Code" and aText != "":
        decryptedText = MorseCodeCipher(aText)

    answerText.delete("1.0", "end")
    answerText.insert("1.0", decryptedText.decrypt())


def main():
    mainWindow()
    root.mainloop()


main()
