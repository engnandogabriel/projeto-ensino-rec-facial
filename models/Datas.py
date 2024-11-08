import datetime

import numpy as np
from services.AlunoService import AlunoService

class Datas:
    def __init__(self):
        # self.api = "https://web-production-9f8c8.up.railway.app/reconhecimento"
        self.api = "http://localhost:8080/reconhecimento"
        #self.requisicao = requests.get(self.api).json()
        self.alunosService = AlunoService()
        self.alunos = []
        
    def getAlunos(self):
        try:
            return self.alunosService.getAlunos()
        except:
            print("Fecth was ocorrued a error")
            
    def get_data(self):
        currentDate = datetime.date.today() 
        currentDate = currentDate.strftime("%Y-%m-%d")
        return currentDate

    def get_data_complete(self):
        dateComplete = datetime.datetime.now()
        dateComplete = dateComplete.strftime("%Y-%m-%dT%H:%M")
        return dateComplete

    def ImportarAlunos(self):
        with open("data/backup/nomes.txt", "r") as arquivo:
            texto = arquivo.read()
            arquivo.close()
            alunos = texto.split("/")  # Divide o arquivo em uma lista com a seguinte estrutura: [matricula1:aluno1, matricula2:aluno2,..., matriculaN:alunoN, NULL]
            alunos.pop()  # Remove o valor nulo da última posição da lista
            # Separa cada item da lista alunos em dois: matricula, nome. Em seguida, armazena na variável nomes apenas o nome do aluno
            for aluno in alunos:
                self.matriculas.append(aluno.split(":")[0])
                self.nomes.append(aluno.split(":")[1])

    def importaFaces(self):
        try:
            backup = np.load("data/backup/faces.npz")
            faces = []

            for item in backup.files:
                if backup[item] != []:
                    faces.append(backup[item])
            return faces
        except:
            print("Não foi possivel ler os dados")
        
    def get_dados(self):
        return self.requisicao