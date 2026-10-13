# importaciones
from tkinter import * 

# Creación de la ventana principal
root = Tk()

# Título de la ventana
root.title('Colores en Tkinter')
# Marcos para dividir el contenido
# marco_1 = LabelFrame(root,
#                    text='Entrada de datos',
#                    width= 300,
#                    height= 300
#                    )
# marco_1.pack(padx=25, pady= 15)

# marco_2 = LabelFrame(root,
#                    text='Enviar',
#                    padx=20,
#                    pady=20
#                    )
# marco_2.pack(padx=5, pady=15)

# marco_3 = LabelFrame(root,
#                    text='Resultado',
#                    padx=20,
#                    pady=20
#                    )
# marco_3.pack(padx=5, pady=15)

# # Entrada de datos
# entrada = Entry(marco_1,
#                 background='springgreen',
#                 border= 3,
#                 foreground= 'red',
#                 width= 30,
#                 )
# entrada.pack()
# entrada.insert(0, 'Escriba su nombre...') 
# entrada.bind('<Button-1>', lambda x : entrada.delete(0, END)) # Borrar el usuario al pulsar

# # Función para el botón
# def enviar():
#     nombre = entrada.get()
#     Label(marco_3,
#           text=f'Hola {nombre}',
#           background='skyblue',
#           width=27
#           ).pack()
#     entrada.delete(0, END)
#     entrada.insert(0, 'Escriba su nombre...')
    
# # Botón de enviar
# boton = Button(marco_2,
#                text='Enviar',
#                command= enviar,
#                background='deepskyblue',
#                foreground='gray98',
#                border=3,
#                width=26
#                )
# boton.pack()

# EJERCICIOS

marco_1 = LabelFrame(root, width=100, height=100, background='tomato', border=0)
marco_1.grid(row=0, column=0)

marco_2 = LabelFrame(root, width=100, height=100, background='skyblue', border=0)
marco_2.grid(row=0, column=1)

marco_3 = LabelFrame(root, width=100, height=100, background='tomato', border=0)
marco_3.grid(row=0, column=2)

marco_4 = LabelFrame(root, width=100, height=100, background='skyblue', border=0)
marco_4.grid(row=1, column=0)

marco_5 = LabelFrame(root, width=100, height=100, background='tomato', border=0)
marco_5.grid(row=1, column=1)

marco_6 = LabelFrame(root, width=100, height=100, background='skyblue', border=0)
marco_6.grid(row=1, column=2)

marco_7 = LabelFrame(root, width=100, height=100, background='tomato', border=0)
marco_7.grid(row=2, column=0)

marco_8 = LabelFrame(root, width=100, height=100, background='skyblue', border=0)
marco_8.grid(row=2, column=1)

marco_9 = LabelFrame(root, width=100, height=100, background='tomato', border=0)
marco_9.grid(row=2, column=2)


# Bucle para mantener la ventana en ejecución
root.mainloop() 