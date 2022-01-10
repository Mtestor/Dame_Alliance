import pygame
from numpy import full
from enum import IntEnum

from pygame import draw

WINDOW_HEIGHT = 900
WINDOW_LENGHT = 800

UNIT_CASE_SIZE = 100
UNIT_CASE_WHITE = pygame.Color(219, 218, 151)
UNIT_CASE_BLACK = pygame.Color(0, 128, 1)

PAWN_BLACK = pygame.Color(50, 40, 5)
PAWN_WHITE = pygame.Color(246, 246, 234)
PAWN_RADIUS = (UNIT_CASE_SIZE - 10) // 2

ROW = 8
COlOMN = 8

#class UnitCasePawn(IntEnum):
#    NOBODY = 0
#    BLACK = 1
#    WHITE = 2
#
#gameMap = full((ROW, COlOMN), UnitCasePawn.NOBODY)

def inv_unitCaseColor(unitCaseColor):
    if (unitCaseColor == UNIT_CASE_BLACK):
        return UNIT_CASE_WHITE
    elif (unitCaseColor ==  UNIT_CASE_WHITE):
        return UNIT_CASE_BLACK
    assert(False and "Une case est soit blanc soit noir")

def draw_background():
    actualColor = UNIT_CASE_BLACK
    for r in range(ROW):
        actualColor = inv_unitCaseColor(actualColor)
        for c in range(COlOMN):
            screen.fill(actualColor, (r * UNIT_CASE_SIZE, c * UNIT_CASE_SIZE, UNIT_CASE_SIZE, UNIT_CASE_SIZE))
            actualColor = inv_unitCaseColor(actualColor)

def center_unitCase(pos : tuple):
    assert(len(pos) == 2 and "La position est un tuple de taille 2")
    return (pos[1] * UNIT_CASE_SIZE + UNIT_CASE_SIZE // 2, pos[0] * UNIT_CASE_SIZE + UNIT_CASE_SIZE //2)

def draw_pawn(surface, pos : tuple, c : pygame.Color):
    center = center_unitCase(pos)
    pygame.draw.circle(surface, c, center, PAWN_RADIUS)

pygame.init()

screen = pygame.display.set_mode((WINDOW_LENGHT, WINDOW_HEIGHT), 0)
pygame.display.set_caption("Dame Alliance")

IS_GAMELOOP_STOPPED = False
fpsLimiter = pygame.time.Clock()

while not IS_GAMELOOP_STOPPED:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_GAMELOOP_STOPPED = True

    draw_background()
    draw_pawn(screen, (1, 2), PAWN_BLACK)
    pygame.display.flip()
    fpsLimiter.tick(30)