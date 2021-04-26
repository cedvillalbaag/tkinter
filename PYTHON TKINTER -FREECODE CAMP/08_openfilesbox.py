#OPEN FILES DIALOG BOX

# Plantilla Basica de Tkinter

#Importar librería
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Code")
root.iconbitmap('a.ico')

#PNG Files "*.png"
#all files "*.*"
#root.filename = filedialog.askopenfilename(initialdir= "/Users/ASUS/Desktop", title= "Select a File", filetypes=(("JPG files","*.jpg"),("Word Files","*.docx")))

#Visualizar que retorna la variable - se apreciara la ruta del archivo
#my_label = Label(root, text=root.filename).pack()

#my_image = ImageTk.PhotoImage(Image.open(root.filename))
#my_image_label = Label(image=my_image).pack()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir= "/Users/ASUS/Desktop", title= "Select a File", filetypes=(("JPG files","*.jpg"),("Word Files","*.docx")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
my_btn = Button(root, text="OpenFile", command=open).pack()




#Bucle infinito
root.mainloop()