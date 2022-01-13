import GameMap as gm
import json # thanks standard library

def save():
    jsoned = {
        "gameMap" : gm.gameMap_to_json(),
        "gameMapState" : gm.gameMapState.to_json()
    }
    with open('save', 'w') as fSave:
        json.dump(jsoned, fSave, indent=4)
