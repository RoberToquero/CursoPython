# Strings avanzados
p = 'Programación'
f = 'Fácil'
print(p,f)

# # Método join, es uno de los de la clase str
print('*'.join([p,f])) 
colores = ['rojo', 'azul', 'amarillo', 'verde']
separador = '€'
concatena = separador.join(colores)
print(concatena)

print("%s %s" % (p,f)) # Otra forma de imprimir String

# Formateo de Strings
print('{} fgf {}'.format(p,f))

texto = ''' Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla non aliquet orci. 
Aenean eros est, pharetra eget viverra et, ultricies nec metus. Integer dapibus ex sit amet ipsum lacinia 
porttitor. In dapibus mi consequat justo luctus gravida. Vivamus auctor aliquet vestibulum. Vivamus nulla
magna, dictum ac mollis ac, pharetra at est. Donec vitae libero erat. Vestibulum rhoncus blandit eros, ut elementum 
magna sagittis sit amet. Nunc accumsan risus eget est sagittis, quis tempor est pulvinar. Sed ornare quis eros ac varius.
Maecenas volutpat consectetur ante, quis vulputate tellus laoreet sit amet. Nullam quis mauris ac ante consequat pretium 
laoreet vel arcu. Vestibulum id mauris risus.'''
print(texto)

print((p+" ")*3)

pf= 'Programación Fácil'
for letra in pf:
    print(letra)
    
for letra in range(len(pf)):
    print(pf[letra])

# Generar diccionario
lista_pf = dict(enumerate(pf))

print(lista_pf)

# Lo mismo para generar un lista con tuplas

lista = list(enumerate(pf))
print(lista) #También puede hacerse con sets

GUION = '-'
PUNTO = '.'

for color in colores:
    print('{}{}{}'.format(GUION,color.capitalize(),PUNTO))
    
#  Ejercicio 

fr= '''Muy lejos, más allá de las montañas de palabras, alejados de los países de las 
vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica
un gran océano de lenguas.
'''

t = input('Qué letra quieres rastrear? \n')
contador = 0
frase = fr.lower()
for letra in frase:
    if letra == t:
        contador+=1
    
print(f'Se encontró {contador} veces la letra {t}')


