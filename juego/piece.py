
class Piece:
    def __init__(self,color,board):
        """
        Inicializa una nueva pieza de ajedrez.

        Args:
            color (str): El color de la pieza ("Black" o "White").
            board (Board): La instancia del tablero en la que se encuentra la pieza.
        """
        self.__color__ = color
        self.__board__ = board
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la pieza.

        Returns:
            str: Una cadena que representa la pieza, incluyendo su color y tipo.
        """
        if self.__color__== "White":
            return self.White_str
        else:
            return self.Black_str
        
    def get_color(self):
        """
        Obtiene el color de la pieza.

        Returns:
            str: El color de la pieza ("Black" o "White").
        """
        return self.__color__
    
    def valid_move_1(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para la pieza.

        Este método debe ser implementado por las subclases específicas de cada tipo de pieza.

        Args:
            from_row (int): La fila de origen de la pieza.
            from_col (int): La columna de origen de la pieza.
            to_row (int): La fila de destino de la pieza.
            to_col (int): La columna de destino de la pieza.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        from juego.knight import Knight
        from juego.king import King
        from juego.pawn import Pawn
        ptr_funcion = None
        if isinstance(self, Pawn):
            ptr_funcion = self.valid_positions_pawn
        if isinstance(self, Knight):
            ptr_funcion = self.valid_positions_knight
        if isinstance(self, King):
            ptr_funcion = self.valid_positions_king
        if ptr_funcion is not None:
            return ptr_funcion(from_row, from_col, to_row, to_col)
        return False
        
    def valid_move_2(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para la pieza.

        Este método debe ser implementado por las subclases específicas de cada tipo de pieza.

        Args:
            from_row (int): La fila de origen de la pieza.
            from_col (int): La columna de origen de la pieza.
            to_row (int): La fila de destino de la pieza.
            to_col (int): La columna de destino de la pieza.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
    
        from juego.rook import Rook
        from juego.bishop import Bishop
        from juego.queen import Queen
        if isinstance(self, Rook):
            return self.valid_positions_rook(from_row, from_col, to_row, to_col)
        elif isinstance(self, Bishop):
            return self.valid_positions_bishop(from_row, from_col, to_row, to_col)
        elif isinstance(self, Queen):
            return self.valid_positions_queen(from_row, from_col, to_row, to_col)
        else:
            return False
    




    # ##################################
   
    def possible_positions_linear(self, row, col, increments, stop, step):
        """
        Calcula las posiciones posibles para las piezas que se mueven en una dirección lineal.

        Args:
            row (int): La fila de inicio.
            col (int): La columna de inicio.
            increments (tuple): Tupla con los incrementos (kr, kc) para filas y columnas.
            stop (int): El límite donde el movimiento debe detenerse.
            step (int): El paso a seguir en cada iteración.

        Returns:
            list: Lista de tuplas con las posiciones posibles.
        """
        kr, kc = increments
        possibles = []

        for i in range(1, 8):
            next_row, next_col = row + kr * i, col + kc * i
            if not (0 <= next_row < 8 and 0 <= next_col < 8):
                break
            if self.check_and_add_position(possibles, next_row, next_col):
                break  

            if stop and (next_row == stop or next_col == stop):
                break

        return possibles

    def possible_positions_vertical(self, row, col, kr, stop, step):
        """
        Calcula las posiciones posibles para las piezas que hagan movimientos verticales.

        Args:
            row (int): La fila actual de la pieza.
            col (int): La columna actual de la pieza.
            kr (int): La cantidad de filas a mover.
            stop (int): La fila de parada.
            step (int): El paso a seguir.

        Returns:
            list: Lista de tuplas con las posiciones verticales posibles.
        """
        return self.possible_positions_linear(row, col, (kr, 0), stop, step)

    def possible_positions_horizontal(self, row, col, kc, stop, step):
        """
        Calcula las posiciones posibles para las piezas que hagan movimientos horizontales.

        Args:
            row (int): La fila actual de la pieza.
            col (int): La columna actual de la pieza.
            kc (int): La cantidad de columnas a mover.
            stop (int): La columna de parada.
            step (int): El paso a seguir.

        Returns:
            list: Lista de tuplas con las posiciones horizontales posibles.
        """
        return self.possible_positions_linear(row, col, (0, kc), stop, step)
    
  

    def possible_positions_diagonal(self,row,col,kr,kc):
        """
        Calcula las posiciones posibles para las piezas que hagan movimientos diagonales.

        Args:
            row (int): La fila actual de la pieza.
            col (int): La columna actual del pieza.
            kr (int): La cantidad de filas a mover.
            kc (int): La cantidad de columnas a mover.

        Returns:
            list: Lista de tuplas con las posiciones diagonales posibles.
        """
        possibles=[]
        next_row,next_col=row+kr,col+kc
        while 0<= next_row<8 and 8>next_col>=0:
            if self.check_and_add_position(possibles, next_row, next_col):
                break  
            next_row +=kr
            next_col +=kc
        return possibles
    
    
    def check_and_add_position(self, possibles, row, col):
        """
        Verifica si hay una pieza en la posición dada y añade la posición a posibles si es válida.

        Args:
            possibles (list): Lista de posiciones posibles.
            row (int): La fila a verificar.
            col (int): La columna a verificar.

        Returns:
            bool: True si se debe detener la iteración, False si no.
        """
        other_piece = self.__board__.get_piece(row, col)
        if other_piece is not None:
            if other_piece.__color__ != self.__color__:
                possibles.append((row, col))
            return True  # Se debe detener la iteración
        possibles.append((row, col))
        return False  # Se puede continuar


    #metodo para movimiento compartido unitario.

    def possible_positions_one_move(self, row, col, kr, kc):
        """
        Calcula las posiciones posibles para los movimientos de una unidad en cualquier direccion.

        Args:
            row (int): La fila actual del rey.
            col (int): La columna actual del rey.
            kr (int): La cantidad de filas a mover.
            kc (int): La cantidad de columnas a mover.

        Returns:
            list: Lista de tuplas con las posiciones posibles en un movimiento.
        """
        possibles = []
        new_row = row + kr
        new_col = col + kc
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            other_piece = self.__board__.get_piece(new_row, new_col)
            if other_piece is not None and other_piece.__color__ != self.__color__:
                possibles.append((new_row, new_col))
            elif other_piece is None:
                possibles.append((new_row, new_col))
        return possibles
    
################
    ##valid positions repeat rook

    def move_rook(self,from_row, from_col):
        """
        Calcula las posiciones posibles para los movimientos del rook.

        Args:   
            from_row (int): La fila de origen.
            from_col (int): La columna de origen.
        
        Returns:
            list: Lista de tuplas con las posiciones posibles para el rook.
        """
        possible=(self.possible_positions_horizontal(from_row,from_col,1,8,1)+self.possible_positions_vertical(from_row,from_col,1,8,1)+self.possible_positions_horizontal(from_row,from_col,-1,-1,-1)+self.possible_positions_vertical(from_row,from_col,-1,-1,-1))
        return possible


    def valid_positions_general(self, from_row, from_col, to_row, to_col):
        from juego.knight import Knight
        from juego.king import King
        from juego.pawn import Pawn
        from juego.rook import Rook
        from juego.bishop import Bishop
        from juego.queen import Queen
        """
        Verifica si un movimiento es válido para el rook, queen y bishop de ajedrez.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """

        possibles = []

        if isinstance(self, Rook):
            straight = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            possibles = [pos for dx, dy in straight for pos in self.possible_positions_linear(from_row, from_col, (dx, dy), None, 1)]
        elif isinstance(self, Bishop) or isinstance(self, Queen):
            diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            possibles = [pos for dx, dy in diagonals for pos in self.possible_positions_diagonal(from_row, from_col, dx, dy)]

            if isinstance(self, Queen):
                possibles += self.move_rook(from_row, from_col)

        if possibles is not None:
            return (to_row, to_col) in possibles

        