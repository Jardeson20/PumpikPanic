import sqlite3

class Score:
    def __init__(self, db_file="pumpik_panic.db"):
        self.db_file = db_file
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER NOT NULL
        )
        """)

        conn.commit()
        conn.close()

    def save_score(self, score):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (score) VALUES (?)", (score,))
        conn.commit()
        conn.close()

    def load_scores(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT score FROM scores ORDER BY score DESC LIMIT 5")
        scores = [row[0] for row in cursor.fetchall()]
        conn.close()
        return scores