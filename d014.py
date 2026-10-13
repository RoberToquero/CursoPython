# importaciones
from tkinter import *
# MANEJO DE RUTAS 
from os import * # Importa el Sistema Operativo 
from PIL import ImageTk, ImageColor, Image # módulo Pillow para imágenes pero solo 3 cosas para no sobrecargar memoria
# Carga de directorios de forma dinámica con __file__
carpeta_principal = path.dirname(__file__) # Con esta variable obtiene la carpeta raíz de donde está el programa 
# print(carpeta_principal) 

# Llamando a la carpeta imágenes con un join
carpeta_imagenes = path.join(carpeta_principal, 'imagenes')
# print(carpeta_imagenes)
carpeta_paisajes = path.join(carpeta_imagenes, 'paisajes')

# Creación de la ventana principal
root = Tk()
# Título de la ventana
root.title('Ejercicio de carga de imágenes')
# Tamaño y posición
root.geometry('600x600+900+50') #Tamaño de ventana y coordenadas en X e Y
#Icono de la ventana
root.iconbitmap(path.join(carpeta_imagenes,'python_icon.ico'))

# CARGA DE IMAGEN
bosque = ImageTk.PhotoImage(Image.open(path.join(carpeta_paisajes, 'paisaje1.jpg')).resize((500,350)))
etiqueta = Label(image=bosque)
etiqueta.pack()

#Bucle de ejecución
root.mainloop()