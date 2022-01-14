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

def do_save_exist():
    return os.path.isfile('save')

def load() -> ps.PlayerState:
    jsoned = None
    with open('save', 'r') as fSave:
        jsoned = json.load(fSave)
    gm.gameMap_from_json(jsoned['gameMap'])
    gm.gameMapState = gm.gameMapState_from_json(jsoned['gameMapState'])
    return ps.player_from_json(jsoned['playerState'])
    