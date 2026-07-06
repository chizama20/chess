from dataclasses import dataclass
from typing import Optional
from typing import Tuple
from piece import PieceType

Square = Tuple[int, int]

@dataclass
class Move:
    from_square: Square
    to_square: Square
    promotion: Optional[PieceType] = None
    is_castle: bool = False
    is_en_passant: bool = False