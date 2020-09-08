from tkinter import *

root = Tk()
root.title("MAIN")
root.geometry("300x400")
root.iconbitmap("logo.ico")
root.configure(bg="#000000")


b = 0
new = None

def create():

    global b
    global new

    if(b == 0):

        new = Toplevel()
        new.title("second")
        new.iconbitmap("i.ico")
        new.geometry("300x300")
        b = 1





    else:
        if new.winfo_exists():
            b = 1

        else:

            new = Toplevel()
            new.title("second")
            new.iconbitmap("i.ico")
            new.geometry("300x300")
            



butt = Button(root, text="ADD", font="android 25", padx=30, pady=20, command=create)
butt.pack(pady=40)



mainloop()