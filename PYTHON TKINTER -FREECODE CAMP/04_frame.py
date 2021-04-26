#FRAMES
#Importar librería
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Code")
root.iconbitmap('a.ico')

frame = LabelFrame(root,text="This is my Frame......", padx=15, pady=15)
frame.pack(padx=100, pady=100 )

b = Button(frame, text="Dont click here!")
b2 = Button(frame, text="Dont click here!")
b.grid(row=0, column=0)
b2.grid(row=0, column=1)


#Bucle infinito
root.mainloop()