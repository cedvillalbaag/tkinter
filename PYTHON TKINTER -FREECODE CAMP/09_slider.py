#SLIDER

#Importar librerías
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog


#Crear ventanas
root = Tk()
root.title("Code")
root.iconbitmap('a.ico')
root.geometry("1000x600")

#Crear un slider vertical
vertical = Scale(root, from_=0, to= 200)
vertical.pack()


#Crear un slider horizontal
horizontal = Scale(root, from_=0, to= 200, orient=HORIZONTAL)
horizontal.pack()


my_label = Label(root, text=horizontal.get()).pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()

    
my_btn = Button(root, text="Click me!", command= slide).pack()
#Bucle infinito
root.mainloop()