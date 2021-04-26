#*********************Image Viewer App**********************************



#Importar librería
from tkinter import *
from PIL import ImageTk, Image
 

root = Tk()
root.title("Code")


###########################################################################################
#CAMBIAR ICONO DE VENTANA
root.iconbitmap('a.ico')



########################################################################################
#USING IMAGES

#es necesario instalar la librería Pillow
#pip freeze podemos ver que librerias tenemos instaladas en python


my_img1 = ImageTk.PhotoImage(Image.open('img1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('img2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('img3.jpg'))

image_list = [my_img1, my_img2,my_img3]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=3, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1 )
my_label.grid(row=0, column=0, columnspan=3)



#########################################
#DEFINICION DE FUNCIONES

def forward(image_number):
    global my_label
    global button_forward
    global button_back


    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    
    button_forward = Button(root,text=">>", command= lambda: forward(image_number + 1))
    button_back = Button(root,text="<<", command= lambda: forward(image_number-1))

    if image_number == 3:
        button_forward = Button(root, text=">>", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column= 0)
    button_forward.grid(row=1, column=2 )

#Agregar la actualizacion de numero de foto al utilizar boton forward
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=3, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back
   
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    
    button_forward = Button(root,text=">>", command= lambda: forward(image_number + 1))
    button_back = Button(root,text="<<", command= lambda: forward(image_number-1))

    if image_number == 0:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column= 0)
    button_forward.grid(row=1, column=2 )

    #Agregar la actualizacion de numero de foto al utilizar boton backward
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=3, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


###################################################################################
#DEFINICION DE BOTONES
#Definimos Botón Atrás
button_back = Button(root,text="<<", command= back, state=DISABLED)

#Definimos Botón Adelante
button_forward = Button(root,text=">>", command= lambda: forward(2))

#Definimos Botón Exit
button_exit = Button(root, text= "Exit Program", command=root.quit) 

#COLOCAR EN PANTALLA BOTONES

button_back.grid(row=1, column= 0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#Bucle infinito
root.mainloop()