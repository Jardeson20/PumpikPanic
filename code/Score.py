import sqlite3

class Score:
    def __init__(self, db_file="pumpik_panic.db"):
        self.db_file = db_file
        self.create_table()  # Cria a tabela se não existir

    def create_table(self):
        # Conecta ao banco de dados (ou cria se não existir)
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # Cria a tabela de pontuações (se não existir)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER NOT NULL
        )
        """)

        # Salva as alterações e fecha a conexão
        conn.commit()
        conn.close()

    def save_score(self, score):
        # Salva uma nova pontuação no banco de dados
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (score) VALUES (?)", (score,))
        conn.commit()
        conn.close()

    def load_scores(self):
        # Carrega as 5 maiores pontuações do banco de dados
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT score FROM scores ORDER BY score DESC LIMIT 5")  # Alterado para LIMIT 5
        scores = [row[0] for row in cursor.fetchall()]  # Extrai os scores
        conn.close()
        return scores