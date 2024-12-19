from juego.rook import Rook
from juego.knight import Knight
from juego.bishop import Bishop
from juego.queen import Queen
from juego.king import King 
from juego.pawn import Pawn
from juego.piece import Piece 
from juego.exceptions import OriginInvalidMove
class Board():
    def __init__(self,for_test = False):
        """
        Inicializa un nuevo tablero de ajedrez.

        Crea una matriz de 8x8 para representar el tablero y coloca las piezas en sus posiciones iniciales,
        a menos que se especifique lo contrario para pruebas.

        Args:
            for_test (bool): Si es True, no coloca las piezas en el tablero para facilitar las pruebas.
        """
        #los indices son E8 por ejemplo. Va de 1-8 y a-h
        self.__positions__= []
        #LLenado de matriz. Primero se crean 8 filas y luego 8 columnas
        for _ in range(8):
            col=[]
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            
            self.__positions__[0][0]= Rook("Black",self) #black
            self.__positions__[7][7]= Rook("White",self) #white
            self.__positions__[0][7]= Rook("Black",self) #black
            self.__positions__[7][0]= Rook("White",self) #White
            self.__positions__[0][1]= Knight("Black",self)
            self.__positions__[0][6]= Knight("Black",self)
            self.__positions__[7][1]= Knight("White",self)
            self.__positions__[7][6]= Knight("White",self)
            self.__positions__[0][2]= Bishop("Black",self)
            self.__positions__[0][5]= Bishop("Black",self)
            self.__positions__[7][2]= Bishop("White",self)
            self.__positions__[7][5]= Bishop("White",self)
            self.__positions__[0][3]= Queen("Black",self)
            self.__positions__[7][3]= Queen("White",self)
            self.__positions__[0][4]= King("Black",self)
            self.__positions__[7][4]= King("White",self)

            for i in range(8):
                self.__positions__[1][i]= Pawn("Black",self)
                self.__positions__[6][i]= Pawn("White",self)

    def __str__(self):
        """
        Devuelve una representación en cadena del tablero de ajedrez.

        Returns:
            str: Una cadena que representa el estado actual del tablero de ajedrez.
        """
        board_str = "  0 1 2 3 4 5 6 7\n"  # Índice superior
        for i, row in enumerate(self.__positions__):
            board_str += f"{i} "  # Índice izquierdo
            for cell in row:
                if cell is not None:
                    board_str += str(f"{cell} ")
                else:
                    board_str += "  "
            board_str += "\n"
        return board_str
    
    def count_pieces(self, color):
        """
        Cuenta el número de piezas de un color específico en el tablero.

        Args:
            color (str): El color de las piezas a contar ("Black" o "White").

        Returns:
            int: El número de piezas del color especificado en el tablero.
        """
        count = 0
        for row in self.__positions__:
            for piece in row:
                if piece is not None and piece.get_color() == color:
                    count += 1
        return count

    def get_piece(self,row,col):
        """
        Obtiene la pieza en la posición especificada del tablero.

        Args:
            row (int): La fila de la posición.
            col (int): La columna de la posición.

        Returns:
            Piece: La pieza en la posición especificada, o None si no hay ninguna pieza.
        """

        if not (0 <= row < 8 and 0 <= col < 8):
         raise OriginInvalidMove()
        
        return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece):
        """
        Coloca una pieza en la posición especificada del tablero.

        Args:
            row (int): La fila de la posición.
            col (int): La columna de la posición.
            piece (Piece): La pieza a colocar en la posición especificada.
        """
        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):
        """
        Mueve una pieza de una posición a otra en el tablero.

        Args:
            from_row (int): La fila de origen de la pieza.
            from_col (int): La columna de origen de la pieza.
            to_row (int): La fila de destino de la pieza.
            to_col (int): La columna de destino de la pieza.
        """
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)
    