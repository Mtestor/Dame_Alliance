from sys import hash_info
from numpy import histogram
from pygame import KEYUP
import pygame.locals as pl
import pygame.key
import GameMap as gm
import PlayerState as ps
import SaveReload as sr
import Pawn as pw

def add_letter_to_winner_name(letter_key):
    letter = pygame.key.name(letter_key)
    if len(gm.gameMapState.m_winnerName) < 10:
        gm.gameMapState.m_winnerName = gm.gameMapState.m_winnerName + letter

def remove_last_letter_from_winner_name():
    if len(gm.gameMapState.m_winnerName) > 0:
        gm.gameMapState.m_winnerName = gm.gameMapState.m_winnerName[:-1]

def end_Game(player : ps.PlayerState):
    gm.init(gm.gameMapState)
    player = ps.PlayerState(pw.PawnColor.WHITE)
    sr.save(player)

def find_pos_to_insert(highScore):
    playerScore = gm.gameMapState.score(gm.gameMapState.m_winnerColor)
    for i in range(len(highScore)):
        if playerScore > highScore[i][1]:
            return i
    return len(highScore)

def enter_name_in_highScore(highScore : list):
    if len(highScore) > 5:
        highScore.pop()
    index = find_pos_to_insert(highScore)
    highScore.insert(index, (gm.gameMapState.m_winnerName, gm.gameMapState.score(gm.gameMapState.m_winnerColor)))
    sr.highScore_save(highScore)

def process(eventList : list[pygame.event.Event], highScore : list, player : ps.PlayerState):
    for event in eventList:
        if event.type == KEYUP:
            if event.key == pl.K_RETURN:
                enter_name_in_highScore(highScore)
                end_Game(player)
            elif event.key >= pl.K_a and event.key <= pl.K_z:
                add_letter_to_winner_name(event.key)
            elif event.key == pl.K_BACKSPACE:
                remove_last_letter_from_winner_name()