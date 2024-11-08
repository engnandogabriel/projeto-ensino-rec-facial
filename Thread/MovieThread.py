from PyQt5.QtCore import QThread, pyqtSignal
import time
import numpy as np

class MovieThread(QThread):
    frame_ready = pyqtSignal(np.ndarray)  # Emite o frame capturado

    def __init__(self, camera):
        super().__init__()
        self.camera = camera
        self.running = True

    def run(self):
        while self.running:
            frame = self.camera.get_frame()
            if frame is not None:
                self.frame_ready.emit(frame)  # Emite o frame para a interface
            time.sleep(0.03)  # Ajusta para 30 FPS

    def stop(self):
        self.running = False
