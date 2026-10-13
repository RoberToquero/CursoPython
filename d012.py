# importaciones
from tkinter import * 

# Creación de la ventana principal
root = Tk()

# Creación de la etiqueta
mensaje = Label(root, text='Curso de Tkinter')

#Entrada de texto
entrada = Entry(root)
entrada.insert(0, 'Escriba su nombre...') #Sirve para que haya un texto predefinido en ese espacio
entrada.bind('<Button-1>', lambda x : entrada.delete(0, END)) # Sirve para que al pulsar con el ratón el texto predefinido se borre
# Necesito la función lambda para desencadenar el evento, porque si no lo borra instantáneamente
entrada.pack()

#Evento para el botón
def pulsar_boton():
    nombre = entrada.get()
    Label(root, text=f'{nombre}').pack()

def crear_etiqueta(numero_boton):
    etiqueta = Label(root, text=f'Botón {numero_boton} pulsado.')
    etiqueta.pack()

#Botón
Button(root, text='Enviar',command=pulsar_boton).pack() #La función pulsar_boton sin parentesis para un evento
Button(root, text='Numero1', command=lambda: crear_etiqueta(1)).pack()
Button(root, text='Numero2', command=lambda: crear_etiqueta(2)).pack()
Button(root, text='Numero3', command=lambda: crear_etiqueta(3)).pack()
Button(root, text='Numero4', command=lambda: crear_etiqueta(4)).pack()


# Bucle para mantener la ventana en ejecución
root.mainloop() 