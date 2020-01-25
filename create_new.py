from tkinter import *
from PIL import  ImageTk, Image

root = Tk()
root.title("Learn to code at gowebkit.com")
root.geometry("600x300")
root.iconbitmap("c:/gui/gowebkit.ico")




def open():
    global  my_img
    top = Toplevel()
    top.title("Calculator")
    top.geometry("1000x500")
    top.iconbitmap("c:/gui/gowebkit.ico")
    my_img = ImageTk.PhotoImage(Image.open("images/aspen.png"))
    my_label = Label(top, image=my_img)
    my_label.pack()
    btn_close = Button(top, text="Close", command=top.destroy)
    btn_close.pack()

btn = Button(root, text="Open Second Window", command=open).pack()


mainloop()
