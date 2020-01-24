from tkinter import *
from PIL import  ImageTk, Image

root = Tk()
root.title("Learn to code at gowebkit.com")
root.geometry("600x300")
root.iconbitmap("c:/gui/gowebkit.ico")

top = Toplevel()
my_img = ImageTk.PhotoImage(Image.open("images/aspen.png"))
my_label = Label(top, image=my_img).pack()

mainloop()