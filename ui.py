import tkinter as tk


def button_press():
    window.config(bg='#05fcec')
def choice():
    if check.get() == 1:
        l_1.config(text='I pressed Checkbutton 1')
    elif check2.get() == 1:
        l_1.config(text='I pressed checkbutton 2')
    elif check3.get() == 1:
        l_1.config(text='I pressed the checkbutton 3')

'''root = tk.Tk()
root.title('My first window ^_^')
root.geometry('300x200+500+300')'''

window = tk.Tk()
window.title('My second window ^_^')
window.geometry('640x480')


l_1 = tk.Label(
    window,
    text='Hello world!',
    font='Arial 16 bold italic underline',
)
l_1.pack(pady=10)


b_1= tk.Button(
    window,
    text='Ok',
    command=button_press
)
b_1.pack()

check = tk.BooleanVar()
check2 = tk.BooleanVar()
check3 = tk.BooleanVar()


c_1 = tk.Checkbutton(window, text='Option 1', variable=check, onvalue=1, offvalue=0, command=choice)
c_2 = tk.Checkbutton(window, text='Option 2', variable=check2, onvalue=1, offvalue=0, command=choice)
c_3 = tk.Checkbutton(window, text='Option 3', variable=check3, onvalue=1, offvalue=0, command=choice)
c_1.pack(pady=10)
c_2.pack(pady=10)
c_3.pack(pady=10)

tk.mainloop()