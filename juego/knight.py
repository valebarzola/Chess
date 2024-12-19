from juego.piece import Piece

class Knight(Piece):

    White_str = "♞"
    Black_str = "♘"
        
    
    def valid_positions_knight(self,from_row,from_col,to_row,to_col):
        """
        Valida el movimiento del knight.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """


        possible=(self.possible_positions_one_move(from_row,from_col,2,1)+self.possible_positions_one_move(from_row,from_col,2,-1)+self.possible_positions_one_move(from_row,from_col,1,2)+self.possible_positions_one_move(from_row,from_col,1,-2)+self.possible_positions_one_move(from_row,from_col,-2,1)+self.possible_positions_one_move(from_row,from_col,-2,-1)+self.possible_positions_one_move(from_row,from_col,-1,2)+self.possible_positions_one_move(from_row,from_col,-1,-2))

        return (to_row, to_col) in possible