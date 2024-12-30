# # BUCLES
# for i in range(3,12,3):
#     print(f'El valor del bucle es: {i}')

# # Iterar una lista
# colores ={'rojo','azul','verde','amarillo'}
# for color in colores:
#     print(f'-{color}')

# # Bucle while
# x = 1
# while x <= 5:
#     print('Hola crack')
#     x+=1

# #El bucle do-while no existe como tal en python
# # Si queremos que al menos el bucle se ejecute una vez que es para lo que sirve el do while
# # Sería así:
# while True:
#     salida = input('Introduce salir para finalizar \n').lower()
#     if salida == 'salir':
#         break

#EJERCICIOS
for i in range(7,15):
    print(i)
print('\n')
x = 7
while x<=14:
    print(x)
    x+=1

for y in range(0,-5001,-500):
   print(y)
print('\n')
j = 0
while j >= -5000:
    print(j)
    j-=500

lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_numeros.sort()
for lista in lista_numeros:
    if lista == 10:
        continue
    elif lista == 356:
        break
    print(f'El valor del elemento es: {lista}')

"""Proyecto:
       Programa de consola que permita al usuario pedir ingredientes de una pizza
       Condiciones:
       - Añadir un titulo con un print
       - El usuario introducirá el dinero que tiene
       - Crea una lista donde ir añadiendo los ingredientes extra. Pista: Métodos de adición en listas
       - Habrá mínimo tres tipos de pizzas para elegir 
       - Cada pizza tendrá un coste diferente
       - El usuario podrá elegir solo una pizza
       - Una vez elegida la pizza se le informará al usuario del total que lleva por el momento.
       - Se le debe pedir si quiere o no, añadir ingredientes extra (estos harán subir el precio final)
       - Añade al menos 3 ingredientes extra. El usuario podrá elegir uno o varios de estos. No hay límite
       de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y que vuelva a realizar el pedido
       - Las pizzas e ingredientes tendrán sus precios almacenados en variables
       - Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario con el cambio que le queda
       - Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
"""
print('-- PIZZERIA TOP CLASS--')    
dinero = float(input('Hola, indique el dinero que lleva.\n'))
pizzas = ['Margarita', 'Jamón y Queso', 'Cuatro Quesos']
precios = [7.85,9.65,8.95]
ingredientes_extra= ['Extra de Queso', 'Peperoni', 'Champiñones', 'Albahaca']
precios_extra = [1.25,2.50,0.85,0.50]
total = None
compra_realizada = False  # Variable para controlar si se ha realizado una compra válida
while dinero>= 7.85:
    while True:
        print(f'Las pizzas disponibles son: \n1 - {pizzas[0]} - {precios[0]}€\n2 - {pizzas[1]} - {precios[1]}€ \n3 - {pizzas[2]} - {precios[2]}€')
        opcion = int(input('Hola, por favor, seleccione su pizza con un número de opción.\n'))
        match opcion:
            case 1:
                print(f'Ha elegido la pizza {pizzas[0]}\n')
                total = precios[0]
                nombre_pizza = pizzas[0]
            case 2: 
                print(f'Ha elegido la pizza {pizzas[1]}\n')
                total = precios[1]
                nombre_pizza = pizzas[1]
            case 3:
                print(f'Ha elegido la pizza {pizzas[2]}\n')
                total = precios[2]
                nombre_pizza = pizzas[2]
            case _:
                print('Por favor elija un número de pizza válido.\n')
                continue
        if total <= dinero:  # Verifica si tiene suficiente dinero
            dinero -= total  # Descuenta el precio de la pizza del dinero disponible
            print(f'Su total actual es :{total}€.\n')
            print(f'Dinero restante: {round(dinero, 2)}€')

           # INGREDIENTES EXTRA
            while True:
                if dinero<=0: # Si no queda dinero se detiene el proceso
                    print('No tiene dinero suficiente para añadir ingredientes.')
                    break
                extra = int(input('¿Desea añadir algún ingrediente extra?\n1- Sí\n2-No\n'))
                if extra == 1:
                    print('Ingredientes disponibles:')
                    for i, (ingrediente,precio) in enumerate(zip(ingredientes_extra,precios_extra), start = 1):
                        print(f'{i} - {ingrediente} -{precio}€')

                    eleccion = int(input('Seleccione el número del ingrediente que desea añadir: '))
                    if 1 <= eleccion <= len(ingredientes_extra):
                        costo_extra = precios_extra[eleccion- 1]
                        if dinero >= costo_extra:
                            dinero -= costo_extra
                            total += costo_extra
                            print(f'Ha añadido {ingredientes_extra[eleccion-1]} por {costo_extra}€.\n')
                            print(f'Total actualizado: {total}€.\n')
                            print(f'Dinero restante: {round(dinero,2)}€\n')
                        else:
                            print('No tienes suficiente dinero para ese ingrediente.\n')
                    else:
                        print('Opción de ingrediente no válida. Intente nuevamente.\n')
                elif extra == 2:
                    print('Compra finalizada.\n')
                    print(f'Total de la compra: {total}€.\n')
                    print(f'Dinero restante: {round(dinero,2)}€.\n')
                    compra_realizada = True
                    break
                else:
                    print('Opción no válida. Intente nuevamente.\n')
            break # Sale del bucle interno porque la compra es válida
 
        else:
            print('No tiene dinero suficiente para esta pizza. Seleccione otra.\n')
            total = 0  # Resetea el total para evitar problemas en la próxima iteración    
    if compra_realizada:
        break  # Sale del bucle externo tras una compra válida

        
if not compra_realizada and dinero < 7.85:
    print('No tiene el dinero suficiente para comprar ningún producto. Vuelva en otra ocasión.')



