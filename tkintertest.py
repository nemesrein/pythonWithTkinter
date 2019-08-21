from tkinter import *
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame,text="Button 1", fg="red")
button2 = Button(topFrame,text="Button 2", fg="orange")
button3 = Button(bottomFrame,text="Button 3", fg="blue")
button4 = Button(bottomFrame,text="Button 4", fg="green")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=BOTTOM)
button4.pack(side=TOP)

root.mainloop()