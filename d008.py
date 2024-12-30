# importaciones
from tkinter import * # Del módulo tkinter importalo todo

# Creación de la ventana principal
root = Tk()

# Creación de la etiqueta
mensaje = Label(root, text='Mi primer programa con Tkinter')

# Muestro la etiqueta
mensaje.pack()
# Bucle para mantener la ventana en ejecución
root.mainloop() 