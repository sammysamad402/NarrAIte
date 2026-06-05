
import sqlite3
class SQLiteManager:
    def __init__(self,db='story.db'):
        self.conn=sqlite3.connect(db)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS stories(
        id INTEGER PRIMARY KEY,
        content TEXT)''')
    def save_story(self,text):
        self.conn.execute('INSERT INTO stories(content) VALUES(?)',(text,))
        self.conn.commit()
