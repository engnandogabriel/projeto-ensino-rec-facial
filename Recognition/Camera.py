import cv2
import face_recognition as fr
from PyQt5.QtCore import QThread, QTimer
from PyQt5 import QtGui

class Camera:
    def __init__(self, cam_num, formulario):
        self.cap = cv2.VideoCapture(cam_num)
        self.formulario = formulario
        self.last_frame = None
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.updateMovie)

    def getFrame(self):
        ret, self.last_frame = self.cap.read()
        return self.last_frame

    def showCamera(self):
        cv2.imshow("Video da webcam", self.last_frame)

    def acquireMovie(self, num_frames):
        movie = []
        for _ in range(num_frames):
            movie.append(self.getFrame())
        return movie

    def stopCamera(self):
        self.cap.release()

    def TratarFrame(self):
        # Reduz o tamanho do Frame para aprimorar performance
        frame_formatado = cv2.resize(self.getFrame(), (0, 0), fx=0.5, fy=0.5)
        frame_formatado = frame_formatado[:, :, :: 1]
        return frame_formatado
    
    def updateMovie(self):
        frame = self.TratarFrame()
        larg = 720
        alt = int(frame.shape[0]/frame.shape[1]*larg)
        localizacoesFaces = fr.face_locations(frame)

        face_cascade = cv2.CascadeClassifier('deteccao/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('deteccao/haarcascade_eye.xml')

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),1)

        frame = cv2.resize(frame, (larg, alt), interpolation = cv2.INTER_AREA)
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        self.formulario.camera.setPixmap(QtGui.QPixmap(qImg))

    def startMovie(self):
        self.movie_thread = MovieThread(self)
        self.movie_thread.start()
        self.update_timer.start(30)

class MovieThread(QThread):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera

    def run(self):
        self.camera.acquireMovie(200)