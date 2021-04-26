#Importar librería
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Code")
root.iconbitmap('a.ico')


#TIPOS DE MENSAJE
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

#Prueba
#def popup():
    #messagebox.showinfo("This is my popup", "Hello world!")


def popup():
    response = messagebox.askyesno("This is my popup", "Hello world!")
    #Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You click yes!!!").pack()
    else:
        Label(root, text="You click No!!!").pack()



#Siempre se debe verificar que devuelve la funcion de acuerdo al tipo de mensaje: 1,0, yes,no, 


Button(root, text="Popup", command= popup).pack()

#Bucle infinito
root.mainloop()