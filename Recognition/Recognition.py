import datetime
import numpy as np
import face_recognition as fr
from PyQt5.QtCore import QTimer, QRunnable, QThreadPool
from models.Logs import Logs
from services.AlunoService import AlunoService
from services.FacesService import FacesService
from models.Faces import Faces

class Recognition:
    def __init__(self, camera, formulario):
        self.localizacoesFaces = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.threaFuncion)
        self.camera = camera
        self.faces_know = Faces().importFaces()
        self.alunos = AlunoService().getAlunos()
        self.formulario = formulario
        self.name = ""
        self.course = ""
        self.registration_code = ""

    def start_recognition(self):
        processo = True
        frame_formated = self.camera.TratarFrame()
        if processo is True:
            face_location = fr.face_locations(frame_formated)
            faces = fr.face_encodings(frame_formated, face_location)
            for face in faces:
                correspodem = fr.compare_faces(self.faces_know, face, tolerance=0.45)
                if True in correspodem:
                    print("reconhecido")
                    primeiraCorresponcia = correspodem.index(True)
                    self.name = self.alunos[primeiraCorresponcia].name
                    self.course = self.alunos[primeiraCorresponcia].course
                    self.registration_code = self.alunos[primeiraCorresponcia].registration_code
                    self.exebirDadosInterfcae()
            return
    
    def exebirDadosInterfcae(self):
        self.formulario.recebe_nome.setText(self.name)
        self.formulario.recebe_matricula.setText(self.registration_code)
        self.formulario.recebe_curso.setText(self.course)
        # self.formulario.recebe_status.setText(self.registrado)
        # self.formulario.recebe_horario.setText(self.hora)


    def reconhecimento(self):
        self.camera.startMovie()
        self.timer.start(1000)

    def threaFuncion(self):
        self.localizacoesFaces = fr.face_locations(self.camera.TratarFrame())
        if self.localizacoesFaces:
            recoThread = ReconhecimentoThread(self)
            QThreadPool.globalInstance().start(recoThread)
            # pool.start(recoThread)
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