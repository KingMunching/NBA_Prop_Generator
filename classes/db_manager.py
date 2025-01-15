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

        cursor.execute("INSERT INTO players (playerName, player_ID) VALUES (?,?)", (player.get_playerName(),player.get_playerID()) )
        connection.commit()

        #get the player
        cursor.execute("SELECT * FROM players")
        print(cursor.fetchall())
        connection.close()
        
if __name__ == "__main__":
    db = Database()
    db.test_insert()