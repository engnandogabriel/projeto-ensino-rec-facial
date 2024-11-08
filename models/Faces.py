import face_recognition as fr
import numpy as np
import base64
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
    
    def storageFace(self) -> None:
        print('Armazenando Face')
        # ARMAZENAMENTO LOCAL:

        try:
            backup = self.loadFaces()
        except:
            np.savez(self.faces_armazenadas, np.array([]))
            backup = np.load(self.faces_armazenadas)

        faces = []

        # Armazena na lista de faces todas os objetos (faces) não nulas que estão na variável de backup
        for item in backup.files:
            if (backup[item] != []): 
                faces.append(backup[item])
        
        faces.append(self.face)
        np.savez(self.faces_armazenadas, *faces)

        # Abaixo adiciona-se o nome e a matrícula dos alunos em um arquivo local no seguinte formato: matricula1:aluno1/matricula2:aluno2/.../matriculaN:alunoN/
        with open("data/backup/nomes.txt", "a") as arquivo:
            arquivo.write("%s:%s/" % (self.aluno.registration_code, self.aluno.name))

    def updateFace(self) -> None:
        print('Atualizanco Face')
        backup = self.loadFaces()
        faces = []
        for item in backup.files:
            if backup[item] != []:
                faces.append(backup[item])

        matriculaAluno = self.dados.matriculas

        indexAluno = matriculaAluno.index(self.aluno.registration_code)

        faces[indexAluno] = self.face
        np.savez(self.faces_armazenadas, *faces)

        tobase64 = base64.b64encode(self.face)

        #requests.patch("{}/atualized/id/{}".format(self.api, self.aluno.matricula),{"atualized": False, "caracteres": tobase64})

    def importFaces(self) -> any:
        try:
            backup = np.load(self.faces_armazenadas)
            faces = []

            for item in backup.files:
                if backup[item] != []:
                    faces.append(backup[item])
            return faces
        except:
            print("Não foi possivel ler os dados")

    def loadFaces(self) -> any:
        return np.load(self.faces_armazenadas)