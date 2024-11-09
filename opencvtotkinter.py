import cv2
from PIL import Image, ImageTk
import tkinter as tk

window = tk.Tk()
window.title('Opencv to tkinter')


image_frame = tk.Frame(window, width=600, height=500)
image_frame.grid(row=1, column=0 , padx=10, pady=2)

label = tk.Label(image_frame)
label.grid(row=0, column=0)



cap = cv2.VideoCapture(0)

def show_frames():
    global frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    label.image = imgtk
    label.config(image=imgtk)
    label.after(20, show_frames)

def save_img():
    cv2.imwrite('img.png', cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

butt = tk.Button(image_frame, text='Capture', command=save_img)
butt.grid(row=0, column=0)


show_frames()

window.mainloop()
