import tkinter as tk
    
import random

mylist = ["paint with Bob Ross", "picnic", "massage", "charcuterie board", "movie night", "blindfolded dinner"]


counter = 0 
def counter_label(label):
  counter = 0
  

def write_slogan():
    print(random.choice(mylist))

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)

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
