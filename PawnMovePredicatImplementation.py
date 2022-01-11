
def is_horizontal_pawn_deplacement(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    if posBegin[0] == posEnd[0] and posBegin[1] + 1 == posEnd[1]:
        return True
    if posBegin[0] == posEnd[0] and posBegin[1] - 1 == posEnd[1]:
        return True
    if posBegin[0] + 1 == posEnd[0] and posBegin[1] == posEnd[1]:
        return True
    if posBegin[0] - 1 == posEnd[0] and posBegin[1] == posEnd[1]:
        return True
    return False

def is_diagonal_pawn_deplacement(posBegin : tuple, posEnd : tuple):
    # pos[0] is row and pos[1] is colomn because of gm.gameMap
    if posBegin[0] + 1 == posEnd[0] and posBegin[1] + 1 == posEnd[1]:
        return True
    if posBegin[0] - 1 == posEnd[0] and posBegin[1] - 1 == posEnd[1]:
        return True
    if posBegin[0] + 1 == posEnd[0] and posBegin[1] - 1 == posEnd[1]:
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