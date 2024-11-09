from tkinter import *

def buttonpress():
    root.config(bg='green')
    root.title = 'Новий заголовок'
    root.geometry('640x480+200+200')
    lbl.config(text='Новий текст',
               fg='blue',
               bg='brown',
               font='Arial 28 bold italic underline'
    )

root = Tk()
root.title('Тестова програма')
root.geometry('300x300+800+200')

lbl = Label(
    text='Тестовий напис',
    font='Arial 20 bold',
    fg='#ff0000'
)
lbl.pack(pady=20)

btn = Button(
    text='OK',
    width=10,
    bg='yellow',
    fg='red',
    command=buttonpress
)

btn.place(x=50, y=50)


root.mainloop()
