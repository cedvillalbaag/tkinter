#Importar librería
from tkinter import *

#Crear Ventana
root = Tk()
root.title("Simple Calculator")

###################################################################################
#Crear entry input
e = Entry(root, width=35, borderwidth= 5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)




#################################################################################################
#Botones

#Para que los botones tengan funcionalidad se debe crear las funciones asociadas a cada uno de ellos.
#Funciones

def button_click(number):
    #e.delete(0,END)
    #guarda el valor actual del input en una variable
    current = e.get()
    #elimina el valor del input
    e.delete(0,END)
    #permite agregar nuevos numeros
    e.insert(0, str(current) + str(number))
    return

def button_clear():
    #elimina el valor del input
    e.delete(0, END)
    return

def button_add():
    #elimina el valor del input
    first_number = e.get()
    global f_num
    global math
    math= "addition"
    f_num = int(first_number)
    e.delete(0, END)
      

def button_subtract():
    #elimina el valor del input
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
    


def button_multiply():
    #elimina el valor del input
    first_number = e.get()
    global f_num
    global math
    math= "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
    

def button_divide():
    #elimina el valor del input
    first_number = e.get()
    global f_num
    global math
    math= "division"
    f_num = int(first_number)
    e.delete(0, END)







def button_equal():
    second_number = e.get()
    
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))
    
      
#--------------------------------------------

#Crear Botones
button_1= Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2= Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3= Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4= Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5= Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6= Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7= Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8= Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9= Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0= Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_subtract = Button(root, text="-", padx=41, pady=20, command= button_subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, command= button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command= button_divide)

#Crear Boton Limpiar
button_clear= Button(root, text="Clear", padx=78, pady=20, command=button_clear)

#Crear boton Suma
button_add= Button(root, text="+", padx=39, pady=20, command=button_add)

#Crear boton Igual
button_equal= Button(root, text="=", padx=87, pady=20, command=button_equal)




#####################################################
#Colocar los botones en la pantalla
button_1.grid(row=3 ,  column=0 )
button_2.grid(row=3 ,  column=1 )
button_3.grid(row=3 ,  column=2 )

button_4.grid(row=2 ,  column=0 )
button_5.grid(row=2 ,  column=1 )
button_6.grid(row=2 ,  column=2 )

button_7.grid(row=1 ,  column=0 )
button_8.grid(row=1 ,  column=1 )
button_9.grid(row=1 ,  column=2 )

button_0.grid(row=4 ,  column=0 )
button_clear.grid(row=4 , column=1, columnspan=2 )
button_add.grid(row=5 , column=0 )
button_equal.grid(row=5 , column=1, columnspan=2 )

button_subtract.grid(row=6,  column=0 )
button_multiply.grid(row=6,  column=1 )
button_divide.grid(row=6,  column=2 )



##########################################################################################
#BucleInifinito - Siempre debe ir al final
root.mainloop()
