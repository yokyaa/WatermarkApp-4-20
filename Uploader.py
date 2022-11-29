from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw,Image,ImageFont


class Uploader:
    def __init__(self):
        self.myimg = None
        self.filename = None
        self.button = Button(text="open", command=self.image,font="verdana")
        self.button.grid()
        self.label=Label()
        self.label.grid()
        self.entry = Entry(font="verdana")
        self.entry.grid()

    def upload(self):
        self.filename = filedialog.askopenfilename(title="open")
        return self.filename

    def image(self):
        self.myimg = ImageTk.PhotoImage(Image.open(self.upload()))
        self.label.config(image=self.myimg)
        return self.myimg
    def draw(self):
        image = Image.open(self.filename)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 30)
        length = len(self.entry.get())
        if length < 4:
            pos = length * 25
        else:
            pos = length * 18
        draw.text((image.getbbox()[2]-pos, image.getbbox()[3]-45), text=self.entry.get(),font=font)
        image.save("images/a.png")
        self.myimg=ImageTk.PhotoImage(Image.open("images/a.png"))
        self.label.config(image=self.myimg)




