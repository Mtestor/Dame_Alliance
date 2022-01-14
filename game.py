from numpy import histogram
import pygame

import GameMap as gm
import Pawn as pw
import InputProcess as inp
import PlayerState as ps
import SaveReload as sr
import GameDrawing as gd
import EndDrawing as ed
import EndProcess

WINDOW_HEIGHT = 900
WINDOW_LENGHT = 800

gm.init(gm.gameMapState)
player = ps.PlayerState(pw.PawnColor.WHITE)
highScore = []

if sr.do_save_exist(): 
    player = sr.load()

if sr.do_highScore_exist():
    highScore = sr.highScore_load()

pygame.init()

screen = pygame.display.set_mode((WINDOW_LENGHT, WINDOW_HEIGHT), 0)
pygame.display.set_caption("Dame Alliance")

isGameloopStopped = False
fpsLimiter = pygame.time.Clock()
GAME_FONT = pygame.font.SysFont("Arial", 24)
END_FONT = pygame.font.SysFont("Arial", 48)

while not isGameloopStopped:

    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            isGameloopStopped = True
    
    if not gm.gameMapState.is_game_ended():
        inp.process(eventList, player)
    else:
        EndProcess.process(eventList, highScore, player)

    if gm.gameMapState.is_game_ended():
        ed.draw_end(screen, END_FONT, highScore)
    else:
        gd.draw_game(screen, player, GAME_FONT)
    
    pygame.display.flip()
    fpsLimiter.tick(30)