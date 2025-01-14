import sqlite3

class Database:

    def __init__(self, db_path='test.db'):
        pass
    
    connection = sqlite3.connect('test.db')

    #Cursor instance
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS players (
                playerName TEXT,
                player_ID INTEGER PRIMARY KEY
               )
                """)