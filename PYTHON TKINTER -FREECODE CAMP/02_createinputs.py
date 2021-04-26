#Importar librería
from tkinter import *

#Crear Ventana
root = Tk()

#Crear etiqueta en ventana
myLabel = Label(root, text= "Crear Inputs")

#Mostrar en pantalla
myLabel.pack()

#############################
#Crear Inputs

#Crear Input , sin parametros
e = Entry(root)
e.pack()


#Agregando parámetros
#Crear Input , definiendo el ancho
e1 = Entry(root, width= 50)
e1.pack()

#Crear Input , definiendo el ancho y agregando color de fondo
e2 = Entry(root, width= 50, bg= "#6689B7")
e2.pack()

#Crear Input , definiendo el ancho, agregando color de fondo y cambiando el color de texto
e3 = Entry(root, width= 50, bg= "#6689B7", fg="#DB900E")
e3.pack()

#Crear Input , cambiar el borde
e4 = Entry(root, width= 50, borderwidth=5)
e4.pack()


#Crear Input , agregar un texto por defecto
e5 = Entry(root, width= 50, borderwidth=5)
e5.pack()
e5.insert(0,"Insert your Name")


#QUE PODEMOS HACER CON LOS INPUTS

#get function





#################################################################################################
#Botones

#Para que los botones tengan funcionalidad se debe crear las funciones asociadas a cada uno de ellos.

def myClick():
    #es posible definir paametro texto a traves de una variable
    #Hello = "Hello " + e.get()
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

#--------

#Crear Boton
myButton = Button(root, text="Enter your Name!", command=myClick)
myButton.pack()


##########################################################################################
#BucleInifinito - Siempre debe ir al final
root.mainloop()