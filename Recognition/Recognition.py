import datetime
import numpy as np
import face_recognition as fr
from PyQt5.QtCore import QTimer, QRunnable, QThreadPool
from Thread.LogsThread import LogThread
from models.Logs import Logs
from services.AlunoService import AlunoService
from models.Faces import Faces
import uuid

class Recognition:
    def __init__(self, camera, formulario):
        self.localizacoesFaces = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.threaFuncion)
        self.camera = camera
        self.user_id, self.faces = Faces().importFaces()
        self.alunos = AlunoService().getAlunos()
        self.logs = Logs()
        self.formulario = formulario
        self.name = ""
        self.course = ""
        self.registration_code = ""

    def start_recognition(self):
        processo = True
        frame_formated = self.camera.TratarFrame()
        if not isinstance(frame_formated, np.ndarray):
            return 
        if processo is True:
            face_location = fr.face_locations(frame_formated)
            faces = fr.face_encodings(frame_formated, face_location)
            for face in faces:
                correspodem = fr.compare_faces(self.faces, face, tolerance=0.45)
                if True in correspodem:
                    primeiraCorresponcia = correspodem.index(True)
                    user_id = self.user_id[primeiraCorresponcia]
                    aluno = next(filter(lambda aluno: aluno.user_id == user_id, self.alunos), None)
                    self.name = aluno.name
                    self.course = aluno.course
                    self.registration_code = aluno.registration_code
                    if(self.alunos[primeiraCorresponcia].recognized is False):
                        self.logs.user_id = self.alunos[primeiraCorresponcia].user_id
                        self.logs.recognation_id = uuid.uuid1()
                        self.logs.access_time = datetime.datetime.now()
                        self.logs.status = "recongnation"
                        self.alunos[primeiraCorresponcia].recognized = True
                        LogThread(self.logs).start()
                    self.exebirDadosInterfcae()
                else:
                    self.name = "Não Conhecido"
                    self.course = "Não Conhecido"
                    self.registration_code = "Não Conhecido"
                    self.exebirDadosInterfcae()
            return
    
    def exebirDadosInterfcae(self):
        self.formulario.recebe_nome.setText(self.name)
        self.formulario.recebe_matricula.setText(self.registration_code)
        self.formulario.recebe_curso.setText(self.course)


    def reconhecimento(self):
        self.camera.startMovie()
        self.timer.start(1000)

    def threaFuncion(self):
        frame = self.camera.TratarFrame()
        if frame is None:
            print("Erro: Não foi possível obter um frame válido.")
            self.name = "SEM ROSTO"
            self.registration_code = "SEM ROSTO"
            self.course = "SEM ROSTO"
            self.exebirDadosInterfcae()
            return  
        self.localizacoesFaces = fr.face_locations(frame)
        if self.localizacoesFaces:
            recoThread = ReconhecimentoThread(self)
            QThreadPool.globalInstance().start(recoThread)
        else:
            self.name = "SEM ROSTO"
            self.registration_code = "SEM ROSTO" 
            self.course = "SEM ROSTO"
            self.exebirDadosInterfcae()

        
class ReconhecimentoThread(QRunnable):
    def __init__(self, reconhecimento) -> None:
        super().__init__()
        self.reconhecimento = reconhecimento

    def run(self) -> None:
        self.reconhecimento.start_recognition()