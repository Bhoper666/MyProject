from tkinter import *


def button_press():
    change.set(not change.get())
    if not change.get():
        lbl.pack()
    if change.get():
        lbl.pack_forget()

root = Tk()
root.title('My first window ^_^')
root.geometry('300x200+500+300')

change = BooleanVar()
change.set(True)

lbl = Label(text='Hello, world!')
btn = Button(text='Change', command=button_press)
btn.pack()

mainloop()
