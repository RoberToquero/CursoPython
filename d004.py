# Listas 
# Una lista es una variable que puede contener más de un valor a la vez y de diferentes tipos
lista_colores = ["rojo", "azul", "amarillo", "verde"]
lista_colores[1] = 'naranja' # sustituir un valor de la lista
print(lista_colores[0]) # acceder a un valor concreto de la lista
print(lista_colores[3][0]) # acceder a un valor concreto de un elemento de la lista

# Añadir un valor a la lista
lista_colores.append('azul')
print(lista_colores)
lista_colores.insert(2,"violeta") # añadir un valor en una posicion concreta
print(lista_colores)

#vaciar la lista lista_colores.clear()
# eliminar un valor concreto
lista_colores.pop(0)
print(lista_colores)
lista_colores.remove('violeta') #Eliminar un elemento indicando su valor
# copiar el contenido de una lista en otra
lista2 = lista_colores.copy()
lista2.append('amarillo')
# contar cuantas veces se repite elemento
print(lista2.count('amarillo'))
# saber en que posicion se encuentra un elemento concreto
print(lista2.index('naranja'))
# invertir las posiciones de una lista
lista2.reverse()
# ordenar alfabeticamente o numéricamente (si es int) el orden de las listas
lista2.sort()
#orden descendente
lista2.sort(reverse=True)
# unir listas
lista_colores.extend(lista2)

# TUPLAS
# Las tuplas son listas pero inmutables
mi_tupla = (2,4,6,8,10)
# Escoger un elemento de la tupla
print(mi_tupla[1])
# Contar los elementos de una lista y tupla
print(len(lista_colores))
print(len(mi_tupla))
# EJERCICIOS
lista_numeros = [10, 45, 55, 76]
print(lista_numeros[3])
print(f'El valor más pequeño en la lista es el {lista_numeros[0]}. El más grande es el {lista_numeros[3]}.')
lista_color = ['rojo', 'azul', 'verde', 'amarillo']
lista_color.insert(0, 'gris')
lista_color.append('rosa')
lista_color.insert(3,'naranja')
print(lista_color)
lista_color.pop(1)
lista_color.pop(3)
lista_color.pop(3)
print(lista_color)
lista_color2 = lista_color.copy()


