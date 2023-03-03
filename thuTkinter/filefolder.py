from tkinter import filedialog
from tkinter import filedialog
from os import path
file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
dir = filedialog.askdirectory()
file = filedialog.askopenfilename(initialdir= path.dirname(__file__))