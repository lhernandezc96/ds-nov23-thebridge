import random as rd
import time
import pandas as pd

def sacar_carta():
    # La función devuelve una tupla con el valor y el palo de la carta.
    return (rd.randint(1, 13), rd.choice(["Picas", "Corazones", "Treboles", "Diamantes"]))

class Jugador:
    def __init__(self, fichas=1000):
        # Inicializa la mano del jugador y sus fichas.
        self.mano = []
        self.fichas = fichas

    def saca_carta(self, carta):
        # Añade el valor de la carta a la mano del jugador.
        self.mano.append(carta)

    def reset_mano(self):
        # Reinicia la mano del jugador.
        self.mano = []

def imprimir_poco_a_poco(texto, velocidad=0.03):
    # Imprime el texto caracter por caracter con una pausa entre caracteres.
    for caracter in texto:
        print(caracter, end='', flush=True)  # Utiliza flush=True para que se imprima de inmediato
        time.sleep(velocidad)  # Pausa entre caracteres

def obtener_nombre_carta(valor):
    # Convierte el valor numérico de la carta a su nombre correspondiente.
    if valor == 1:
        return "As"
    elif valor == 11:
        return "Príncipe"
    elif valor == 12:
        return "Reina"
    elif valor == 13:
        return "Rey"
    else:
        return str(valor)

columnas = ['Valor Primera Carta', 'Cartas Restantes', 'Suma Mano', 'Fichas Apostadas', 'Ganancia/Perdida', 'Fichas Restantes']
index = pd.MultiIndex(levels=[[], [], []], codes=[[], [], []], names=['Partida', 'Ronda', 'Jugador'])
data = pd.DataFrame(columns=columnas, index=index)
partida = 1

