#Importar librería
from tkinter import *

root = Tk()
root.title("Code")
root.iconbitmap('a.ico')



#Asegurar el valor de la variable como Integer
r = IntVar()
# Fijar Un valor de ejemplo
# r.set("2")

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")]


pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()
#########################################

#Definir funcion para que al presionar boton se muestre el resultado seleccionado de los botones
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


#Radiobutton(root, text="Option1", variable=r, value=1, command= lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option2", variable=r, value=2, command= lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option3", variable=r, value=3, command= lambda: clicked(r.get())).pack()


myLabel = Label(root, text = r.get())
myLabel.pack()

myButton = Button(root, text="Click Me!!", command= lambda: clicked(pizza.get())).pack()


#Bucle infinito
root.mainloop()