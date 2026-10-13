# importaciones
from tkinter import * # Del módulo tkinter importalo todo

# Creación de la ventana principal
root = Tk()

# Título de la ventana
root.title('Ejercicio con Tkinter')

# Tamaño de la ventana
root.geometry('300x200+560+50') #Tamaño de ventana y coordenadas en X e Y

# Creación de las etiquetas
Label(root, text='Nombre:').grid(row=0,column=0)
Label(root, text='Edad:').grid(row=1,column=0)
#Creación de entradas
entrada = Entry(root) # el grid no va seguido porque si no da error de None en el get
entrada.grid(row=0,column=1)
entrada1 = Entry(root)
entrada1.grid(row=1,column=1)

# Evento para el botón
def pulsar_boton():
    nombre = entrada.get()
    edad = entrada1.get()
    Label(root, text=f'Tu nombre es {nombre} y tu edad es {edad}').grid(row=3, column=1)

# Creación del botón
Button(root, text='Enviar',command=pulsar_boton).grid(row=2, column=1)


# Bucle para mantener la ventana en ejecución
root.mainloop() 