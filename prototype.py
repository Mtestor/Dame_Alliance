import pygame
from numpy import full
from enum import IntEnum

WINDOW_HEIGHT = 900
WINDOW_LENGHT = 800

UNIT_CASE_SIZE = 100
UNIT_CASE_WHITE = pygame.Color('beige')
UNIT_CASE_BLACK = pygame.Color('darkgreen')

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
    pygame.display.flip()
    fpsLimiter.tick(30)