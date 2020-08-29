import tkinter as tk
from tkinter import filedialog, Text
import tkinter.font as font
import os

root=tk.Tk()
canvas=tk.Canvas(root,height=400,width=300,bg=('red'))
canvas.pack()

helv36 = font.Font(family='Helvetica', size=25)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 5) .place(x=15, y=350)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width =5 ) .place(x=125, y=350)
btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 5) .place(x=180, y=236)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=15, y=236)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=70, y=236)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=125, y=236)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=15, y=132)
btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=70, y=132)
btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=125, y=132)
btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=180, y=132)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=15, y=188)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=70, y=188)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=125, y=188)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=180, y=188)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=180, y=80)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=15, y=80)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=70, y=80)

btn0=tk.Button(canvas,text="0",font=helv36,bg='black',fg="white",height = 1, width = 2) .place(x=125, y=80)

w = tk.Label(root, text="Hello, world!",height=3,width=30,bg='white',fg='black')
w=w.place(x=15, y=10)


root.mainloop()