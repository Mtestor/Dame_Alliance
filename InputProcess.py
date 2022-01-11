from numpy import true_divide
import pygame
import PlayerState as ps
import Movement
import GameMap as gm

UNIT_CASE_SIZE = 100

def mousePos_to_mapPos(mousePos):
    colomn = mousePos[0] // UNIT_CASE_SIZE
    row = mousePos[1] // UNIT_CASE_SIZE
    return (row, colomn)

def pawn_choosing_proccess(pos, player : ps.PlayerState):
    if not Movement.is_pos_in_border(pos):
        return
    if Movement.is_pos_free(pos):
        return
    if True:#gm.gameMap[pos].m_color == player.m_color:
        player.m_isPawnChoosed = True
        player.m_pawnPos = pos

def movement_process(pos, player : ps.PlayerState):
    if Movement.is_movement_legal(player.m_pawnPos, pos):
        Movement.move_pawn_to(player.m_pawnPos, pos)
        player.m_pawnPos = pos
        return
    player.m_isPawnChoosed = False

def click_input_process(mousePos, player : ps.PlayerState):
    pos = mousePos_to_mapPos(mousePos)
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
                player.isClicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            if player.isClicked:
                mousePos = pygame.mouse.get_pos()
                click_input_process(mousePos, player)
                player.isClicked = False