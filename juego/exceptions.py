#movimientos invalidados
class InvalidMove(Exception):
    pass
#movimiento invalidado:desde el origen
class OriginInvalidMove(InvalidMove):
    pass
#movimiento invalidado:hacia el destino
class DestinationInvalidMove(InvalidMove):
    pass
class EmptyPosition(InvalidMove):
    pass
class InvalidTurn(InvalidMove):
    pass

class InvalidMoveNoPiece(InvalidMove):
    pass

class InvalidMoveRookMove(InvalidMove):
    pass

