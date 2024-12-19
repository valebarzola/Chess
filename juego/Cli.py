
from juego.chess import Chess
from juego.exceptions import *


def main():
    """
    Inicia el juego de ajedrez y controla el bucle principal del juego.

    Crea una instancia de la clase Chess y llama a la función play en un bucle
    mientras el juego esté en curso.
    """
    chess = Chess()
    while Chess.is_playing():
        play(chess)

print("Bienvenido al juego de ajedrez. Para empezar a jugar coloca el numero de fila y columna de una pieza para moverla. Para terminar el juego puedes escribir STOP en cualquier momento")

def play(chess):
    """
    Controla un turno del juego de ajedrez.

    Muestra el tablero actual, solicita al usuario las coordenadas de la pieza a mover
    y las coordenadas de destino. Si el usuario escribe 'STOP', se llama a la función tie
    para terminar el juego.

    Args:
        chess (Chess): Una instancia de la clase Chess que representa el estado actual del juego.

    Returns:
        bool: Devuelve True si el juego continúa, False si el juego ha terminado.
    """
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)

        from_row = input("From row ")
        if from_row.lower()=="stop":
            return chess.tie() 
        
        from_col = input("From col ")
        if from_col.lower()=="stop":
            return chess.tie()
        
        to_row = input("To row ")
        if to_row.lower()=="stop":
            return chess.tie()
        
        to_col = input("To col ")
        if to_col.lower()=="stop":
            return chess.tie()
        
        from_row = int(from_row)
        from_col = int(from_col)
        to_row = int(to_row)
        to_col = int(to_col)

        chess.move(from_row, from_col, to_row, to_col)
        


#aca ponemos la llamada a las excepciones de menor a mayor jerarquia
    except OriginInvalidMove as e:
        print("El Movimiento de la fila o columna origen es invalido")
    except EmptyPosition as e:
        print("No hay ninguna pieza en la posición de origen")
    except DestinationInvalidMove as e:
        print("El Movimiento de la fila o columna destino es invalido")
    except InvalidTurn as e:
        print("No es tu turno")
    except InvalidMove as e:
        print("Movimiento inválido")
    except Exception as e:
        print("Error inesperado")

    

if __name__ == "__main__":
    main()


