from infra.DataBase.Connection import ConnectionDB
from models.Faces import Faces

class FacesService:
    def __init__(self, aluno=None) -> None:
        self.connection_db = ConnectionDB()
        self.aluno = aluno
        self.faces = Faces(self.aluno)

    def storeFaces(self, user_id):
        self.faces.extractFace()
        self.faces.storegeFaces(user_id)
    
    def updateFaces(self):
        self.faces.extractFace()
        self.faces.updateFace()

