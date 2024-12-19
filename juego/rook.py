from juego.piece import Piece

class Rook(Piece):
    def __init__(self,color,board):
        super().__init__(color,board)
    
      
    White_str = "♜"
    Black_str = "♖"

    def valid_positions_rook(self,from_row,from_col,to_row,to_col):

        """
        Valida el movimiento del rook.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        return self.valid_positions_general(from_row,from_col,to_row,to_col)