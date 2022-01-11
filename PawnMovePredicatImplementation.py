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

def is_horizontal_pawn_capture(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    pawnC = gm.gameMap[posBegin].m_color
    if posBegin[0] == posEnd[0] and posBegin[1] + 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0], posBegin[1] + 1)].m_color != pawnC:
            return True
    if posBegin[0] == posEnd[0] and posBegin[1] - 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0], posBegin[1] - 1)].m_color != pawnC:
            return True
    if posBegin[0] + 2 == posEnd[0] and posBegin[1] == posEnd[1]:
        if gm.gameMap[(posBegin[0] + 1, posBegin[1])].m_color != pawnC:
            return True
    if posBegin[0] - 2 == posEnd[0] and posBegin[1] == posEnd[1]:
        if gm.gameMap[(posBegin[0] - 1, posBegin[1])].m_color != pawnC:
            return True
    return False

def is_diagonal_pawn_capture(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    pawnC = gm.gameMap[posBegin].m_color
    if posBegin[0] + 2 == posEnd[0] and posBegin[1] + 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0] + 1, posBegin[1] + 1)].m_color != pawnC:
            return True
    if posBegin[0] + 2 == posEnd[0] and posBegin[1] - 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0] + 1, posBegin[1] - 1)].m_color != pawnC:
            return True
    if posBegin[0] - 2 == posEnd[0] and posBegin[1] - 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0] - 1, posBegin[1] - 1)].m_color != pawnC:
            return True
    if posBegin[0] - 2 == posEnd[0] and posBegin[1] + 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0] - 1, posBegin[1] + 1)].m_color != pawnC:
            return True
    return False

def is_royal_pawn_capture(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    if is_horizontal_pawn_capture(posBegin, posEnd):
        return True
    if is_diagonal_pawn_capture(posBegin, posEnd):
        return True
    return False