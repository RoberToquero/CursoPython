# DICCIONARIOS
office = {
    'word':'Procesador de texto',
    'excel':'Hoja o plantilla de cálculo',
    'power':'Crear presentaciones'
}
print(office['word'])
# Añadir al diccionario
office['outlook'] = 'Correo electrónico'

# BUCLES PARA ITERAR TODO EL DICCIONARIO
for programa in office:
    print(programa.capitalize() + '--> ' + office[programa]) # método capitalize pone en mayúsculas la primera letra

# SETS
# Listas desordenadas sin índice de posición. SIN ELEMENTOS DUPLICADOS
animales = {'perro', ' iguana', 'gato', 'pìtón', 'chimpancé'}
print(animales)

