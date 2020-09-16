import tkinter as tk
    
import random

mylist = ["paint", "picnic", "massage", ""]

def write_slogan():
    print(random.choice(mylist))

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Press me for an idea",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
