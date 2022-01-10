from typing import Tuple
from Pawn import *
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