from infra.DataBase.Connection import ConnectionDB
from models.Aluno import Aluno
import datetime

class AlunoService:

    def __init__(self) -> None:
        self.connection_db = ConnectionDB()
        self.alunos = []  

    def createAluno(self, aluno:Aluno) -> None:
        try:
            self.connection_db.open()
            self.connection_db.query("INSERT INTO user (user_id, name, document, course, registration_code, photo, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (aluno.user_id, aluno.name, aluno.document, aluno.course, aluno.registration_code, aluno.photo, aluno.created_at, aluno.updated_at))
            self.connection_db.close()
        except Exception as e:
            print(e)
            
    def getAlunos(self) -> list[Aluno]:   # type: ignore
        try:
            self.connection_db.open()
            rows = self.connection_db.query("SELECT * FROM user", ())  
            self.connection_db.close()
            for row in rows:
                self.alunos.append(Aluno(**row) )  
            return self.alunos  
        except Exception as e:
            print(e)

    def getAlunoById(self, user_id:int) -> Aluno or None: # type: ignore
        try:
            self.connection_db.open()
            row = self.connection_db.query("SELECT * FROM user WHERE user_id = ? LIMIT 1", (user_id,))
            self.connection_db.close()
            return Aluno(**row[0])
        except Exception as e:
            print(e)        