def jugar():
    # Inicialización de jugadores
    global data
    global partida
    jugador1 = Jugador()
    crupier = Jugador()
    ronda = 0
    while jugador1.fichas > 0:
        ronda += 1
        fichas_iniciales = jugador1.fichas  # Guardar el número de fichas al comienzo de la ronda
        otra = ""
        i = 1
        imprimir_poco_a_poco("Tienes " + str(jugador1.fichas) + " fichas")
        print()
        while True:
            imprimir_poco_a_poco("¿Cuantas fichas quieres apostar? ")
            apuesta = input()
            if apuesta == "all in" or apuesta == "end":
                break
            try:
                apuesta = int(apuesta)
                if apuesta <= jugador1.fichas:
                    break
                imprimir_poco_a_poco("""El valor introducido debe ser numerico y menor o igual a las fichas que le quedan.
También puede introducir all in si quieres apostar todas tus fichas o end si quieres que acabe el juego""")
                print()
            except:
                imprimir_poco_a_poco("""El valor introducido debe ser numerico y menor o igual a las fichas que le quedan.
También puede introducir all in si quieres apostar todas tus fichas o end si quieres que acabe el juego""")
                print()
        
        if apuesta == "end":
            imprimir_poco_a_poco("Has acabado con " + str(jugador1.fichas) + " fichas")
            return
        elif apuesta == "all in":
            apuesta = jugador1.fichas
        apuesta = int(apuesta)
        jugador1.fichas -= apuesta
        as_crupier = False
        as_jugador1 = False

        while i > 0:
            # Turno del jugador
            if otra != "N":
                
                carta_jugador = sacar_carta()
                valor_carta, palo_carta = carta_jugador

                nombre_carta = obtener_nombre_carta(valor_carta)
                imprimir_poco_a_poco("Has sacado un " + str(nombre_carta) + " de " + str(palo_carta))
                print()

                if valor_carta > 10:
                    valor_carta = 10

                if valor_carta == 1:
                    as_jugador1 = True
                    valor_carta = 11

                jugador1.saca_carta(valor_carta)

                # Verificación de as para ajustar la mano si es necesario
                if sum(jugador1.mano) > 21 and as_jugador1:
                    for i in range(len(jugador1.mano)):
                        if jugador1.mano[i] == 11:
                            jugador1.mano[i] = 1
                if sum(jugador1.mano) > 21:
                    otra = "N"

                imprimir_poco_a_poco("Tu mano: "+ str(sum(jugador1.mano)))
                print()

                # Pregunta al jugador si desea otra carta (excepto en el primer turno)
                if i > 1 and sum(jugador1.mano) < 21:
                    while True:
                        imprimir_poco_a_poco("¿Quieres que se te reparta otra carta? S/N ")
                        otra = input().upper()
                        if otra == "END":
                            imprimir_poco_a_poco("Has acabado con " + str(jugador1.fichas) + " fichas")
                            return
                        if otra == "S" or otra == "N":
                            break
                        imprimir_poco_a_poco("Por favor, escribe S si quieres otra carta o N si no la quieres")
                        print()

                # Continuar al siguiente turno si el jugador desea otra carta
                if otra == "S":
                    continue

            # Turno del crupier
            
            carta_crupier = sacar_carta()
            valor_carta_crupier, palo_carta_crupier = carta_crupier

            nombre_carta_crupier = obtener_nombre_carta(valor_carta_crupier)
            imprimir_poco_a_poco("El crupier ha sacado un " + str(nombre_carta_crupier) + " de " + str(palo_carta_crupier))
            print()

            if valor_carta_crupier > 10:
                    valor_carta_crupier = 10

            if valor_carta_crupier == 1:
                as_crupier = True
                valor_carta_crupier = 11

            crupier.saca_carta(valor_carta_crupier)

            # Verificación de as para ajustar la mano si es necesario
            if sum(crupier.mano) > 21 and as_crupier:
                for i in range(len(crupier.mano)):
                        if crupier.mano[i] == 11:
                            crupier.mano[i] = 1
            
            imprimir_poco_a_poco("La mano del crupier: "+ str(sum(crupier.mano)))
            print()

            # Fin del turno del crupier si su mano supera 16
            if sum(crupier.mano) > 16:
                break

            i += 1

        # Resultado del juego
        if sum(jugador1.mano) == 21 and len(jugador1.mano) == 2:
            if sum(crupier.mano) == 21 and len(crupier.mano) == 2:
                imprimir_poco_a_poco("El crupier y tú habéis obtenido un blackjack, es un empate")
                jugador1.fichas += apuesta
            else:
                imprimir_poco_a_poco("Blackjack!!!, has conseguido un blackjack por lo que ganas el doble de fichas")
                jugador1.fichas += 4*apuesta
        elif sum(jugador1.mano) > 21:
            imprimir_poco_a_poco("Has perdido, tu mano es superior a 21")
        elif sum(crupier.mano) > 21:
            imprimir_poco_a_poco("Has ganado, la mano del crupier es superior a 21")
            jugador1.fichas += 2*apuesta
        elif sum(jugador1.mano) == sum(crupier.mano):
            imprimir_poco_a_poco("El crupier y tú tenéis la misma mano, es un empate")
            jugador1.fichas += apuesta
        elif sum(jugador1.mano) > sum(crupier.mano):
            imprimir_poco_a_poco("Has ganado, tu mano es superior a la del crupier")
            jugador1.fichas += 2*apuesta
        else:
            imprimir_poco_a_poco("Has perdido, tu mano es inferior a la del crupier")
        print()
        
        # Registrar datos de la ronda en el DataFrame
        data.loc[(partida, ronda, 'Jugador'), :] = [
            jugador1.mano[0], str(jugador1.mano[1:]), sum(jugador1.mano), apuesta, '', jugador1.fichas
        ] if len(jugador1.mano) >= 2 else [jugador1.mano[0], (), jugador1.mano[0], apuesta, '', jugador1.fichas]

        data.loc[(partida, ronda, 'Crupier'), :] = [
            crupier.mano[0], str(crupier.mano[1:]), sum(crupier.mano), pd.NA, '', pd.NA
        ] if len(crupier.mano) >= 2 else [crupier.mano[0], (), sum(crupier.mano), pd.NA, '', pd.NA]
        # Calcular ganancia/resta y actualizar la columna correspondiente
        ganancia_perdida = jugador1.fichas - fichas_iniciales
        data.loc[(partida, ronda, 'Jugador'), 'Ganancia/Perdida'] = f"+{ganancia_perdida}" if ganancia_perdida > 0 else f"{ganancia_perdida}"
        
        jugador1.reset_mano()
        crupier.reset_mano()



    imprimir_poco_a_poco("Te has quedado sin fichas")
    print() 
    while True:
        imprimir_poco_a_poco("¿Quieres jugar otra partida? S/N ")
        otrapartida = input().upper()
        if otrapartida == "END":
            imprimir_poco_a_poco("Has acabado con " + str(jugador1.fichas) + " fichas")
            return
        elif otrapartida == "N":
            break
        elif otrapartida == "S":
            partida += 1
            return jugar()
        imprimir_poco_a_poco("Por favor, escribe S si quieres otra partida o N si no la quieres")
        print()

# Llamada a la función para iniciar el juego.
jugar()
print(data)

