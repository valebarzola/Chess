from juego.piece import Piece

class Queen(Piece):
    
    White_str = "♛"
    Black_str = "♕"

    def valid_positions_queen(self,from_row,from_col,to_row,to_col):
        """
            Valida el movimiento de la reina.

            Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

            Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        return self.valid_positions_general(from_row,from_col,to_row,to_col)

        
