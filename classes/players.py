class Player:
    playerId = ""
    playerName = ""
    GP = 0
    GS = 0
    FG3A = 0
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

    def get_playerID(self):
        return self.playerId
    
    def set_playerID(self, playerId):
        self.playerId = playerId

    def get_playerName(self):
        return self.playerName
    
    def set_playerName(self, playerName):
        self.playerName = playerName


    def get_FG3M(self):
        return self.FG3M
    
    def set_FG3M(self, FG3M):
        self.FG3M = FG3M

    def get_REB(self):
        return self.REB
    
    def set_REB(self, REB):
        self.REB = REB

    def get_AST(self):
        return self.AST
    
    def set_AST(self, AST):
        self.AST = AST

    def get_STL(self):
        return self.STL
    
    def set_STL(self, STL):
        self.STL = STL

    def get_BLK(self):
        return self.BLK
    
    def set_BLK(self, BLK):
        self.BLK = BLK

    def get_TOV(self):
        return self.TOV
    
    def set_TOV(self, TOV):
        self.TOV = TOV

    def get_PF(self):
        return self.PF
    
    def set_PF(self, PF):
        self.PF = PF

    def get_PTS(self):
        return self.PTS
    
    def set_PTS(self, PTS):
        self.PTS = PTS
