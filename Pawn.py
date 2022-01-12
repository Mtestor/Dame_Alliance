from enum import IntEnum

class PawnColor(IntEnum):
    NONE = 0
    WHITE = 1
    BLACK = 2

class PawnType(IntEnum):
    ROYAL = 0
    HORIZONTAL = 1
    DIAGONAL = 2

class Pawn:
    """ Class that represent a pawn"""

    def __init__(self, color = PawnColor.NONE, type = PawnType.ROYAL):
        self.m_color = color
        self.m_type = type
    
def inv_pawnColor(pawnColor : PawnColor):
    if pawnColor == PawnColor.BLACK:
        return PawnColor.WHITE
    if pawnColor == PawnColor.WHITE:
        return PawnColor.BLACK
    return pawnColor

def inv_pawnType(pawnType : PawnType):
    if pawnType == PawnType.DIAGONAL:
        return PawnType.HORIZONTAL
    if pawnType == PawnType.HORIZONTAL:
        return PawnType.DIAGONAL
    return pawnType