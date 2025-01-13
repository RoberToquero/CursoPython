class Motocicleta():
    # Atributo de clase
    estado = 'nueva'
    motor = False

    #Constructor
    def __init__(self, color, matricula,combustible_litros, numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso,capacidad):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.capacidad = capacidad
    
    def arrancar(self):
        if self.motor == False:
             self.motor = True
             print('El motor ha arrancado, ruge como un león.')
        else:
            print('Se escuha un molesto sonido al girar la llave, el motor ya estaba en marcha')

    def detener(self):
        if self.motor != False:
            self.motor = False
            print('El motor se ha detenido.')
        else:
            print('El motor ya estaba detenido.')

    def consulta_precio(self):
        print(f'El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio}')

    def consultar_litros(self):
        print(f'--->REPORTE DE DEPÓSITO DE {self.marca} {self.modelo}<---')
        print(f'El depósito tiene {self.combustible_litros}.')
        print(f'La capacidad máxima del tanque de combustible es de {self.capacidad}')
        print(f'Faltan {self.capacidad - self.combustible_litros} para llenar el depósito.')
        print('--->FIN DEL REPORTE<---')
        
    def repostar(self):
        litros_repostados = int(input('Por favor, introduzca los litros que desea repostar:\n'))
        while (litros_repostados + self.combustible_litros) > self.capacidad:
            print('No cabe tanto combustible. ¿Quieres encharcar el concesionario?')
            litros_repostados = int(input('Por favor, introduzca los litros que desea repostar:\n'))
        self.combustible_litros+=litros_repostados
        print(f'Repostaje exitoso.\nSe han repostado {litros_repostados} litros.\nEl depósito tiene {self.combustible_litros} litros de combustible.')
       

# Instanciar un objeto

motocicleta_yamaha = Motocicleta('Roja y blanca', '45663-FHD', 10, 2, 'Yamaha','YZF-R1', '22/02/2022', 288, 199,17)
motocicleta_harley = Motocicleta(matricula = '48659-FHE', combustible_litros=0,color='Negra', marca='Harley Davidson',
modelo='Fat Boy', numero_ruedas=2,peso=304,fecha_fabricacion='29/03/2021', velocidad_punta=160, capacidad=20)

# Llamando a un método
motocicleta_yamaha.arrancar()
motocicleta_harley.detener()

# Asignar a uno de los dos objetos un atributo nuevo llamado precio
motocicleta_harley.precio = 27000
motocicleta_yamaha.precio = 21000
motocicleta_harley.consulta_precio()
motocicleta_yamaha.consulta_precio()

motocicleta_yamaha.consultar_litros()
motocicleta_yamaha.repostar()
