import Pawn as pw

class PlayerState:

    def __init__(self, color : pw.PawnColor):
        self.m_isClicked = False
        self.m_color = color
        self.m_isPawnChoosed = False
        self.m_pawnPos = None
        self.m_hasMoved = False
        self.m_hasCaptured = False
        self.m_score = 0

    def reset(self, color : pw.PawnColor):
        self.__init__(color)