from pygame.math import enable_swizzling
import GameMap as gm
import Pawn as pw
import Movement as mv

def do_enemy_have_pawn(enemy : pw.PawnColor):
    return gm.gameMapState.number_pawn(enemy) != 0

def can_move(pos : tuple):
    for r in range(pos[0] - 1, pos[0] + 2):
        for c in range(pos[1] - 1, pos[1] + 2):
            if mv.is_movement_legal(pos, (r, c)):
                return True
    return False

def can_capture(pos : tuple):
    for r in range(pos[0] - 2, pos[0] + 3):
        for c in range(pos[1] - 2, pos[1] + 3):
            if mv.which_capture(pos, (r, c)) != None:
                return True
    return False

def is_enemy_blocked(enemy : pw.PawnColor):
    for r in range(gm.ROW_MAX + 1):
        for c in range(gm.COLOMN_MAX + 1):
            if gm.gameMap[r,c] != None and gm.gameMap[r,c].m_color == enemy:
                if can_move((r, c)):
                    return False
                if can_capture((r, c)):
                    return False
    return True

def have_win(playerColor : pw.PawnColor) -> bool:
    enemy = pw.inv_pawnColor(playerColor)
    if not do_enemy_have_pawn(enemy):
        return True
    if is_enemy_blocked(enemy):
        return True
    return False

def winner_early_end() -> pw.PawnColor:
    brn = gm.gameMapState.number_royal_pawn(pw.PawnColor.BLACK)
    wrn = gm.gameMapState.number_royal_pawn(pw.PawnColor.WHITE) 
    if brn > wrn:
        return pw.PawnColor.BLACK
    elif brn < wrn:
        return pw.PawnColor.WHITE
    else:
        return pw.PawnColor.NONE

def is_early_endable():
    if gm.gameMapState.number_royal_pawn(pw.PawnColor.BLACK) == gm.gameMapState.number_pawn(pw.PawnColor.BLACK) and \
       gm.gameMapState.number_royal_pawn(pw.PawnColor.WHITE) == gm.gameMapState.number_pawn(pw.PawnColor.WHITE):
        return True
    return False