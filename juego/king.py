from juego.piece import Piece

class King(Piece):
   

    White_str = "♚"
    Black_str = "♔"

    
    def valid_positions_king(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para el rey.
    
        Args:
            from_row (int): La fila de origen del rey.
            from_col (int): La columna de origen del rey.
            to_row (int): La fila de destino del rey.
            to_col (int): La columna de destino del rey.
    
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        directions = [
            (1, 1), (1, -1), (-1, 1), (-1, -1),  # Diagonales
            (0, 1), (0, -1), (1, 0), (-1, 0)     # Vertical y horizontal
        ]
        
        possible_positions = []
        for d_row, d_col in directions:
            possible_positions += self.possible_positions_one_move(from_row, from_col, d_row, d_col)
        return (to_row, to_col) in possible_positions
    