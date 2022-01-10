from Pawn import Pawn, PawnColor, PawnType
import Movement
import GameMap as gm

def is_pos_inside_border():
    p = (gm.ROW_MAX, gm.COLOMN_MAX)
    is_in_limit = Movement.is_pos_in_border(p)
    assert(is_in_limit == True and "position p should be inside the border")

def is_pos_outside_border():
    p = (gm.ROW_MAX + 1, -1)
    is_in_limit = Movement.is_pos_in_border(p)
    assert(is_in_limit == False and "position p should be outside the border")

is_pos_inside_border()
is_pos_outside_border()