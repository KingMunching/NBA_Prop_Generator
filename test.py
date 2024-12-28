# api end points to remember
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/teamandplayersvsplayers.md

# common team roster
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonteamroster.md


# can view end points here
# https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints


from nba_api.stats.endpoints import commonteamroster

# Basic Request
# team_id = 1610612752 = New York Knicks
team_info = commonteamroster.CommonTeamRoster(team_id=1610612752, season="2024-25")

print(team_info.get_json())
