# importaciones
from tkinter import * # Del módulo tkinter importalo todo

# Creación de la ventana principal
root = Tk()

# Título de la ventana
root.title('Curso de Tkinter')

# Tamaño de la ventana
root.geometry('800x600+560+20') #Tamaño de ventana y coordenadas en X e Y

# Creación de las etiquetas
mensaje = Label(root, text='Mi primer programa con Tkinter.')
mensaje2 = Label(root, text='Esta es la segunda etiqueta.')


# Se muestran las etiquetas
mensaje.grid(row=0,column=0) #Con el grid podemos colocar los elementos en diversas filas y columnas
mensaje2.grid(row=1,column=1) #Los grid también pueden aplicarse directamente en la creación de la etiqueta, ahorrando lineas de codigo

# Bucle para mantener la ventana en ejecución
root.mainloop() 