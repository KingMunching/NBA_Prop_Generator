from nba_api.stats.endpoints import playergamelog
import pandas as pd


## TESTING THIS STUFF


# Function to fetch all game logs and filter for Christmas Day games
def get_christmas_stats(player_id, season):
    # Fetch game logs for the player for the specified season
    player_logs = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    player_logs_df = player_logs.get_data_frames()[0]

    # Filter for games played on Christmas (December 25)
    player_logs_df['GAME_DATE'] = pd.to_datetime(player_logs_df['GAME_DATE'])
    christmas_stats = player_logs_df[player_logs_df['GAME_DATE'].dt.month == 12]
    christmas_stats = christmas_stats[christmas_stats['GAME_DATE'].dt.day == 25]

    return christmas_stats


# Stephen Curry's Player ID and example usage
player_id = 201939  # Stephen Curry's Player ID
season = "2024-25"  # Adjust for the current season or any other season
curry_christmas_stats = get_christmas_stats(player_id, season)

# Display the filtered DataFrame
print(curry_christmas_stats['PTS'])
print(curry_christmas_stats['AST'])
