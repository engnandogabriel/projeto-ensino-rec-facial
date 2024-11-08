from infra.DataBase.Connection import ConnectionDB
from models.Aluno import Aluno
import datetime

class AlunoService:

    def __init__(self) -> None:
        self.connection_db = ConnectionDB()
        self.alunos = []  

    def createAluno(self, aluno:Aluno) -> None:
        try:
            self.connection_db.query("INSERT INTO users (user_id, name, document, course, registration_code, photo, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (aluno.user_id, aluno.name, aluno.document, aluno.course, aluno.registration_code, aluno.photo, aluno.created_at, aluno.updated_at))
        except Exception as e:
            print(e)
            
    def getAlunos(self) -> list[Aluno] or None:   # type: ignore
        try:
            rows = self.connection_db.query("SELECT * FROM users", ())  
            for row in rows:
                self.alunos.append(Aluno(**row) )  
            return self.alunos  
        except Exception as e:
            print(e)

    def getAlunoById(self, user_id:int) -> Aluno or None: # type: ignore
        try:
            row = self.connection_db.query("SELECT * FROM users WHERE user_id = ?", (user_id,))
            return Aluno(**row[0])
        except Exception as e:
            print(e)        
