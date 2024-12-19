from juego.board import Board
from juego.exceptions import *
import sys



class Chess():
    def __init__(self):
        """
        Inicializa una nueva partida de ajedrez.

        Crea una instancia de la clase Board, establece el turno inicial en "White"
        y marca el juego como en curso.
        """
        self.__board__= Board()
        self.__turn__= "White"
       
    def is_playing():
        """
        Verifica si el juego está en curso.

        Returns:
            bool: True si el juego está en curso, False en caso contrario.
        """
        return True    
    
    def move(self, from_row, from_col, to_row, to_col):
        """
        Realiza un movimiento en el tablero de ajedrez.

        Verifica la validez del movimiento y actualiza el tablero. Si el movimiento
        resulta en la victoria de un equipo, termina el juego.

        Args:
            from_row (int): Fila de origen de la pieza.
            from_col (int): Columna de origen de la pieza.
            to_row (int): Fila de destino de la pieza.
            to_col (int): Columna de destino de la pieza.

        Raises:
            OriginInvalidMove: Si la posición de origen es inválida.
            EmptyPosition: Si no hay una pieza en la posición de origen.
            DestinationInvalidMove: Si la posición de destino es inválida.
            InvalidTurn: Si no es el turno del jugador que intenta mover la pieza.
            InvalidMove: Si el movimiento no es válido para la pieza.
        """
        piece = self.__board__.get_piece(from_row, from_col)

        if not piece:
            raise EmptyPosition()
        if not (0<=to_row<8 and 0<=to_col<8):
            raise DestinationInvalidMove()
        if not piece.get_color() == self.__turn__: 
            raise InvalidTurn()
        if not piece.valid_move_1(from_row, from_col, to_row, to_col) and not piece.valid_move_2(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        
        self.__board__.move(from_row, from_col, to_row, to_col)

        if self.winner():
          print(f"¡Felicidades! El ganador es el equipo: {self.turn}")
          return self.finish()
        
        self.change_turn()

      
        
    def tie(self):
        """
        Pregunta al usuario si desea terminar la partida y maneja la respuesta.

        Si el usuario confirma que desea terminar la partida, se llama a la función finish
        para terminar el juego.

        Returns:
            bool: Devuelve True si el usuario decide continuar jugando, y llama a finish() si el juego ha terminado.
        """
        import sys
        print("Estas seguro que desea terminar la partida?\n y/n")
        option = input()
        if option == "y":
            print("Gracias por jugar al ajedrez")
            return self.finish()
        else:
            print("Continua jugando")
            return True
        
    def winner(self):
        """
        Verifica si el equipo contrario ha sido derrotado.

        Returns:
            bool: True si todas las piezas del equipo contrario han sido eliminadas, False en caso contrario.
        """
        opponent_color="Black" if self.__turn__=="White" else "White"
        return self.__board__.count_pieces(opponent_color)==0

    
    @property
    def turn(self):
        """
        Obtiene el color del equipo que tiene el turno actual.

        Returns:
            str: El color del equipo que tiene el turno actual ("White" o "Black").
        """
        return self.__turn__
    
    def change_turn(self):
        """
        Cambia el turno al equipo contrario.
        """
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"
    
    def show_board(self):
        """
        Muestra el estado actual del tablero de ajedrez.

        Returns:
            str: Una representación en cadena del tablero de ajedrez.
        """
        return str(self.__board__)
    
    def finish(self):
        """
        Termina el juego de ajedrez.

        Llama a sys.exit() para terminar el juego y salir del programa.

        Returns:
            sys.exit() terminado la ejecucion del programa.
        """
        return sys.exit()
 




