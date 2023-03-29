from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=200)
w.pack()

x1=50
y1=50

x2=100
y2=100

dim=50

top = -1
left = -1
right = 1
bottom = 1

tl = w.create_rectangle(x1, y1, x2, y2, fill="yellow")
tr = w.create_rectangle(x1 * 2, y1, x2+dim, y2, fill="red")
bl = w.create_rectangle(x1, y1 + dim, x2, y2 + dim, fill="green")
br = w.create_rectangle(x2, y2, x2 + dim, y2 + dim, fill="black")

def task():
    l = master.after(1000, task)
    w.move(tl,left, top)
    w.move(tr, right, top)
    w.move(bl, left, bottom)
    w.move(br, right, bottom)
    print(l)
    if "after#50" in l:
        master.after_cancel(l)
   

task()

mainloop()