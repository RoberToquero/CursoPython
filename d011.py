#PROGRAMACIÓN ORIENTADA A OBJETOS (POO)

class Vehiculo(): 

    # Atributos de clase (valores por defecto que tienen todos)

    pais_origen = 'Alemania'


    def __init__(self, color, longitud,ruedas): #Constructor que tiene los atributos de instancia
        self.color = color
        self.longitud = longitud
        self.ruedas = ruedas

    # MÉTODOS
    def arrancar(self):
        print('El vehículo ha arrancado.')

    def detener(self):
        print('El vehículo se ha detenido.')

    # Cuando se llama a un atributo en un método siempre hay que ponerlo así:
    def mostrar_info(self):
        print(f'Vehículo de color {self.color}. Con una longitud de {self.longitud}. Tiene {self.ruedas} ruedas.')

# Instancia de objetos
vehiculo_1 = Vehiculo('rojo', 4, 4)
vehiculo_2 = Vehiculo('negro', 8.25, 8)

vehiculo_1.mostrar_info()

class Camion(): #Clase vacía 
    pass

