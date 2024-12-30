# Condicionales
# numero = 7
# if numero > 7:
#     print("El número es mayor que 7.")
# elif numero == 7:
#     print("El número es igual a 7.")
# else:
#     print("EL número es menor que 7.")
"""
Operadores: 
> mayor que
< menor que
>= mayor o igual que
<= menor o igual que
== igual a
!= distinto de

"""
# edad = int(input("Introduzca su edad:\n"))
# if edad >= 18:
#     print("Es mayor de edad, puede comprar alcohol ¿Cuál desea comprar?")
#     opcion = int(input("1-ron.\n2-whisky.\n3- ginebra.\n"))
#     if opcion == 1:
#         print("Ha elegido comprar ron.")
#     elif opcion == 2:
#         print("Ha elegido comprar whisky.")
#     elif opcion == 3:
#         print("Ha elegido comprar ginebra.")
#     else:
#         print("Tienes que introducir una opción correcta.")
# else:
#     print("Eres menor de edad no puedes comprar alcohol.")

# and or not (operaciones lógicos)
# color = "rojo"
# forma = "circulo"
# if color == "rojo" and forma == "circulo":
#     print("Es un circulo rojo")
# else:
#     print("No se cumple condición")

# # El condicional switch en Java aquí es match
# error = input("Introduce un código de error \n")

# match error:
#     case "200":
#         print("Todo ok.")
#     case "301":
#         print('Movimiento permanente de la página.')
#     case "302":
#         print('Movimiento temporal de la página.')
#     case "404":
#         print('Página no encontrada.')
#     case '500':
#         print('Error interno del servidor.')
#     case '503':
#         print('Servicio no disponible')
#     case _: # Bloque de código que representa el False 
#         print('Error no disponible.')    

"""Proyecto
            Calculadora con dos datos numéricos de sumas, restas. multiplicaciones. módulo y exponentes en la consola

"""
print('CALCULADORA TOP')
operacion=input('Escoge la operación que quieras realizar:\n 1: Suma\n 2: Resta\n 3: Multiplicacion\n 4: División\n 5: Módulo\n 6: Exponente\n Teclee un número y pulse ENTER:\n')

match operacion:
    case "1":
        print("Has elegido suma")
        dato_1 = float(input("Introduce un número: "))
        dato_2 = float(input("Introduce otro número: "))
        resultado = round(dato_1 + dato_2,2)
        print(f"La suma es: {resultado}")
    case "2":
         print("Has elegido resta")
         dato_1 = float(input("Introduce un número: "))
         dato_2 = float(input("Introduce otro número: "))
         resultado = round(dato_1 - dato_2,2)
         print(f"La resta es: {resultado}")
    case "3":
         print("Has elegido multiplicación")
         dato_1 = float(input("Introduce un número: "))
         dato_2 = float(input("Introduce otro número: "))
         resultado = round(dato_1 * dato_2,2)
         print(f"La multiplicación es: {resultado}")
    case "4":
         print("Has elegido división")
         dato_1 = float(input("Introduce un número: "))
         dato_2 = float(input("Introduce otro número: "))
         if dato_2 == 0:
              print("No se puede dividir entre 0")
         else:
          resultado = round(dato_1 / dato_2,2)
          print(f"La división es: {resultado}")
    case '5':
          print('Has elegido módulo de la división')
          dato_1 = float(input("Introduce un número: "))
          dato_2 = float(input("Introduce otro número: "))
          if dato_2 == 0:
              print("No se puede dividir entre 0")
          else:
           resultado = round(dato_1 % dato_2,2)
           print(f"El resto de la división es: {resultado}")
    case '6':
         print('Has elegido exponente.')
         dato_1 = float(input("Introduce un número: "))
         dato_2 = float(input("Introduce otro número: "))
         resultado = round(dato_1 ** dato_2,2)
         print(f"El exponente es: {resultado}")
    case _:
           print('Error, opción inválida.\nPor favor,vuelva a ejecutar la calculadora')
  