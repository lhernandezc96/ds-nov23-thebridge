# Importar las librerías necesarias
import numpy as np
import funciones  # funciones.py debe contener las funciones necesarias para el juego
import tablero    # tablero.py debe contener la clase Tablero
import time

def imprimir_poco_a_poco(texto, velocidad=0.025):
    for caracter in texto:
        print(caracter, end='', flush=True)  # Utiliza flush=True para que se imprima de inmediato
        time.sleep(velocidad)  # Pausa entre caracteres
    
# Función principal para iniciar el juego
def jugar():
    # Mensaje de bienvenida
    print('''
 _   _                 _ _        _          __ _       _        
| | | |               | (_)      | |        / _| |     | |       
| |_| |_   _ _ __   __| |_ _ __  | | __ _  | |_| | ___ | |_ __ _ 
|  _  | | | | '_ \ / _` | | '__| | |/ _` | |  _| |/ _ \| __/ _` |
| | | | |_| | | | | (_| | | |    | | (_| | | | | | (_) | || (_| |
\_| |_/\__,_|_| |_|\__,_|_|_|    |_|\__,_| |_| |_|\___/ \__\__,_|
                                                                 
 \n''')

    imprimir_poco_a_poco('''Bienvenido al juego de Hundir la flota, tanto tú como tu oponente dispondréis de un tablero con
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora''')
    print()

    # Crear los tableros para el jugador y la máquina
    player = tablero.Tablero("player")
    player.rellenar_tablero()
    pc = tablero.Tablero("pc")
    pc.rellenar_tablero()

    # Mostrar la posición de los barcos del jugador
    imprimir_poco_a_poco("Tus barcos se posicionan aleatoriamente en el tablero, al igual que los de la máquina.")
    print()
    imprimir_poco_a_poco("Así ha quedado tu tablero:")
    print()
    print(player.tablero)

    imprimir_poco_a_poco('''El juego es sencillo, consiste en ir introduciendo coordenadas hasta que hundas todos los barcos del rival.
Cuando disparas, se marcará con un "-" si el disparo ha fallado y con una "X" cuando el disparo de en el blanco.
El tablero es de tamaño 10x10, por lo que las coordenadas que debemos introducir van de 0 a 9.
Por ejemplo, si queremos disparar a la segunda fila y la tercera columna, debemos introducir primero un 1 y después un 2.
          
¡Empecemos a jugar!

Si en cualquier momento quieres salir del juego, solo tienes que escribir la palabra: end
          
Lo primero de todo tenemos que escoger la dificultad:
    Nivel 1: Cada turno el enemigo dispara hasta fallar una vez
    Nivel 2: Cada turno el enemigo dispara hasta fallar dos veces
    Nivel 3: Cada turno el enemigo dispara hasta fallar 3 veces''')
    print()


    # Pedir la dificultad al jugador
    dificultad = funciones.pedir_dif()
    
    # Salir si el jugador escribió "end"
    if dificultad == "end":
        return 

    imprimir_poco_a_poco("Bien, una vez elegida la dificultad, ¡empecemos!")
    print()

    # Bucle principal del juego
    while funciones.seguir_juego(player.tablero) and funciones.seguir_juego(pc.tablero):
        # Mostrar el estado actual de los tableros
        imprimir_poco_a_poco("Es tu turno, tu tablero se encuentra así:")
        print()
        print(player.tablero)
        imprimir_poco_a_poco("Y así está el tablero de tu contrincante:")
        print()
        print(player.tablero_del_enemigo_que_ves)

        # Pedir al jugador las coordenadas para disparar
        imprimir_poco_a_poco("¿A qué coordenadas quieres disparar?")
        print()
        disparo_dado = True
        while disparo_dado:
            imprimir_poco_a_poco("Introduce la fila a la que quieres disparar: ")
            coordenada_x = input()
            if coordenada_x == "end":
                return
            imprimir_poco_a_poco("Introduce la columna a la que quieres disparar: ")
            coordenada_y = input()
            if coordenada_y == "end":
                return
            try:
                coordenadas = (int(coordenada_x), int(coordenada_y))
                funciones.disparo(coordenadas, pc.barcos, player.tablero_del_enemigo_que_ves, pc.tablero)
            except:
                imprimir_poco_a_poco("Por favor, asegúrate de que las coordenadas introducidas sean números enteros del 0 al 9")
                print()
                continue
            disparo_dado = player.tablero_del_enemigo_que_ves[coordenadas[0], coordenadas[1]] == "X"
            if disparo_dado:
                imprimir_poco_a_poco("Has dado a un barco enemigo. Así está el tablero de tu contrincante:")
                print()
                print(player.tablero_del_enemigo_que_ves)
                imprimir_poco_a_poco("Puedes volver a disparar")
                print()

                # Salir si ya no quedan barcos enemigos
                if ~funciones.seguir_juego(pc.tablero):
                    break

        # Mostrar mensaje de "AGUA" si el disparo falló
        imprimir_poco_a_poco("¡AGUA! Has fallado, es el turno de la máquina")
        print()

        # Bucle de disparos de la máquina según la dificultad
        disparo_dado_pc = True
        dif = dificultad
        while dif > 0:
            while disparo_dado_pc:
                # Generar coordenadas aleatorias para el disparo de la máquina
                coordenadas_pc = (np.random.randint(0, 10), np.random.randint(0, 10))

                # Salir si ya no quedan barcos del jugador
                if ~funciones.seguir_juego(player.tablero):
                    break

                # Continuar si ya se disparó a esa posición
                if pc.tablero_del_enemigo_que_ves[coordenadas_pc[0], coordenadas_pc[1]] == "X" or pc.tablero_del_enemigo_que_ves[coordenadas_pc[0], coordenadas_pc[1]] == "-":
                    continue

                # Mostrar mensaje de disparo de la máquina
                imprimir_poco_a_poco("La máquina dispara a las coordenadas ")
                print(coordenadas_pc)

                # Procesar el disparo de la máquina
                funciones.disparo(coordenadas_pc, player.barcos, pc.tablero_del_enemigo_que_ves, player.tablero)

                # Actualizar la variable de control si el disparo dio en el blanco
                disparo_dado_pc = pc.tablero_del_enemigo_que_ves[coordenadas_pc[0], coordenadas_pc[1]] == "X"

                # Mostrar mensaje de que la máquina volverá a disparar
                if disparo_dado_pc:
                    imprimir_poco_a_poco("¡NOS HAN DADO! Le vuelve a tocar a la máquina")
                    print()

                # Salir si ya no quedan barcos del jugador
                if ~funciones.seguir_juego(player.tablero):
                    dif = 0
                    break

            # Reiniciar la variable de control y mostrar mensaje de resultado del disparo de la máquina
            disparo_dado_pc = True
            if dif == 1:
                imprimir_poco_a_poco("La máquina ha fallado y no le quedan más disparos")
                print()
            else:
                imprimir_poco_a_poco("La máquina ha fallado pero le quedan más disparos")
                print(f"({dif - 1})")
            dif -= 1

    # Mostrar el resultado final del juego
    else:
        if ~funciones.seguir_juego(player.tablero):
            print('''
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                      ''')
        elif ~funciones.seguir_juego(pc.tablero):
            print('''
 __      ___      _             _       
 \ \    / (_)    | |           (_)      
  \ \  / / _  ___| |_ ___  _ __ _  __ _ 
   \ \/ / | |/ __| __/ _ \| '__| |/ _` |
    \  /  | | (__| || (_) | |  | | (_| |
     \/   |_|\___|\__\___/|_|  |_|\__,_|
                                        
                                       
''')

# Llamar a la función principal para iniciar el juego
jugar()
