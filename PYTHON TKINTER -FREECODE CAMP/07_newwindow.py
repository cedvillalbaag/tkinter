#NEW WINDOW IN TKINTER



#Importar librería
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Code")
root.iconbitmap('a.ico')

top1 =Toplevel()
#Definir funcion para accion open

#Nota: la imagen debe ser asignada a una variable global para que pueda funcionar
def open():
    global my_img
    top1 = Toplevel()
    top1.title("Titulo de Segunda Ventana")
    my_img = ImageTk.PhotoImage(Image.open("img2.jpg"))
    my_label = Label (top1, image= my_img).pack()
    btn2= Button(top1, text="Close Window", command= top.destroy).pack()




#Crear boton
btn = Button(top1, text="Open Second Window", command = open). pack()


#Ejemplo de Crear ventana nueva
top = Toplevel()
top.title("Titulo de Segunda Ventana")
#Colocar etiqueta en la nueva ventana
#lbl = Label(top, text= "Hola Mundo").pack()


#Colocar imagen en la ventana nueva
my_img = ImageTk.PhotoImage(Image.open("img1.jpg"))
my_label = Label (top, image= my_img).pack()

#Bucle infinito
root.mainloop()