from numpy import true_divide
import pygame
import PlayerState as ps
import Pawn as pw
import Movement
import GameMap as gm
import SaveReload as sr

UNIT_CASE_SIZE = 100

def mousePos_to_mapPos(mousePos):
    colomn = mousePos[0] // UNIT_CASE_SIZE
    row = mousePos[1] // UNIT_CASE_SIZE
    return (row, colomn)

def pawn_choosing_proccess(pos, player : ps.PlayerState):
    if player.m_hasMoved and pos != player.m_pawnPos:
        return
    if not Movement.is_pos_in_border(pos):
        return
    if Movement.is_pos_free(pos):
        return
    if gm.gameMap[pos].m_color == player.m_color:
        player.m_isPawnChoosed = True
        player.m_pawnPos = pos

def movement_process(pos, player : ps.PlayerState):
    if not player.m_hasMoved and Movement.is_movement_legal(player.m_pawnPos, pos):
        Movement.move_pawn_to(player.m_pawnPos, pos)
        player.m_pawnPos = pos
        player.m_hasMoved = True
        return

    if player.m_hasMoved and not player.m_hasCaptured:
        return
    capture = Movement.which_capture(player.m_pawnPos, pos)
    if capture != None:
        Movement.pawn_capture(player.m_pawnPos, pos, capture)
        player.m_pawnPos = pos
        if not player.m_hasCaptured:
            player.m_score = 1
        else:
            player.m_score *= 2
        player.m_hasMoved = True
        player.m_hasCaptured = True
        return 
        
    player.m_isPawnChoosed = False
    
def end_turn(player : ps.PlayerState):
    gm.gameMapState.add_score(player.m_color, player.m_score)
    player.reset(pw.inv_pawnColor(player.m_color))

def gui_process(pos, player : ps.PlayerState):
    if pos[1] == gm.COLOMN_MAX and player.m_hasMoved:
        end_turn(player)
    elif pos[1] == gm.COLOMN_MAX - 1 and player.m_isPawnChoosed and player.m_hasMoved:
        pawn = gm.gameMap[player.m_pawnPos]
        pawn.m_type = pw.inv_pawnType(pawn.m_type)
        end_turn(player)
    return

def click_input_process(mousePos, player : ps.PlayerState):
    pos = mousePos_to_mapPos(mousePos)
    if pos[0] == gm.ROW_MAX + 1:
        gui_process(pos, player)
    if player.m_isPawnChoosed:
        movement_process(pos, player)
    elif not player.m_isPawnChoosed:
        pawn_choosing_proccess(pos, player)
    else:
        assert(False and "player.m_isPawnChoosed doit être soit vrai, soit faux.")

def process(input_list, player : ps.PlayerState):
    for event in input_list:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == True:
                player.m_isClicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if player.m_isClicked:
                mousePos = pygame.mouse.get_pos()
                click_input_process(mousePos, player)
                player.isClicked = False