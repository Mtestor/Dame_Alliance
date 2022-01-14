import GameMap as gm
import json # thanks standard library
import os.path
import PlayerState as ps

def save(player : ps.PlayerState):
    jsoned = {
        "gameMap" : gm.gameMap_to_json(),
        "gameMapState" : gm.gameMapState.to_json(),
        "playerState"  : player.to_json()
    }
    with open('save', 'w') as fSave:
        json.dump(jsoned, fSave, indent=4)

def do_save_exist() -> bool:
    return os.path.isfile('save')

def load() -> ps.PlayerState:
    jsoned = None
    with open('save', 'r') as fSave:
        jsoned = json.load(fSave)
    gm.gameMap_from_json(jsoned['gameMap'])
    gm.gameMapState = gm.gameMapState_from_json(jsoned['gameMapState'])
    return ps.player_from_json(jsoned['playerState'])
    
def do_highScore_exist() -> bool:
    return os.path.isfile('highScore')

def highScore_save(highScore : list):
    with open('highScore', 'w') as fHighScore:
        json.dump(highScore, fHighScore, indent=4)

def highScore_load() -> list:
    jsoned = []
    with open('highScore', 'r') as fHighScore:
        jsoned = json.load(fHighScore)
    return jsoned
