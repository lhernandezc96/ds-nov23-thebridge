import numpy as np
import funciones
import tablero

def jugar():
    print('''
 _   _                 _ _        _          __ _       _        
| | | |               | (_)      | |        / _| |     | |       
| |_| |_   _ _ __   __| |_ _ __  | | __ _  | |_| | ___ | |_ __ _ 
|  _  | | | | '_ \ / _` | | '__| | |/ _` | |  _| |/ _ \| __/ _` |
| | | | |_| | | | | (_| | | |    | | (_| | | | | | (_) | || (_| |
\_| |_/\__,_|_| |_|\__,_|_|_|    |_|\__,_| |_| |_|\___/ \__\__,_|
                                                                 
 \n'''                                                                
)
    print('''Bienvenido al juego de Hundir la flota, tanto tu como tu oponente dispondreis de un tablero con
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora''')

    player = tablero.Tablero("player")
    player.rellenar_tablero()
    pc = tablero.Tablero("pc")
    pc.rellenar_tablero()
    print ("""Tus barcos se posicionan aleatoriamente en el tablero, al igual que los de la maquina.
Así ha quedado tu tablero: \n""", player.tablero)
    print('''El juego es sencillo, consiste en ir introduciendo coordenadas hasta que hundas todos los barcos del rival.
Cuando disparas se marcara con un - si el disparo ha fallado y con una X cuando el disparo de en el blanco.
El tablero es de tamañao 10x10, por lo que las coordenadas que debemos introducir van de 0 a 9.
Por ejemplo, si queremos disparar a la segunda fila y la tercera columna deberemos introducir primero un 1 y despues un 2
          
Empecemos a jugar!!

Si en cualquier momento quieres salir de juego solo tienes que escribir la palabra: end         
          
Lo primero de todo tenemos que escoger la dificultad:
    Nivel 1: Cada turno el enemigo dispara hasta fallar una vez
    Nivel 2: Cada turno el enemigo dispara hasta fallar dos veces
    Nivel 3: Cada turno el enemigo dispara hasta fallar 3 veces''')
    def pedir_dif ():
        try:
            dificultad =  input("¿Que dificultad eliges?: ")
            if dificultad == "end":
                return "end"
            dificultad = int(dificultad)
            while 0 > dificultad or dificultad > 3:
                print ("El valor introducida debe estar comprendido entre 1 y 3")
                return pedir_dif()
            return dificultad
        except:
            print ("Debe introducir un valor numerico comprendido entre 1 y 3")
            return pedir_dif()
    dificultad = pedir_dif()
    if dificultad == "end":
        return 


    print('''Bien,una vez elegida la dificultad empecemos''')
    while funciones.seguir_juego(player.tablero) and funciones.seguir_juego(pc.tablero):
        print('''Es tu turno, Tu tablero se encuentra asi:''',player.tablero,"Y asi esta el tablero de tu contrincante:",player.tablero_del_enemigo_que_ves, sep="\n")
        print("¿A que coordenadas quieres disparar? ")
        disparo_dado = True
        while disparo_dado:
            coordenada_x = input("Introduce la fila a la que quieres disparar: ")
            if coordenada_x == "end":
                return
            coordenada_y = input("Introduce la columna a la que quieres disparar: ")
            if coordenada_y == "end":
                return
            try:
                coordenadas = (int(coordenada_x),int(coordenada_y))
                funciones.disparo(coordenadas,pc.barcos,player.tablero_del_enemigo_que_ves,pc.tablero)
            except:
                print("Por favor asegurese que las coordenadas introducidas deben ser numeros enteros del 0 al 9")
                continue
            disparo_dado = player.tablero_del_enemigo_que_ves[coordenadas[0], coordenadas[1]] == "X"
            if disparo_dado:
                print ("Has dado a un barco enemigo, asi esta el tablero de tu contrincante:",player.tablero_del_enemigo_que_ves,"Puedes volver a disparar", sep="\n")
                if ~funciones.seguir_juego(pc.tablero):
                    break
        print("¡AGUA! Has fallado, es el turno de la maquina")
        disparo_dado_pc = True
        dif = dificultad
        while dif > 0:
            while disparo_dado_pc:
                coordenadas_pc = (np.random.randint(0, 10), np.random.randint(0, 10))
                if ~funciones.seguir_juego(player.tablero):
                    break
                if pc.tablero_del_enemigo_que_ves[coordenadas_pc[0], coordenadas_pc[1]] == "X" or pc.tablero_del_enemigo_que_ves[coordenadas_pc[0], coordenadas_pc[1]] == "-":
                    continue
                print("La maquina dispara a las coordenadas", coordenadas_pc)
                funciones.disparo(coordenadas_pc,player.barcos,pc.tablero_del_enemigo_que_ves,player.tablero)
                disparo_dado_pc = pc.tablero_del_enemigo_que_ves[coordenadas_pc[0], coordenadas_pc[1]] == "X"
                if disparo_dado_pc:
                    print("¡NOS HAN DADO! Le vuelve a tocar a la maquina")
                    if ~funciones.seguir_juego(player.tablero):
                        break
            disparo_dado_pc = True
            if dif == 1:
                print("La maquina ha fallado y no le quedan mas disparos")
            else:
                print("La maquina ha fallado pero le quedan mas disparos ("+str(dif-1)+")")
            dif -= 1
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
            


        
        

jugar()