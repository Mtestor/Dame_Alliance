import GameMap as gm
import json # thanks standard library
import os.path

def save():
    jsoned = {
        "gameMap" : gm.gameMap_to_json(),
        "gameMapState" : gm.gameMapState.to_json()
    }
    with open('save', 'w') as fSave:
        json.dump(jsoned, fSave, indent=4)

def do_save_exist():
    return os.path.isfile('save')

def load():
    jsoned = None
    with open('save', 'r') as fSave:
        jsoned = json.load(fSave)
    gm.gameMap_from_json(jsoned['gameMap'])
    gm.gameMapState = gm.gameMapState_from_json(jsoned['gameMapState'])
    