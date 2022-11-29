from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
from Uploader import *

window = Tk()
uploader = Uploader()
image = Image.open("hopper.jpg")

window.title("Watermark")
window.minsize(height=500, width=500)

button = Button(font="verdana",text="watermark", command=uploader.draw)
button.grid(column=0,row=3)

window.mainloop()
