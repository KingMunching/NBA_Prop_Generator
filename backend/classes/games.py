from classes.teams import Team

class Game:
    # team 1 will be HOME Team
    # team 2 will be AWAY Team
    team1 = Team
    team2 = Team 

    def __init__(self, team1:Team, team2:Team):
        self.team1 = team1
        self.team2 = team2
    
    def get_team1(self):
        return self.team1
    
    def set_team1(self, team):
        self.team1 = team
    
    def get_team2(self):
        return self.team2
    
    def set_team2(self, team):
        self.team2 = team
