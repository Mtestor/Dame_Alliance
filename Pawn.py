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

    def __init__(self, color : PawnColor, type : PawnType):
        self.m_color = color
        self.m_type = type
    
    def __init__(self):
        self.m_color = PawnColor.NONE
        self.m_type = PawnType.ROYAL