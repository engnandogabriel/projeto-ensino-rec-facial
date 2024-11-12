import face_recognition as fr
import numpy as np
import shutil

class Faces:
    def __init__(self, Aluno=None):
        self.aluno = Aluno
        self.face = list
        self.faces_armazenadas = "data/backup/faces.npz"

    def extractFace(self) -> None:
        imagem = self.importImage()
        aluno = fr.load_image_file(imagem)
        self.face = fr.face_encodings(aluno)[0] 

    def importImage(self) -> str:
        pathImage = "data/imagens/%s.jpg" % self.aluno.registration_code
        # Copiar o arquivo local para o novo caminho
        shutil.copy(self.aluno.photo, pathImage)
        return pathImage


    # def importaImagem(self):
    #     caminhoDaImagem = "data/imagens/%s.jpg" % self.aluno.registration_code
    #     urllib.request.urlretrieve(self.aluno.photo, caminhoDaImagem)
        
        # return caminhoDaImagem
    def storegeFaces(self, user_id) -> None:
        try:
            faces_dict = dict(np.load(self.faces_armazenadas, allow_pickle=True))
        except (FileNotFoundError, ValueError):  # Se o arquivo não existe ou está corrompido
            faces_dict = {}

        faces_dict[user_id] = self.face
        np.savez(self.faces_armazenadas, **faces_dict)
       
    def updateFace(self) -> None:
        print('Atualizando Face')        
        backup = self.loadFaces()
        backup[self.aluno.registration_code] = self.face
        np.savez(self.faces_armazenadas, **backup)

       
    def importFaces(self) -> list:
        try:
            backup = dict(np.load(self.faces_armazenadas, allow_pickle=True))
            faces = []
            for user_id, face_matrix in backup.items():
                if face_matrix.size != 0:
                    faces.append((user_id, face_matrix))
            dict_datas = {user_id: face_matrix for user_id, face_matrix in faces}
            
            return list(dict_datas.keys()), list(dict_datas.values())
          
        except Exception as e:
            print(e)
            print("Não foi possível ler os dados")

    def loadFaces(self) -> dict:
        try:
            data = np.load(self.faces_armazenadas)
            faces_dict = {key: data[key] for key in data.files}
            return faces_dict
        except FileNotFoundError:
            print("Arquivo de faces não encontrado. Retornando dicionário vazio.")
            return {}  # Retorna um dicionário vazio caso o arquivo não exista