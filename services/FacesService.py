from infra.DataBase.Connection import ConnectionDB
from models.Faces import Faces

class FacesService:
    def __init__(self, aluno=None) -> None:
        self.connection_db = ConnectionDB()
        self.aluno = aluno
        self.faces = Faces(self.aluno)

    def storeFaces(self):
        self.faces.extractFace()
        self.faces.storageFace()
    
    def updateFaces(self):
        self.faces.extractFace()
        self.faces.updateFace()

    # @staticmethod
    # def importFacesService(self):
    #     return self.faces.importFaces()
