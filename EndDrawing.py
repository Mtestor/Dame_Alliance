import pygame.surface
import pygame.font
import pygame.color
import GameMap as gm

UNIT_CASE_SIZE = 100

def draw_winner_name(surface : pygame.surface.Surface, END_FONT : pygame.font.Font):
    textSurfaceName = END_FONT.render("Enter your name", False, pygame.color.Color('darkblue'))
    surface.blit(textSurfaceName, ((gm.COLOMN_MAX // 2) * UNIT_CASE_SIZE - UNIT_CASE_SIZE // 2, gm.ROW_MAX * UNIT_CASE_SIZE + UNIT_CASE_SIZE // 2))
    winnerString = gm.gameMapState.m_winnerName + " : " + str(gm.gameMapState.score(gm.gameMapState.m_winnerColor))
    textSurfaceWinner = END_FONT.render(winnerString, False, pygame.color.Color('black'))
    surface.blit(textSurfaceWinner, ((gm.COLOMN_MAX // 2) * UNIT_CASE_SIZE, (gm.ROW_MAX + 1) * UNIT_CASE_SIZE + UNIT_CASE_SIZE // 4))

def draw_highScore(surface : pygame.surface.Surface, END_FONT : pygame.font.Font, highScore : list):
    textSurfaceHighScore = END_FONT.render("High Score", False, pygame.color.Color('darkblue'))
    surface.blit(textSurfaceHighScore, ((gm.COLOMN_MAX // 2) * UNIT_CASE_SIZE, UNIT_CASE_SIZE // 2))
    for k in range(len(highScore)):
        textSurfaceHighScoreName = END_FONT.render(highScore[k][0], False, pygame.color.Color('darkred'))
        surface.blit(textSurfaceHighScoreName, (UNIT_CASE_SIZE, (k + 1) * UNIT_CASE_SIZE + UNIT_CASE_SIZE // 2))
        textSurfaceHighScorePoint = END_FONT.render(str(highScore[k][1]), False, pygame.color.Color('darkred'))
        surface.blit(textSurfaceHighScorePoint, ((gm.COLOMN_MAX + 1) * UNIT_CASE_SIZE - UNIT_CASE_SIZE, (k + 1) * UNIT_CASE_SIZE + UNIT_CASE_SIZE // 2))

def draw_end(surface : pygame.surface.Surface, END_FONT : pygame.font.Font, highScore : list):
    surface.fill(pygame.color.Color('white'))
    draw_highScore(surface, END_FONT, highScore)
    draw_winner_name(surface, END_FONT)