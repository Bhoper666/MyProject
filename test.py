import cv2
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('My first window ^_^')
root.geometry('1280x720')

cap = cv2.VideoCapture(0)
label = Label(root)
label.pack()

def show_frames():
    global frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    label.image = imgtk
    label.config(image=imgtk)
    label.after(20, show_frames)

show_frames()
root.mainloop()
