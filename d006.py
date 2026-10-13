# FUNCIONES
# def saludar():
#     nombre = input('Introduce tu nombre, por favor.\n')
#     print(f'¡Muy buenas, {nombre}!')

# saludar()

# # FUNCION CON ARGUMENTO
# def saludar_p(nombre1):
#     print(f'¡Muy buenas, {nombre1}!')

# saludar_p('Quique')

# Las funciones pueden tener más de un argumento
# Los argumentos vistos hasta aquí son posicionales
# Se pueden tener otro tipo de argumwntos que son llamados de clave 
# Los posicionales van por orden de posición en la declaravión de los parámetros
# Los clave van en cualquier orden, ya que se indica en el propio argumento, el parámetro como clave

# RETURN EN LAS FUNCIONES
# def suma(numero1, numero2):
#     return numero1 + numero2

# resultado = suma(10, 50) # Así se guarda en una variable el resultado de la operación y poder utilizarlo en el programa
# print(resultado)

# colores = ['rojo', 'verde', 'amarillo']
# def nuevo_color(color):
#     colores.insert(0, color)

# nuevo_color(input('Escriba un nuevo color para añadirlo a la lista:\n'))
# print(colores)

# PROYECTO
def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def producto(numero1, numero2):
    return round(numero1 * numero2,2)

def division(numero1,numero2):
     if numero2 == 0:
        return "Error: División entre cero"
     else:
        return round(numero1 / numero2, 2)

def resto(numero1,numero2):
    if numero2 == 0:
        return "Error: División entre cero"
    else:
        return round(numero1 % numero2, 2)

def exponente(numero1, numero2):
    return round(numero1 ** numero2,2)

print("¡Bienvenido a la calculadora en Python!")
salir = True
while salir:
    operacion=int(input('Escoge la operación que quieras realizar:\n 1: Suma\n 2: Resta\n 3: Multiplicacion\n 4: División\n 5: Módulo\n 6: Exponente\n Teclee un número y pulse ENTER:\n'))
    if operacion > 0 and operacion<=6:

        dato_1 = float(input("Introduce un número: "))
        dato_2 = float(input("Introduce otro número: "))
        match operacion:
            case 1:
                print("Has elegido suma")
                print(f"La suma es: {suma(dato_1,dato_2)}")
            case 2:
                print("Has elegido resta")
                print(f"La resta es: {resta(dato_1,dato_2)}")
            case 3:
                print("Has elegido multiplicación")
                print(f"La multiplicación es: {producto(dato_1,dato_2)}")
            case 4:
                print("Has elegido división")
                print(f"La división es: {division(dato_1,dato_2)}")
            case 5:
                print('Has elegido módulo de la división')     
                print(f"El resto de la división es: {resto(dato_1,dato_2)}")
            case 6:
                print('Has elegido exponente.')
                print(f"El exponente es: {exponente(dato_1,dato_2)}")
         
    else:
        print('Introduce una opción correcta.')

    respuesta = input('¿Desea salir? si/no \n')

    if respuesta.lower() == 'si':
        salir = False

print("¡Gracias por usar la calculadora! ¡Hasta pronto!")

print('CALCULADORA AUTOMATICA')
salir = True
while salir:
    x = float(input("Introduce un número: "))
    y = float(input("Introduce otro número: "))
    print(f'Suma: {suma(x,y)}\nResta: {resta(x,y)}\nProducto: {producto(x,y)}\nDivision: {division(x,y)}\nResto: {resto(x,y)}\nExponente: {exponente(x,y)}')
    respuesta = input('¿Desea salir? si/no \n')

    if respuesta.lower() == 'si':
        salir = False 


