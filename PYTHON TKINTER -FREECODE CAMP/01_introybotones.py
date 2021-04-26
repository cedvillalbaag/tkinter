
#Importar librería
from tkinter import *

#Crear Ventana
root = Tk()

#Crear etiqueta en ventana
myLabel = Label(root, text= "Crear Botones")

#Mostrar en pantalla
myLabel.pack()

#################################################################################################
#Botones

#Para que los botones tengan funcionalidad se debe crear las funciones asociadas a cada uno de ellos.

def myClick():
    myLabel = Label(root, text="Look, I clicked a bottom!")
    myLabel.pack()

#--------

#Crear Boton
myButton = Button(root, text="ClickMe!")
myButton.pack()

#Crear Boton Deshabilitado
myButton2 = Button(root, text="ClickMe!", state=DISABLED)
myButton2.pack()

#Crear Boton - cambio de tamaño
myButton3 = Button(root, text="ClickMe!", pady = 50)
myButton3.pack()




#Crear boton que genere una accion asociado a una función
myButton4 = Button(root,text="ClickMe!", command= myClick)
myButton4.pack()


#Crear boton agregando color diferente al texto
myButton5 = Button(root,text="ClickMe!", command= myClick, fg="blue")
myButton5.pack()

#Crear boton agregando color diferente al fondo del boton
myButton6 = Button(root,text="ClickMe!", command= myClick, fg="white", bg="red")
myButton6.pack()


#Crear boton agregando color diferente al fondo del boton usando codigo de colores
myButton6 = Button(root,text="ClickMe!", command= myClick, fg="white", bg="#FF5733")
myButton6.pack()

#Crear boton agregando color diferente al fondo del boton usando codigo de colores
myButton6 = Button(root,text="ClickMe!", command= myClick, fg="white", bg="#1C9D47", width=50)
myButton6.pack()


##########################################################################################
#BucleInifinito - Siempre debe ir al final
root.mainloop()