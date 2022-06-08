'''
En este juego, el jugador se encuentra en una tierra llena de dragones. Los dragones viven en sus cuevas y en ellas guardan 
sus tesoros. Algunos dragones son buenos y compartirán su tesoro, otros dragones son codiciosos y hambrientos y se comerán a 
cualquiera que pise su cueva. El jugador se encuentra frente a las dos cuevas, una con un dragón amable y otra con 
un dragón hambriento. El jugador tiene que elegir a cual cueva entrar, sin saber de ante mano donde esta uno u el otro. 
'''
import random
import time

print ('Historia: Estamos en una tierra llena de dragones. Delante nuestro, se ven dos cuevas. En una cueva, el dragón es amigable y compartirá el tesoro contigo. En la otra el dragón es codicioso, hambriento, y te comerá sin dudarlo.')

def chooseCave():
    '''Función encargada de preguntarle al usuario que cueva desea elegir y devolverá su respuesta.'''

    cave = 0
    try:
        while cave != 1 and cave != 2:
            cave = int(input('''
Elige una Cueva ¿1 ó 2?
>>>'''))

        return cave

    except ValueError:
        chooseCave()
    

def final_cave(chooseCave):
    '''Función que se encargará de comparar la cueva que ha sido escogida por el usuario y mostrar el ganador. Parámetros:
    -chooseCave: llamada de otra función que tendrá la cueva elegida por el usuario.
    '''

    print ("\nTe acercas a la Cueva...")
    time.sleep(2)
    print ("Está oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragón salta delante tuyo, abre su boca y...")
    time.sleep(2.5)
    
    good_cave = random.randint(1, 2)

    if chooseCave == good_cave:
        print("El Dragón ha resultado ser amable, te ha entregado el tesoro! :D")
    else:
        print('''
El Dragón te ha comido...  
GAME OVER   :'(''')


#Menú Intro:
while True:
    option = input('''
¿Quieres Intentarlo? [S/N] :
>>>''')

    if option.upper() == 'S':
        choosed_cave = chooseCave()
        final_cave(choosed_cave)
        break

    elif option.upper() == 'N':
        break

    else:
        print("ERROR!")