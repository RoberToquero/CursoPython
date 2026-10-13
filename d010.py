# FUNCIONES LAMBDA O ANONIMAS
# Solo pueden tener una expresión
# Se almacenan en una variable para poder llamarla, pero si solo se quiere usar una sola vez

multiplicacion = lambda numero1,numero2 : numero1*numero2
resultado1 = multiplicacion(10,7)
resultado2 = multiplicacion(56,5)

# declaracion y llamada en una misma linea
(lambda numero1,numero2 : print(numero1*numero2)) (7,5)

# EJERCICIO1: CREA CON UNA FUNCION LAMBDA UNA CALCULADORA DE ÁREAS DE CÍRCULO
PI = 3.14159265359
(lambda radio : print(f'El área del círculo es: {round(PI**radio,2)}') ) (int(input('Introduce un radio\n')))



