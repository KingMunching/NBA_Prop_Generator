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

    def get_playerID(self):
        return self.playerId
    
    def set_playerID(self, playerId):
        self.playerId = playerId

    def get_playerName(self):
        return self.playerName
    
    def set_playerName(self, playerName):
        self.playerName = playerName

    def get_GP(self):
        return self.GP
    
    def set_GP(self, GP):
        self.GP = GP

    def get_GS(self):
        return self.GS
    
    def set_GS(self, GS):
        self.GS = GS

    def get_MIN(self):
        return self.MIN
    
    def set_MIN(self, MIN):
        self.MIN = MIN

    def get_FGM(self):
        return self.FGM
    
    def set_FGM(self, FGM):
        self.FGM = FGM

    def get_FGA(self):
        return self.FGA
    
    def set_FGA(self, FGA):
        self.FGA = FGA

    def get_FG_PCT(self):
        return self.FG_PCT
    
    def set_FG_PCT(self, FG_PCT):
        self.FG_PCT = FG_PCT

    def get_FG3M(self):
        return self.FG3M
    
    def set_FG3M(self, FG3M):
        self.FG3M = FG3M

    def get_FG3A(self):
        return self.FG3A
    
    def set_FG3A(self, FG3A):
        self.FG3A = FG3A

    def get_FG3_PCT(self):
        return self.FG3_PCT
    
    def set_FG3_PCT(self, FG3_PCT):
        self.FG3_PCT = FG3_PCT

    def get_FTM(self):
        return self.FTM
    
    def set_FTM(self, FTM):
        self.FTM = FTM

    def get_FTA(self):
        return self.FTA
    
    def set_FTA(self, FTA):
        self.FTA = FTA

    def get_FT_PCT(self):
        return self.FT_PCT
    
    def set_FT_PCT(self, FT_PCT):
        self.FT_PCT = FT_PCT

    def get_OREB(self):
        return self.OREB
    
    def set_OREB(self, OREB):
        self.OREB = OREB

    def get_DREB(self):
        return self.DREB
    
    def set_DREB(self, DREB):
        self.DREB = DREB

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
