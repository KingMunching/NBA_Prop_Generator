import sqlite3
from players import Player
class Database:
    

    def __init__(self, db_path='test.db'):
        self.db_path = db_path
        self.intialize_db()
        pass
    
    def intialize_db(self):
        connection = sqlite3.connect('test.db')
        #Cursor instance
        cursor = connection.cursor()

        cursor.execute(
        """CREATE TABLE IF NOT EXISTS players (
                playerName TEXT,
                player_ID INTEGER PRIMARY KEY
        )""")

        connection.commit()
        connection.close()
    
    def test_insert(self):
        player = Player(125, "King")
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        if self.check_if_in_database(player.get_playerID()):
            print(f"Player {player.get_playerName()} is in the database")
        else:
            cursor.execute("INSERT INTO players (playerName, player_ID) VALUES (?,?)", (player.get_playerName(),player.get_playerID()) )
            connection.commit()

        #get the player
        cursor.execute("SELECT rowid, * FROM players")
        print(cursor.fetchall())
        connection.close()

    def check_if_in_database(self, playerid):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM players WHERE player_ID = ?", (playerid,))
        result = cursor.fetchone()
        connection.close()
        #return true if player exists, false otherwise
        return result is not None
    

        
if __name__ == "__main__":
    db = Database()
    db.test_insert()