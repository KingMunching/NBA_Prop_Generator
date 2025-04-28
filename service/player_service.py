from nba_api.stats.endpoints import playercareerstats

def get_player_stats(player_id):
    """
    Retrieves the career stats for a given player by using the player ID.
    Returns the object provided by the NBA API.
    """
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career


def load_player_stats(player):
   
    pass
