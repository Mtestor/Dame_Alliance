from numpy import full
from Pawn import *

ROW_MAX = 7
COLOMN_MAX = 7

gameMap = full((ROW_MAX + 1, COLOMN_MAX + 1), None)

def init():
    for k in range(1, 7):
        gameMap[1, k] = Pawn(PawnColor.BLACK, PawnType.HORIZONTAL)
        gameMap[2, k] = Pawn(PawnColor.BLACK, PawnType.DIAGONAL)

        gameMap[5, k] = Pawn(PawnColor.WHITE, PawnType.DIAGONAL)
        gameMap[6, k] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)