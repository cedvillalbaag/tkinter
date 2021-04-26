#IMAGENES ICONOS Y BOTON DE SALIDA


#Importar libería
from tkinter import *
from PIL import ImageTk, Image



##########################################################################
root = Tk()
root.title("Code")


###########################################################################################
#CAMBIAR ICONO DE VENTANA
root.iconbitmap('a.ico')

#########################################################################################
#EXIT BUTTON

button_quit = Button(root, text= "Exit Program", command=root.quit) 
button_quit.pack()

########################################################################################
#USING IMAGES

#es necesario instalar la librería Pillow
#pip freeze podemos ver que librerias tenemos instaladas en python


my_img = ImageTk.PhotoImage(Image.open('img1.jpg'))

my_label = Label(image=my_img )
my_label.pack()
#-------------------------------------------------------------------------------------------
#Bucle infinito
root.mainloop()