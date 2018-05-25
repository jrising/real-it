from Tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk

tk = Tk()
tk.title = "Real-It"
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

cam = cv2.VideoCapture(0)

class Eyeball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.panel = Label(self.canvas)
        self.image = None

    def draw(self):
        s, img = cam.read() # captures image

        #Rearrang the color channel
        b,g,r = cv2.split(img)
        img = cv2.merge((r,g,b))

        # Convert the Image object into a TkPhoto object
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im) 

        # Put it in the display window
        self.panel.configure(image=imgtk)
        self.image = imgtk
        self.panel.pack()
        self.canvas.after(1, self.draw)

eyeball = Eyeball(canvas)
eyeball.draw()
tk.mainloop()
