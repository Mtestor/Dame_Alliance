from pygame.constants import NOEVENT
import GameMap as gm
import Pawn as pw

def is_horizontal_pawn_capture(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    pawnC = gm.gameMap[posBegin].m_color
    if posBegin[0] == posEnd[0] and posBegin[1] + 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0], posBegin[1] + 1)] == None:
            return False
        if gm.gameMap[(posBegin[0], posBegin[1] + 1)].m_color != pawnC:
            return True
    elif posBegin[0] == posEnd[0] and posBegin[1] - 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0], posBegin[1] - 1)] == None:
                return False
        if gm.gameMap[(posBegin[0], posBegin[1] - 1)].m_color != pawnC:
            return True
    elif posBegin[0] + 2 == posEnd[0] and posBegin[1] == posEnd[1]:
        if gm.gameMap[(posBegin[0] + 1, posBegin[1])] == None:
            return False
        if gm.gameMap[(posBegin[0] + 1, posBegin[1])].m_color != pawnC:
            return True
    elif posBegin[0] - 2 == posEnd[0] and posBegin[1] == posEnd[1]:
        if gm.gameMap[(posBegin[0] - 1, posBegin[1])] == None:
            return False
        if gm.gameMap[(posBegin[0] - 1, posBegin[1])].m_color != pawnC:
            return True
    return False

def is_diagonal_pawn_capture(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    pawnC = gm.gameMap[posBegin].m_color
    if posBegin[0] + 2 == posEnd[0] and posBegin[1] + 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0] + 1, posBegin[1] + 1)] == None:
            return False
        if gm.gameMap[(posBegin[0] + 1, posBegin[1] + 1)].m_color != pawnC:
            return True
    elif posBegin[0] + 2 == posEnd[0] and posBegin[1] - 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0] + 1, posBegin[1] - 1)] == None:
            return False
        if gm.gameMap[(posBegin[0] + 1, posBegin[1] - 1)].m_color != pawnC:
            return True
    elif posBegin[0] - 2 == posEnd[0] and posBegin[1] - 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0] - 1, posBegin[1] - 1)] == None:
            return False
        if gm.gameMap[(posBegin[0] - 1, posBegin[1] - 1)].m_color != pawnC:
            return True
    elif posBegin[0] - 2 == posEnd[0] and posBegin[1] + 2 == posEnd[1]:
        if gm.gameMap[(posBegin[0] - 1, posBegin[1] + 1)] == None:
            return False
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

def capture_between_two_distance_cases(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    row = posBegin[0] + (posEnd[0] - posBegin[0]) // 2
    colomn = posBegin[1] + (posEnd[1] - posBegin[1]) // 2
    pawn = gm.gameMap[row, colomn]
    gm.gameMapState.remove_pawn(pawn.m_color, pawn.m_type)
    gm.gameMap[row, colomn] = None

def horizontal_pawn_capture(posBegin : tuple, posEnd : tuple):
    capture_between_two_distance_cases(posBegin, posEnd)

def diagonal_pawn_capture(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    capture_between_two_distance_cases(posBegin, posEnd)

def royal_pawn_capture(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    capture_between_two_distance_cases(posBegin, posEnd)