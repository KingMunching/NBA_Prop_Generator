class Player:
    playerId = ""
    playerName = ""
    GP = 0
    GS = 0
    MIN = 0
    FGM = 0
    FGA = 0
    FG_PCT = 0
    FG3M = 0
    FG3A = 0
    FG3_PCT = 0
    FTM = 0
    FTA = 0
    FT_PCT = 0
    OREB = 0
    DREB = 0
    REB = 0
    AST = 0
    STL = 0
    BLK = 0
    TOV = 0
    PF = 0
    PTS = 0

    def __init__(self, playerId, playerName):
        self.playerId = playerId
        self.playerName = playerName
