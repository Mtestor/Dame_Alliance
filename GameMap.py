from numpy import full
import Pawn as pw

ROW_MAX = 7
COLOMN_MAX = 7

gameMap = full((ROW_MAX + 1, COLOMN_MAX + 1), None)

def gameMap_to_json():
    jsoned = list()
    for r in range(ROW_MAX + 1):
        jsoned.append(list())
        for c in range(COLOMN_MAX + 1):
            if gameMap[r,c] == None:
                jsoned[r].append(None)
            else:
                jsoned[r].append(gameMap[r,c].to_json())
    return jsoned

def gameMap_from_json(jsoned):
    for r in range(ROW_MAX + 1):
        for c in range(COLOMN_MAX + 1):
            if jsoned[r][c] == None:
                gameMap[r,c] = None
            else:
                gameMap[r,c] = pw.pawn_from_json(jsoned[r][c])

class GameMapState:
    """Hold the state of the gameMap"""
    def __init__(self, blackNormalPawn = 12, blackRoyalPawn = 0, blackScore = 0, 
            whiteNormalPawn = 12, whiteRoyalPawn = 0, whiteScore = 0, wantToEarlyEnd = False):
        self.m_BlackNormalPawn = blackNormalPawn
        self.m_BlackRoyalPawn = blackRoyalPawn
        self.m_WhiteNormalPawn = whiteNormalPawn
        self.m_WhiteRoyalPawn = whiteRoyalPawn
        self.m_BlackScore = blackScore
        self.m_WhiteScore = whiteScore
        self.m_wantToEarlyEnd = wantToEarlyEnd
        self.m_isGameEnded = False
        self.m_winnerColor = pw.PawnColor.NONE
        self.m_winnerName = ""

    def number_pawn(self, pawnColor : pw.PawnColor):
        if pawnColor == pw.PawnColor.BLACK:
            return self.m_BlackNormalPawn + self.m_BlackRoyalPawn
        else:
            return self.m_WhiteNormalPawn + self.m_WhiteRoyalPawn

    def number_royal_pawn(self, pawnColor : pw.PawnColor):
        if pawnColor == pw.PawnColor.BLACK:
            return self.m_BlackRoyalPawn
        else:
            return self.m_WhiteRoyalPawn

    def add_royal_pawn(self, pawnColor : pw.PawnColor):
        if pawnColor == pw.PawnColor.BLACK:
            self.m_BlackRoyalPawn += 1
            self.m_BlackNormalPawn -= 1
        else:
            self.m_WhiteRoyalPawn += 1
            self.m_WhiteNormalPawn -= 1

    def add_score(self, pawnColor : pw.PawnColor, points):
        if pawnColor == pw.PawnColor.BLACK:
            self.m_BlackScore += points
        else:
            self.m_WhiteScore += points
    
    def remove_pawn(self, pawnColor : pw.PawnColor, pawnType : pw.PawnType):
        if pawnColor == pw.PawnColor.BLACK:
            if pawnType == pw.PawnType.ROYAL:
                self.m_BlackRoyalPawn -= 1
            else:
                self.m_BlackNormalPawn -= 1
        else:
            if pawnType == pw.PawnType.ROYAL:
                self.m_WhiteRoyalPawn -= 1
            else:
                self.m_WhiteNormalPawn -= 1

    def do_want_to_end_early(self):
        return self.m_wantToEarlyEnd
    
    def want_to_end_early(self, choice : bool):
        self.want_to_end_early = choice

    def end_game(self, playerColor : pw.PawnColor):
        self.m_winnerColor = playerColor
        self.m_isGameEnded = True

    def is_game_ended(self):
        return self.m_isGameEnded

    def reset(self):
        self.__init__()

    def to_json(self):
        return {
            "black" : [
                self.m_BlackNormalPawn,
                self.m_BlackRoyalPawn,
                self.m_BlackScore
            ],
            "white" : [
                self.m_WhiteNormalPawn,
                self.m_WhiteRoyalPawn,
                self.m_WhiteScore
            ],
            "earlyEnd" : self.m_wantToEarlyEnd
        }

def gameMapState_from_json(jsoned) -> GameMapState:
    return GameMapState(jsoned['black'][0], jsoned['black'][1], jsoned['black'][2],
            jsoned['white'][0], jsoned['white'][1], jsoned['white'][2], jsoned['earlyEnd'])

gameMapState = GameMapState()

def init(gameMapState : GameMapState):
    gameMap[:,:] = None
    for k in range(1, 7):
        gameMap[1, k] = pw.Pawn(pw.PawnColor.BLACK, pw.PawnType.HORIZONTAL)
        gameMap[2, k] = pw.Pawn(pw.PawnColor.BLACK, pw.PawnType.DIAGONAL)

        gameMap[5, k] = pw.Pawn(pw.PawnColor.WHITE, pw.PawnType.DIAGONAL)
        gameMap[6, k] = pw.Pawn(pw.PawnColor.WHITE, pw.PawnType.HORIZONTAL)
    
    gameMapState.reset()