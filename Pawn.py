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

    def to_json(self) -> dict:
        return {
            "color" : str(self.m_color),
            "type"  : str(self.m_type)
        }
    
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

def pawnType_from_json(jsoned) -> PawnType:
    if jsoned == 'PawnType.ROYAL':
        return PawnType.ROYAL
    if jsoned == 'PawnType.HORIZONTAL':
        return PawnType.HORIZONTAL
    if jsoned == 'PawnType.DIAGONAL':
        return PawnType.DIAGONAL
    assert(False and "There is no other PawnType")

def pawnColor_from_json(jsoned) -> PawnColor:
    if jsoned == 'PawnColor.BLACK':
        return PawnColor.BLACK
    if jsoned == 'PawnColor.WHITE':
        return PawnColor.WHITE
    if jsoned == 'PawnColor.NONE':
        return PawnColor.NONE
    assert(False and "There is no other PawnColor")

def pawn_from_json(jsoned):
    return Pawn(pawnColor_from_json(jsoned['color']), pawnType_from_json(jsoned['type']))