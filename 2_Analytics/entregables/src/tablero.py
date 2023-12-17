import numpy as np
import funciones

class Tablero:
    def __init__(self, player, tamaño=10):
        self.tamaño = tamaño
        self.player = player
        self.barcos = []  # Inicializar la lista de barcos
        self.tablero = np.full((tamaño, tamaño), " ")
        self.tablero_del_enemigo_que_ves = np.full((tamaño, tamaño), " ")

    def rellenar_tablero(self):
        # Posiciones de los barcos iniciales
        tamaños_barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        for tamaño in tamaños_barcos:
            self.barcos.append(funciones.nuevo_barco(tamaño, self.tablero))

'''
# Crear una instancia de la clase Tablero
tablero_player = Tablero("player")
tablero_pc = Tablero("pc")

# Llamar al método para rellenar el tablero
tablero_player.rellenar_tablero()
tablero_pc.rellenar_tablero()

funciones.disparo_yo(tablero_pc.barcos,tablero_player.tablero_del_enemigo_que_ves,tablero_pc.tablero)
funciones.dispara_enemigo(tablero_player.barcos,tablero_pc.tablero_del_enemigo_que_ves,tablero_player.tablero)

# Imprimir el tablero y la lista de barcos
print(tablero_player.tablero,"\n")
print(tablero_player.tablero_del_enemigo_que_ves,"\n")
print(tablero_pc.tablero,"\n")
print(tablero_pc.tablero_del_enemigo_que_ves)
'''