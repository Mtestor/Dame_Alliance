from Pawn import Pawn, PawnColor, PawnType
import PawnMovePredicatImplementation as pwmpi
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

def is_diagonal_pawn_movement_predicat_to_north_correct():
    pBeg = (2, 2)
    pEnd = (1, 2)
    gm.gameMap[pBeg] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_diagonal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == True and "The diagonal pawn should be able move to one case north")

def is_diagonal_pawn_movement_predicat_to_south_correct():
    pBeg = (2, 2)
    pEnd = (3, 2)
    gm.gameMap[pBeg] = Pawn(PawnColor.BLACK, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_diagonal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == True and "The diagonal pawn should be able move to one case south")

def is_diagonal_pawn_movement_predicat_to_east_correct():
    pBeg = (2, 2)
    pEnd = (2, 3)
    gm.gameMap[pBeg] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_diagonal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == True and "The diagonal pawn should be able move to one case east")

def is_diagonal_pawn_movement_predicat_to_west_correct():
    pBeg = (2, 2)
    pEnd = (2, 1)
    gm.gameMap[pBeg] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_diagonal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == True and "The diagonal pawn should be able move to one case west")

def is_diagonal_pawn_movement_predicat_to_wrong_pos_correct():
    pBeg = (2, 2)
    pEnd = (1, 1)
    gm.gameMap[pBeg] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_diagonal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == False and "The diagonal pawn shouldn't be able move to one case north-west")

def is_horizontal_pawn_movement_predicat_to_southwest_correct():
    pBeg = (2, 2)
    pEnd = (3, 1)
    gm.gameMap[pBeg] = Pawn(PawnColor.BLACK, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_horizontal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == True and "The horizontal pawn should be able move to one case south-west")

def is_horizontal_pawn_movement_predicat_to_northwest_correct():
    pBeg = (2, 2)
    pEnd = (1, 1)
    gm.gameMap[pBeg] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_horizontal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == True and "The horizontal pawn should be able move to one case north-west")

def is_horizontal_pawn_movement_predicat_to_northeast_correct():
    pBeg = (2, 2)
    pEnd = (1, 3)
    gm.gameMap[pBeg] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_horizontal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == True and "The horizontal pawn should be able move to one case north-east")

def is_horizontal_pawn_movement_predicat_to_southeast_correct():
    pBeg = (2, 2)
    pEnd = (3, 3)
    gm.gameMap[pBeg] = Pawn(PawnColor.BLACK, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_horizontal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == True and "The horizontal pawn should be able move to one case south-east")

def is_horizontal_pawn_movement_predicat_to_wrong_pos_correct():
    pBeg = (2, 2)
    pEnd = (2, 1)
    gm.gameMap[pBeg] = Pawn(PawnColor.WHITE, PawnType.HORIZONTAL)
    gm.gameMap[pEnd] = None
    isMovableTo = pwmpi.is_horizontal_pawn_deplacement(pBeg, pEnd)
    assert(isMovableTo == False and "The horizontal pawn shouldn't be able move to one case west")

is_pos_inside_border()
is_pos_outside_border()

is_pos_without_pawn()
is_pos_with_pawn()

is_diagonal_pawn_movement_predicat_to_north_correct()
is_diagonal_pawn_movement_predicat_to_south_correct()
is_diagonal_pawn_movement_predicat_to_east_correct()
is_diagonal_pawn_movement_predicat_to_west_correct()
is_diagonal_pawn_movement_predicat_to_wrong_pos_correct()

is_horizontal_pawn_movement_predicat_to_southwest_correct()
is_horizontal_pawn_movement_predicat_to_northwest_correct()
is_horizontal_pawn_movement_predicat_to_northeast_correct()
is_horizontal_pawn_movement_predicat_to_southeast_correct()
is_horizontal_pawn_movement_predicat_to_wrong_pos_correct()