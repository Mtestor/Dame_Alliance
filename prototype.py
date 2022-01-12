import pygame
from enum import IntEnum

from pygame.version import PygameVersion
import GameMap as gm
from Pawn import *
import InputProcess as inp
import PlayerState as ps

WINDOW_HEIGHT = 900
WINDOW_LENGHT = 800

UNIT_CASE_SIZE = 100
UNIT_CASE_WHITE = pygame.Color(219, 218, 151)
UNIT_CASE_BLACK = pygame.Color(0, 128, 1)

PAWN_BLACK = pygame.Color(50, 40, 5)
PAWN_WHITE = pygame.Color(246, 246, 234)
PAWN_RADIUS = (UNIT_CASE_SIZE - 10) // 2
PAWN_TYPE_COLOR = pygame.Color(111, 111, 52)
PAWN_TYPE_WIDTH = 11
PAWN_TYPE_LENGHT = PAWN_RADIUS - 20

gm.init()

ROW = 8
COlOMN = 8

def inv_unitCaseColor(unitCaseColor):
    if (unitCaseColor == UNIT_CASE_BLACK):
        return UNIT_CASE_WHITE
    if (unitCaseColor ==  UNIT_CASE_WHITE):
        return UNIT_CASE_BLACK
    assert(False and "Une case est soit blanc soit noir")

def draw_background(display):
    actualColor = UNIT_CASE_BLACK
    for r in range(ROW):
        actualColor = inv_unitCaseColor(actualColor)
        for c in range(COlOMN):
            display.fill(actualColor, (r * UNIT_CASE_SIZE, c * UNIT_CASE_SIZE, UNIT_CASE_SIZE, UNIT_CASE_SIZE))
            actualColor = inv_unitCaseColor(actualColor)


