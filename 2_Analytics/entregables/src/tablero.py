import numpy as np
import funciones

class Tablero:
    def __init__(self, player, tamaño=10):
        self.tamaño = tamaño
        self.player = player
        self.barcos = []  # Inicializar la lista de barcos
        self.tablero = np.full((tamaño, tamaño), " ")
        self.tablero_del_enemigo_que_ves = np.full((tamaño, tamaño), " ")

    def rellenar_tablero(self,tamaños_barcos = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]):
        # Posiciones de los barcos iniciales
        
        for tamaño in tamaños_barcos:
            self.barcos.append(funciones.nuevo_barco(tamaño, self.tablero))

