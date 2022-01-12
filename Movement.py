from typing import Tuple

import Pawn as pw
import PawnMovePredicat as pwmp
import GameMap as gm
import PawnCapture as pwc

def is_pos_in_border(pos : Tuple):
    if pos[0] < 0:
        return False
    if pos[0] > gm.ROW_MAX:
        return False
    if pos[1] < 0:
        return False
    if pos[1] > gm.COLOMN_MAX:
        return False
    return True

# @pre pos is a valid position in gm.gameMap
def is_pos_free(pos : Tuple):
    if gm.gameMap[pos] == None:
        return True
    else:
        return False

# @pre there is a pawn at posBegin
def is_movement_respect_predicat(posBegin : Tuple, posEnd : Tuple):
    pawn = gm.gameMap[posBegin]
    for predicat in pwmp.pawnMovePredicat[pawn.m_type]:
        if predicat(posBegin, posEnd):
            return True

def are_position_correct(posBegin : tuple, posEnd : tuple):
    if not is_pos_in_border(posBegin):
        return False
    if is_pos_free(posBegin):
        return False
    if not is_pos_in_border(posEnd):
        return False
    if not is_pos_free(posEnd):
        return False
    return True

def is_movement_legal(posBegin : Tuple, posEnd : Tuple):
    if not are_position_correct(posBegin, posEnd):
        return False
    if is_movement_respect_predicat(posBegin, posEnd):
        return True
    return False

def which_capture(posBegin : Tuple, posEnd : Tuple):
    if not are_position_correct(posBegin, posEnd):
        return None
    pawn = gm.gameMap[posBegin]
    for captureCouple in pwc.pawnCapture[pawn.m_type]:
        if captureCouple[0](posBegin, posEnd):
            return captureCouple[1]
    return None

def move_pawn_to(posBegin : tuple, posEnd : tuple):
    gm.gameMap[posEnd] = gm.gameMap[posBegin]
    if (gm.gameMap[posEnd].m_color == pw.PawnColor.BLACK and posEnd[0] == gm.ROW_MAX or \
       gm.gameMap[posEnd].m_color == pw.PawnColor.WHITE and posEnd[0] == 0):
        gm.gameMap[posEnd].m_type = pw.PawnType.ROYAL
        gm.gameMapState.add_royal_pawn(gm.gameMap[posEnd].m_color)
    gm.gameMap[posBegin] = None

def pawn_capture(posBegin : tuple, posEnd : tuple, capture):
    move_pawn_to(posBegin, posEnd)
    capture(posBegin, posEnd)