class Team:
    teamID = ""
    teamName = ""
    city = ""
    state = ""
    players = []

    def __init__(self, teamID, teamName):
        self.teamID = teamID
        self.teamName = teamName

    def get_teamID(self):
        return self.teamID
    
    def set_teamID(self, teamID):
        self.teamID = teamID
    
    def get_teamName(self):
        return self.teamName
    
    def set_teamName(self, teamName):
        self.teamName = teamName

    def get_city(self):
        return self.city
    
    def set_city(self, city):
        self.city = city
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def get_players(self):
        return self.players

    def set_players(self, players):
        self.players = players