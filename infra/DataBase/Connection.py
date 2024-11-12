import sqlite3
import datetime

class ConnectionDB:
    def __init__(self, db_name: str = "reconhecimento_db") -> None:
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def open(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name, check_same_thread=False)
            self.connection.row_factory = sqlite3.Row 
            self.cursor = self.connection.cursor()
            print("Conexão aberta com o banco de dados.")
        else:
            print("A conexão já está aberta.")

    def query(self, statement: str, data: tuple) -> list:

        if self.connection is None:
            raise Exception("Conexão com o banco não está aberta. Use o método 'open' para abrir a conexão.")
        
        try:
            self.cursor.execute(statement, data)
            self.connection.commit() 
            return self.cursor.fetchall()  
        except sqlite3.DatabaseError as e:
            print(f"Erro ao executar a query: {e}")
            return []

    def close(self) -> None:
        if self.connection is not None:
            try:
                self.cursor.close() 
                self.connection.close()  
                print("Conexão fechada com sucesso.")
            except sqlite3.DatabaseError as e:
                print(f"Erro ao fechar a conexão: {e}")
            finally:
                self.connection = None
                self.cursor = None
        else:
            print("A conexão já está fechada.")

# Exemplo de uso da classe
if __name__ == "__main__":
    # Criar conexão com o banco de dados
    db = ConnectionDB()
    db.open()
    # db.open()
    db.query("DROP TABLE user", ())
    db.query("DROP TABLE logs", ())
    db.query("DROP TABLE programs", ())
    db.query("DROP TABLE user_programs", ())
    db.query("DROP TABLE administrator", ())
    # db.query("CREATE TABLE recognation_logs (recognation_id VARCHAR(36), user_id VARCHAR(36), access_time DATE, status VARCHAR(30))", ())
    # db.query("CREATE TABLE users (user_id int, name VARCHAR(36), document VARCHAR(15), course VARCHAR(36), registration_code VARCHAR(45), photo VARCHAR(100), created_at DATE, updated_at DATE)", ())
    # ("INSERT INTO users (user_id, name, document, course, registration_code, photo, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (2, 'Fábio da Silva Eloi Jr', "628.031.203-80", "Engenharia de Computação 2022", "20221ENG.SIN0004", "/home/nando/Desktop/reconhecimento-facial/data/imagens/20221ENG.SIN0004.jpg", datetime.now(), datetime.now()))
    # db.query("UPDATE users SET photo = ? WHERE user_id = ?",('/home/nando/Desktop/reconhecimento-facial/20221ENG.SIN0003.jpg', 1) )
    # db.query("INSERT INTO recognation_logs (recognation_id, user_id, access_time, status) VALUES (?, ?, ?, ?)", ("1", '1', datetime.datetime.now(), "recognation"))
    # db.query("DELETE FROM recognation_logs WHERE recognation_id = ? ", ("1"))
    # rows = db.query("SELECT * FROM users", ())
    # for row in rows:
        # print(f"{row['user_id']}, {row['name']} {row['document']} {row['course']} {row['registration_code']} {row['photo']} {row['created_at']} {row['updated_at']}")
    # db.close()
