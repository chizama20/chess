from enum import Enum
from collections import namedtuple

class Color(Enum):
    WHITE = 0
    BLACK = 1


class PieceType(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6


Piece = namedtuple('Piece', ['PieceType' 'Color'])
