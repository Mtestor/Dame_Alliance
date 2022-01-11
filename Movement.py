from typing import Tuple

import Pawn as pw
import PawnMovePredicat as pwmp
import GameMap as gm

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

def is_pos_free(pos : Tuple):
    if gm.gameMap[pos] == None:
        return True
    else:
        return False

def is_movement_respect_predicat(posBegin : Tuple, posEnd : Tuple, pawnT : pw.PawnType):
    for predicat in pwmp.pawnMovePredicat[pawnT]:
        if predicat(posBegin, posEnd):
            return True

def is_movement_legal(posBegin : Tuple, posEnd : Tuple):
    if not is_pos_in_border(posBegin):
        return False
    if is_pos_free(posBegin):
        return False
    if not is_pos_in_border(posEnd):
        return False
    if is_pos_free(posEnd):
        return False
    pawn = gm.gameMap[posBegin]
    if is_movement_respect_predicat(posBegin, posEnd, pawn.m_type):
        return True
    return False