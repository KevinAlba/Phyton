import random
#*******************************************PedraPaperTisores***************************************
def PedraPaperTisores():
    puntosJugadorPrincipal = 0
    puntosJugadirRival = 0
    
    opciones = {
        1: 'Pedra',
        2: 'Paper',
        3: 'Tisores'
    }

    while puntosJugadorPrincipal < 3 and puntosJugadirRival < 3:

        print('----------------------------- Menu  Pedra - Paper - Tisores ----------------------------------')
        print('1. Pedra ')
        print('2. Paper ')
        print('3. Tisores ')

        try: 
            opcion_usario = int(input('Elige una opción (1-3): '))
            opcionRival = random.randint(1, 3)

            texto_usuario = opciones[opcion_usario]
            texto_maquina = opciones[opcionRival]

            if opcion_usario == 1 and opcionRival == 3 or opcion_usario == 2 and opcionRival == 1 or opcion_usario == 3 and opcionRival == 2:
                print(f'Usuario a sacado: {texto_usuario}')
                print(f'Maquina a sacado: {texto_maquina}')
                print(f'El ganador de esta ronda es Usuario ')

                puntosJugadorPrincipal += 1
            elif opcion_usario == opcionRival:
                print(f'Usuario a sacado: {texto_usuario}')
                print(f'Maquina a sacado: {texto_maquina}')
                print("La partida es un empate")
            else: 
                print(f'Usuario a sacado: {texto_usuario}')
                print(f'Maquina a sacado: {texto_maquina}')
                print(f'El ganador de esta ronda es la maquina ')
                puntosJugadirRival += 1
        except (ValueError, KeyError):
            print('opcion no valida')

        print('Puntos Usuario: ', puntosJugadorPrincipal)
        print('Puntos Maquina: ', puntosJugadirRival)
        
    if puntosJugadorPrincipal > puntosJugadirRival:
        print('El ganador del juego es Usuario')
    else:
        print('El ganador del juego es Maquina')

#********************************************Ahorcado*****************


def Ahorcado():
    palabrasRandom = random.choice([
        'gato', 'perro', 'casa', 'libro', 'mesa', 'silla', 'coche', 'flor', 'arbol', 'sol',
        'luna', 'estrella', 'mariposa', 'elefante', 'jirafa', 'tigre', 'leon', 'oso', 'conejo', 'pez'
    ])

    intentos = len(palabrasRandom) * 2
    letras = []
    errores = 0

    while errores < intentos:    
        letraUsuario = input('Dime la letra q quieras eleguir: ').lower()
        palabraOculta = ''

        if letraUsuario in letras:
            print('Intentalo de nuevo esta letra ya la has probado. Vuelvelo a intentar')
        elif letraUsuario not in palabrasRandom:
            letras.append(letraUsuario)
            errores += 1
        else:
            letras.append(letraUsuario)

        for letra in palabrasRandom:
            if letra in letras:
                palabraOculta += letra + ' '
            else:
                palabraOculta += '_ '

        print("Palabra:", palabraOculta)
        print(f"Errores: {errores}/{intentos}") 

        if '_' not in palabraOculta:
            print('Felicidades has ganado')
            break

    if errores >= intentos:
        print(f'Has perdido la palabra oculta es: {palabrasRandom}')

#********************************************TRES en Raya*****************#

