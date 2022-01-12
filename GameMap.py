from numpy import full
from Pawn import *

ROW_MAX = 7
COLOMN_MAX = 7

gameMap = full((ROW_MAX + 1, COLOMN_MAX + 1), None)

class GameMapState:
    """Hold the state of the gameMap"""
    def __init__(self):
        self.m_BlackNormalPawn = 12
        self.m_BlackRoyalPawn = 0
        self.m_WhiteNormalPawn = 12
        self.m_WhiteRoyalPawn = 0
        self.m_BlackScore = 0
        self.m_WhiteScore = 0

    def number_pawn(self, pawnColor : PawnColor):
        if pawnColor == PawnColor.BLACK:
            return self.m_BlackNormalPawn + self.m_BlackRoyalPawn
        else:
            return self.m_WhiteNormalPawn + self.m_WhiteRoyalPawn

    def add_royal_pawn(self, pawnColor : PawnColor):
        if pawnColor == PawnColor.BLACK:
            self.m_BlackRoyalPawn += 1
            self.m_BlackNormalPawn -= 1
        else:
            self.m_WhiteRoyalPawn += 1
            self.m_WhiteNormalPawn -= 1

    def add_score(self, pawnColor : PawnColor, points):
        if pawnColor == PawnColor.BLACK:
            self.m_BlackScore += points
        else:
            self.m_WhiteScore += points
    
    def remove_pawn(self, pawnColor : PawnColor, pawnType : PawnType):
        if pawnColor == PawnColor.BLACK:
            if pawnType == PawnType.ROYAL:
                self.m_BlackRoyalPawn -= 1
            else:
                self.m_BlackNormalPawn -= 1
        else:
            if pawnType == PawnType.ROYAL:
                self.m_WhiteRoyalPawn -= 1
            else:
                self.m_WhiteNormalPawn -= 1

    def reset(self):
        self.__init__

gameMapState = GameMapState()

def init():
    for k in range(1, 7):
        gameMap[1, k] = Pawn(PawnColor.BLACK, PawnType.HORIZONTAL)
        gameMap[2, k] = Pawn(PawnColor.BLACK, PawnType.DIAGONAL)

        gameMap[5, k] = Pawn(PawnColor.WHITE, PawnType.DIAGONAL)
        gameMap[6, k] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    
    gameMapState.reset()