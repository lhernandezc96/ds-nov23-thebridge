import numpy as np
# Función para posicionar un barco en el tablero
def posicionar_barco(barco,tablero):
    for posicion in barco:
        tablero[posicion[0], posicion[1]] = "O"

barcos = []

# Función para generar un nuevo barco de longitud 4 aleatoriamente
def nuevo_barco(tamaño,tablero):
    posicion = (np.random.randint(0, 10), np.random.randint(0, 10))
    orientacion = np.random.randint(0, 4)  # 0->N, 1->S, 2->E, 3->O
    barco_nuevo = []

    # Verificar si hay espacio para posicionar el barco según la orientación
    if orientacion == 0 and posicion[0] >= tamaño-1:
        for i in range(tamaño):
            barco_nuevo.append(((posicion[0] - i), posicion[1]))
    elif orientacion == 1 and posicion[0] <= 10-tamaño:
        for i in range(tamaño):
            barco_nuevo.append(((posicion[0] + i), posicion[1]))
    elif orientacion == 2 and posicion[1] <= 10-tamaño:
        for i in range(tamaño):
            barco_nuevo.append(((posicion[0]), posicion[1] + i))
    elif orientacion == 3 and posicion[1] >= tamaño-1:
        for i in range(tamaño):
            barco_nuevo.append(((posicion[0]), posicion[1] - i))
    else:
        return nuevo_barco(tamaño,tablero)  # Si no hay espacio, generar un nuevo barco

    # Verificar que el nuevo barco no se superponga con los existentes
    for posi_barco_nuevo in barco_nuevo:
        for barco in barcos:
            for posi_barco in barco:
                if posi_barco == posi_barco_nuevo:
                    return nuevo_barco(tamaño,tablero)  # Si se superpone, generar un nuevo barco

    # Imprimir el nuevo barco y posicionarlo en el tablero
    posicionar_barco(barco_nuevo,tablero)
    barcos.append(barco_nuevo)
    return barco_nuevo



# Función para realizar un disparo en el tablero
def disparo(coordenadas,barcos_enemigos,tablero_del_enemigo_que_ves,tablero):
    for barco in barcos_enemigos:
        for posicion in barco:
            if posicion == coordenadas:
                tablero_del_enemigo_que_ves[coordenadas[0], coordenadas[1]] = "X"
                tablero[coordenadas[0], coordenadas[1]] = "X"
                break
            elif posicion != coordenadas and tablero_del_enemigo_que_ves[coordenadas[0], coordenadas[1]] == " ":
                tablero_del_enemigo_que_ves[coordenadas[0], coordenadas[1]] = "-"
                tablero[coordenadas[0], coordenadas[1]] = "-"
                break

#Función para detectar si se han hundido todos los barcos
def seguir_juego (tablero):
    return np.any(tablero == "O")

# Función para pedir la dificultad al jugador
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



        
    