def tresEnRatlla():
    posicionTabla = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    jugador1 = input('Dime el nombre del jugador1: ')
    print(f'El jugador1 es {jugador1} y su simbolo es: X')
    jugador2 = input('Dime el nombre del jugador2: ')
    print(f'El jugador2 es {jugador2} y su simbolo es: O')

    turnos = 0
    ganador = False

    while turnos < 9 and not ganador:
        if turnos % 2 == 0:
            jugador = jugador1
            simbolo = 'X'
        else:
            jugador = jugador2
            simbolo = 'O'

        print(f'{posicionTabla[0]} | {posicionTabla[1]} | {posicionTabla[2]}')
        print('---+---+---')
        print(f'{posicionTabla[3]} | {posicionTabla[4]} | {posicionTabla[5]}')
        print('---+---+---')
        print(f'{posicionTabla[6]} | {posicionTabla[7]} | {posicionTabla[8]}')

        posicion = int(input(f'{jugador} ({simbolo}), dime la posicion( 1 - 9 ): ')) - 1

        while posicionTabla[posicion] == 'X' or posicionTabla[posicion] == 'O':
            print('Esta ocupada')
            posicion = int(input(f'{jugador} ({simbolo}), dime la posicion( 1 -9 ): ')) - 1

        posicionTabla[posicion] = simbolo
        turnos += 1

        if (posicionTabla[0] == posicionTabla[1] == posicionTabla[2]) or \
           (posicionTabla[3] == posicionTabla[4] == posicionTabla[5]) or \
           (posicionTabla[6] == posicionTabla[7] == posicionTabla[8]) or \
           (posicionTabla[0] == posicionTabla[3] == posicionTabla[6]) or \
           (posicionTabla[1] == posicionTabla[4] == posicionTabla[7]) or \
           (posicionTabla[2] == posicionTabla[5] == posicionTabla[8]) or \
           (posicionTabla[0] == posicionTabla[4] == posicionTabla[8]) or \
           (posicionTabla[2] == posicionTabla[4] == posicionTabla[6]):
            ganador = True

            print(f'{posicionTabla[0]} | {posicionTabla[1]} | {posicionTabla[2]}')
            print('---+---+---')
            print(f'{posicionTabla[3]} | {posicionTabla[4]} | {posicionTabla[5]}')
            print('---+---+---')
            print(f'{posicionTabla[6]} | {posicionTabla[7]} | {posicionTabla[8]}')

            print(f'Ha ganado la partida {jugador}!')
        else:            
            print(f'{posicionTabla[0]} | {posicionTabla[1]} | {posicionTabla[2]}')
            print('---+---+---')
            print(f'{posicionTabla[3]} | {posicionTabla[4]} | {posicionTabla[5]}')
            print('---+---+---')
            print(f'{posicionTabla[6]} | {posicionTabla[7]} | {posicionTabla[8]}')

            print('Empate')


def BlackJack():

    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(cartas)

    jugador = [cartas.pop(), cartas.pop()]
    maquina = [cartas.pop(), cartas.pop()]

    print(f'Tus cartas: {jugador} / Suma: {sum(jugador)}')

    pedir = input('Quieres otra carta? (s/n): ')
    if pedir == 's':
        jugador.append(cartas.pop())
        print(f'Tus cartas ahora: {jugador} / Suma: {sum(jugador)}')

    print(f'Puntos tuyos: {sum(jugador)}')
    print(f'Puntos máquina: {sum(maquina)}')

    if sum(jugador) > 21:
        print('Te pasaste de 21. Perdiste')
    elif sum(jugador) > sum(maquina) or sum(maquina) > 21:
        print('Ganaste')
    else:
        print('gana la maquina')
    


def mostrarMenu():
    while True:
        print('----------------------------- Menu juego Principal ----------------------------------')
        print('1. Pedra - Paper - Tisores: ')
        print('2. Penjat - Ahorcado: ')
        print('3. Tres en ratlla: ')
        print('4. BlackJack: ')
        print('5. Salir')

        try:
            juegos = int(input('A que juego quieres jugar (1 - 5 ): '))
       
            if juegos == 1:
                PedraPaperTisores()
            elif juegos == 2:
                Ahorcado()
            elif juegos == 3:
                tresEnRatlla()
            elif juegos == 4:
                BlackJack()
            elif juegos == 5:
                print('Saliendo...')
                break
            else:
                print('La opción no es correcta, vuelve a intentarlo')
        except (ValueError):
            print('Solo numero enteros')
mostrarMenu()