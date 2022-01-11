import Pawn as pw

class PlayerState:

    def __init__(self, color : pw.PawnColor):
        self.m_isClicked = False
        self.m_color = color
        self.m_isPawnChoosed = False
        self.m_pawnPos = None