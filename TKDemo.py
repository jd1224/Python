from tkinter import *
from tkinter import ttk

root = Tk()

for i in range(0,10):
	framei = Frame(width=768, height=576, bg="", colormap="new")

	label_red = Label(framei, text="Red", fg='white', bg='red')
	label_blue = Label(framei, text="Blue", fg='white', bg='blue')
	label_green = Label(framei, text="Green", fg='white', bg='green')
	label_yellow = Label(framei, text="Yellow", fg='black', bg='yellow')


	label_red.pack(fill=X, pady=0.5)
	label_blue.pack(fill=X,pady=0.5)
	label_green.pack(fill=X,pady=0.5)
	label_yellow.pack(fill=X,pady=0.5)

	framei.pack(side=LEFT,fill=X, padx=0.5)

root.mainloop()
