# importaciones
from tkinter import * # Del módulo tkinter importalo todo

# Creación de la ventana principal
root = Tk()

# Título de la ventana
root.title('Curso de Tkinter')

# Tamaño de la ventana
root.geometry('800x600+560+20')

# Creación de las etiquetas
mensaje = Label(root, text='Mi primer programa con Tkinter.')
mensaje2 = Label(root, text='Esta es la segunda etiqueta.')
# Se muestran las etiquetas
mensaje.pack()
mensaje2.pack()

# Bucle para mantener la ventana en ejecución
root.mainloop() 