def center_unitCase(pos : tuple):
    assert(len(pos) == 2 and "La position est un tuple de taille 2")
    return (pos[1] * UNIT_CASE_SIZE + UNIT_CASE_SIZE // 2, pos[0] * UNIT_CASE_SIZE + UNIT_CASE_SIZE //2)

def draw_pawn_base(surface, center, c : pygame.Color):
    pygame.draw.circle(surface, c, center, PAWN_RADIUS)

def rigth_part_points(center, type : PawnType):
    if type == PawnType.HORIZONTAL:
        return((center[0] + PAWN_TYPE_WIDTH, center[1]) , 
            (center[0] + PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT, center[1]))
    if type == PawnType.DIAGONAL:
        return((center[0] + int(PAWN_TYPE_WIDTH * 0.7), center[1] + int(PAWN_TYPE_WIDTH * 0.7)) , 
            (center[0] + int(PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT * 0.7), center[1] + int(PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT * 0.7)))

def left_part_points(center, type : PawnType):
    if type == PawnType.HORIZONTAL:
        return((center[0] - PAWN_TYPE_WIDTH, center[1]), 
            (center[0] - PAWN_TYPE_WIDTH - PAWN_TYPE_LENGHT, center[1]))
    if type == PawnType.DIAGONAL:
        return((center[0] - int(PAWN_TYPE_WIDTH * 0.7), center[1] - int(PAWN_TYPE_WIDTH * 0.7)) , 
            (center[0] - int(PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT * 0.7), center[1] - int(PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT * 0.7)))

def top_part_points(center, type : PawnType):
    if type == PawnType.HORIZONTAL:
        return((center[0], center[1] + PAWN_TYPE_WIDTH), 
            (center[0], center[1] + PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT))
    if type == PawnType.DIAGONAL:
        return((center[0] + int(PAWN_TYPE_WIDTH * 0.7), center[1] - int(PAWN_TYPE_WIDTH * 0.7)) , 
            (center[0] + int(PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT * 0.7), center[1] - int(PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT * 0.7)))

def bottom_part_points(center, type : PawnType):
    if type == PawnType.HORIZONTAL:
        return((center[0], center[1] - PAWN_TYPE_WIDTH), 
            (center[0], center[1] - PAWN_TYPE_WIDTH - PAWN_TYPE_LENGHT))
    if type == PawnType.DIAGONAL:
        return((center[0] - int(PAWN_TYPE_WIDTH * 0.7), center[1] + int(PAWN_TYPE_WIDTH * 0.7)) , 
            (center[0] - int(PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT * 0.7), center[1] + int(PAWN_TYPE_WIDTH + PAWN_TYPE_LENGHT * 0.7)))

def draw_pawn_type(surface, center, type : PawnType):
    if type == PawnType.ROYAL:
        return
    rigthPart = rigth_part_points(center, type)
    leftPart = left_part_points(center, type)
    topPart = top_part_points(center, type)
    bottomPart = bottom_part_points(center, type)

    pygame.draw.line(surface, PAWN_TYPE_COLOR ,rigthPart[0], rigthPart[1], PAWN_TYPE_WIDTH)
    pygame.draw.line(surface, PAWN_TYPE_COLOR ,leftPart[0], leftPart[1], PAWN_TYPE_WIDTH)
    pygame.draw.line(surface, PAWN_TYPE_COLOR ,topPart[0], topPart[1], PAWN_TYPE_WIDTH)
    pygame.draw.line(surface, PAWN_TYPE_COLOR ,bottomPart[0], bottomPart[1], PAWN_TYPE_WIDTH)

def draw_pawn(surface, pos, c : pygame.Color, type : PawnType):
    center = center_unitCase(pos)
    draw_pawn_base(surface, center, c)
    draw_pawn_type(surface, center, type)


def pawnColor_to_color(pc : PawnColor):
    if (pc == PawnColor.WHITE):
        return PAWN_WHITE
    if (pc == PawnColor.BLACK):
        return PAWN_BLACK
    assert(False and "You didn't give a drawable pawnColor")

def draw_map(surface, player : ps.PlayerState):
    if player.m_isPawnChoosed:
        pygame.draw.circle(surface, pygame.Color('red'), center_unitCase(player.m_pawnPos), PAWN_RADIUS + 2)
    for r in range(gm.ROW_MAX + 1):
        for c in range(gm.COLOMN_MAX + 1):
            p = gm.gameMap[r,c]
            if (p != None):
                draw_pawn(surface, (r, c), pawnColor_to_color(p.m_color), p.m_type)

def triangle_points_around_center(center : tuple):
    rigth_part_points = (center[0] + UNIT_CASE_SIZE // 2, center[1])
    top_part_points = (center[0] - UNIT_CASE_SIZE // 2, center[1] - UNIT_CASE_SIZE // 2)
    bottom_part_points = (center[0] - UNIT_CASE_SIZE // 2, center[1] + UNIT_CASE_SIZE // 2)
    return(top_part_points, rigth_part_points, bottom_part_points)

def draw_gui(surface, player : ps.PlayerState):
    posColorPlayer = (gm.ROW_MAX + 1, 0)
    pygame.draw.circle(surface, pawnColor_to_color(player.m_color), center_unitCase(posColorPlayer), PAWN_RADIUS)
    posEndTurn = (gm.ROW_MAX + 1, gm.COLOMN_MAX)
    pygame.draw.polygon(surface, pygame.Color('darkblue'), triangle_points_around_center(center_unitCase(posEndTurn)))
    posChangeType = (gm.ROW_MAX + 1, gm.COLOMN_MAX - 1)
    surface.fill(pygame.Color('red'), (posChangeType[1] * UNIT_CASE_SIZE + 5, posChangeType[0] * UNIT_CASE_SIZE + 5, UNIT_CASE_SIZE - 10, UNIT_CASE_SIZE - 10))

pygame.init()

screen = pygame.display.set_mode((WINDOW_LENGHT, WINDOW_HEIGHT), 0)
pygame.display.set_caption("Dame Alliance")

GAME_FONT = pygame.font.SysFont("Arial", 24)

isGameloopStopped = False
fpsLimiter = pygame.time.Clock()
player = ps.PlayerState(PawnColor.WHITE)

while not isGameloopStopped:

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            isGameloopStopped = True
    
    inp.process(event_list, player)

    screen.fill(pygame.Color('black'))
    draw_background(screen)
    draw_map(screen, player)
    draw_gui(screen, player)
   
    text_surface_black = GAME_FONT.render(str(gm.gameMapState.m_BlackScore), False, PAWN_BLACK)
    text_surface_white = GAME_FONT.render(str(gm.gameMapState.m_WhiteScore), False, PAWN_WHITE)
    screen.blit(text_surface_white, (1 * UNIT_CASE_SIZE, (gm.ROW_MAX + 1) * UNIT_CASE_SIZE))
    screen.blit(text_surface_black, (3 * UNIT_CASE_SIZE, (gm.ROW_MAX + 1) * UNIT_CASE_SIZE))

    if gm.gameMapState.number_pawn(PawnColor.BLACK) == 0 or gm.gameMapState.number_pawn(PawnColor.WHITE) == 0:
        screen.fill(pygame.Color('red'))
    
    pygame.display.flip()
    fpsLimiter.tick(30)