from Pawn import Pawn, PawnColor, PawnType
import Movement
import GameMap as gm

def is_pos_inside_border():
    p = (gm.ROW_MAX, gm.COLOMN_MAX)
    isInLimit = Movement.is_pos_in_border(p)
    assert(isInLimit == True and "position p should be inside the border")

def is_pos_outside_border():
    p = (gm.ROW_MAX + 1, -1)
    isInLimit = Movement.is_pos_in_border(p)
    assert(isInLimit == False and "position p should be outside the border")

def is_pos_without_pawn():
    p = (2, 2)
    pawn = gm.gameMap[p]
    gm.gameMap[p] = None
    isWithoutPawn = Movement.is_pos_free(p)
    gm.gameMap[p] = pawn
    assert(isWithoutPawn == True and "They shouldn't have a pawn at position p")

def is_pos_with_pawn():
    p = (2, 2)
    pawn = gm.gameMap[p]
    gm.gameMap[p] = Pawn()
    isWithoutPawn = Movement.is_pos_free(p)
    gm.gameMap[p] = pawn
    assert(isWithoutPawn == False and "They should have a pawn at position p")


is_pos_inside_border()
is_pos_outside_border()
is_pos_without_pawn()
is_pos_with_pawn()
