from os import * 
from tkinter import *
from PIL import ImageTk, Image 

ruta = path.dirname(__file__)
carpeta_imagenes = path.join(ruta, 'imagenes')
carpeta_motos = path.join(carpeta_imagenes, 'motos')


'''
Creación de dos entradas por la consola que pida el usuario y la contraseña. 
Ambas cosas se deben pedir dos veces, con el fin de comprobar que no se haya equivocado. 
Si se equivoca que vuelva a realizar el proceso
'''


while True:
    nuevo_usuario = input('Introduzca un nombre para el nuevo usuario. \n')
    nueva_contrasena = input('Introduce una contraseña para el nuevo usuario. \n')
    repite_usuario = input('Introduzca el usuario de nuevo. \n')
    repite_contrasena = input('Introduzca la contraseña de nuevo. \n')  
    if nuevo_usuario == repite_usuario and nueva_contrasena == repite_contrasena:
        usuario_creado = (nuevo_usuario, nueva_contrasena)
        print('Usuario creado con éxito.\n')
        break
    else: 
        print('Los datos no coinciden vuelva a intentarlo.')


# Creación de la ventana principal
root = Tk()
# Título de la ventana
root.title('American riders')
# Icono de la ventana
root.iconbitmap(path.join(carpeta_imagenes,'python_icon.ico'))
# CARGA DE IMAGEN
lista_imagenes = ['moto1.jpg', 'moto2.jpg', 'moto3.png', 'moto4.jpg']
fotos = []  # guarda las imágenes para que no se borren de memoria

for i, nombre in enumerate(lista_imagenes):
    imagen = Image.open(path.join(carpeta_motos, nombre)).resize((400, 250))
    foto = ImageTk.PhotoImage(imagen)
    fotos.append(foto)

    etiqueta = Label(root, image=foto)
    etiqueta.grid(row=i // 2, column=i % 2)  # 2 columnas, las filas se calculan solas

# Campos de texto (centrados bajo las imágenes)
Label(root, text='Usuario').grid(row=2, column=0, columnspan=2, pady=(10, 0))
usuario = Entry(root)
usuario.insert(0, 'Ej: Laura') # Ejemplo
usuario.bind('<Button-1>', lambda x : usuario.delete(0, END)) # Borrar el usuario al pulsar
usuario.grid(row=3, column=0, columnspan=2)

Label(root, text='Contraseña').grid(row=4, column=0, columnspan=2, pady=(10, 0))
contrasena = Entry(root, show='*')  # show='*' oculta lo que escribes
contrasena.insert(0,'*'*7)
contrasena.bind('<Button-1>', lambda x : contrasena.delete(0, END))
contrasena.grid(row=5, column=0, columnspan=2, pady=(0, 10))

# Función para validar el login
def validar():
    obtener_usuario = usuario.get()
    obtener_contrasena = contrasena.get()
    if obtener_usuario != usuario_creado[0] or obtener_contrasena != usuario_creado[1]:
        Label(text='Usuario o contraseña incorrectos.').grid(row=9, column=0, columnspan=2, pady=10)
    else:
        Label(text=f'Hola, {usuario_creado[0]}. Espere unos instantes...').grid(row=11, column=0, columnspan=2, pady=10)
# Botón 
Button(text='Entrar', command= validar).grid(row=7, column=0, columnspan=2)

# Bucle de ejecución
root.mainloop()

