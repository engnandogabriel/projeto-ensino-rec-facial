import sqlite3
from datetime import datetime

class ConnectionDB:
    def __init__(self, db_name: str = "reconhecimento_db") -> None:
        self.connection = sqlite3.connect(db_name)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def query(self, statement:str, data:list) -> sqlite3.Row:
        row = self.cursor.execute(statement, data)
        self.connection.commit()
        return row.fetchall()
    

    def close(self) -> None:
        self.connection.close()


# Exemplo de uso da classe
if __name__ == "__main__":
    # Criar conexão com o banco de dados
    db = ConnectionDB()
    # db.query("DROP TABLE users", ())
    # db.query("CREATE TABLE users (user_id int, name VARCHAR(36), document VARCHAR(15), course VARCHAR(36), registration_code VARCHAR(45), photo VARCHAR(100), created_at DATE, updated_at DATE)", ())
    # db.query("INSERT INTO users (user_id, name, document, course, registration_code, photo, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (2, 'Fábio da Silva Eloi Jr', "628.031.203-80", "Engenharia de Computação 2022", "20221ENG.SIN0004", "/home/nando/Desktop/reconhecimento-facial/data/imagens/20221ENG.SIN0004.jpg", datetime.now(), datetime.now()))
    # db.query("UPDATE users SET photo = ? WHERE user_id = ?",('/home/nando/Desktop/reconhecimento-facial/20221ENG.SIN0003.jpg', 1) )
    rows = db.query("SELECT * FROM users", ())
    for row in rows:
        print(f"{row['user_id']}, {row['name']} {row['document']} {row['course']} {row['registration_code']} {row['photo']} {row['created_at']} {row['updated_at']}")
    db.close()
