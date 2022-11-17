from tkinter import *

import matplotlib.pyplot as plt

root = Tk()
root.geometry("500x500")
root.title("Stonkinator")


rules = Label(root, text = "The amount of values the x and y axes possess must be the same")
rules.pack(pady = 10)

label1 = Label(root, text = "X axis")
label1.pack(pady = 10)

axis1 = Entry(root)  
axis1.pack(pady = 10)

label2 = Label(root, text = "Y axis")
label2.pack(pady = 10)

axis2 = Entry(root)
axis2.pack(pady = 10)

global lis1
global lis2
lis1 = []
lis2 = []

def add():
  
    x = axis1.get()
    y = axis2.get()
    lis1.append(x)
    lis2.append(y)
    print(str(lis1),str(lis2))
    

def plot1():
    plt.plot(lis1, lis2)
    plt.show()

btn = Button(root, text = "plot",command=plot1)
btn.pack(pady = 10)

add1 = Button(root, text = "Add", command = add)
add1.pack(pady = 10)


root.mainloop()