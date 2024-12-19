from juego.piece import Piece

class Bishop(Piece):
    def __str__(self):
        """
        Devuelve una representación en cadena del Alfil.

        Returns:
            str: "♝" si el Alfil es blanco, "♗" si es negro.
        """
        if self.__color__ == "White":
            return "♝"
        else:
            return "♗"
    
    

    def valid_positions_bishop(self,from_row,from_col,to_row,to_col):

        """
        Valida el movimiento del bishop.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """

        return self.valid_positions_general(from_row,from_col,to_row,to_col)
        
    
    
