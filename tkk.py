import Tkinter as tk
from Tkinter  import Text
import os 
root=tk.Tk()
canvas=tk.Canvas(root, height=700,width=700, bg="#263D42")
canvas.pack()
frame=tk.Frame(root, bg="white")
frame.place(relwidth=.8,relheight=.8, relx=.1, rely=.1)
openFile=tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42")
openFile.pack()
runapp=tk.Button(root, text="run app", padx=10, pady=5, fg="white", bg="#263D42")
runapp.pack()
root.mainloop()