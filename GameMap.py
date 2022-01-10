from numpy import full
from Pawn import *

ROW_MAX = 7
COLOMN_MAX = 7

gameMap = full((ROW_MAX + 1, COLOMN_MAX + 1), None)

def init():
    gameMap[1,1:7] = Pawn(PawnColor.BLACK, PawnType.HORIZONTAL)
    gameMap[2,1:7] = Pawn(PawnColor.BLACK, PawnType.DIAGONAL)

    gameMap[5,1:7] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    gameMap[6,1:7] = Pawn(PawnColor.WHITE, PawnType.DIAGONAL)