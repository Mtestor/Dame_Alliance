import GameMap as gm
import Pawn as pw

def is_diagonal_pawn_deplacement(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    pawnC = gm.gameMap[posBegin].m_color
    if posBegin[0] == posEnd[0] and posBegin[1] + 1 == posEnd[1]:
        return True
    if posBegin[0] == posEnd[0] and posBegin[1] - 1 == posEnd[1]:
        return True
    if posBegin[0] + 1 == posEnd[0] and posBegin[1] == posEnd[1]:
        if pawnC == pw.PawnColor.WHITE:
            return False
        return True
    if posBegin[0] - 1 == posEnd[0] and posBegin[1] == posEnd[1]:
        if pawnC == pw.PawnColor.BLACK:
            return False
        return True
    return False

def is_horizontal_pawn_deplacement(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    pawnC = gm.gameMap[posBegin].m_color
    if pawnC == pw.PawnColor.BLACK:
        if posBegin[0] + 1 == posEnd[0] and posBegin[1] + 1 == posEnd[1]:
            return True
        if posBegin[0] + 1 == posEnd[0] and posBegin[1] - 1 == posEnd[1]:
            return True
    if pawnC == pw.PawnColor.WHITE:
        if posBegin[0] - 1 == posEnd[0] and posBegin[1] - 1 == posEnd[1]:
            return True
        if posBegin[0] - 1 == posEnd[0] and posBegin[1] + 1 == posEnd[1]:
            return True
    return False

def is_royal_pawn_deplacement(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    if is_horizontal_pawn_deplacement(posBegin, posEnd):
        return True
    if is_diagonal_pawn_deplacement(posBegin, posEnd):
        return True
    return False