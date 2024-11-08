from Recognition.Camera import Camera
from Recognition.Recognition import Recognition
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
formulario = uic.loadUi('tela.ui')

camera = Camera(0,formulario)

reconhecimento_facial = Recognition(camera, formulario)


#acoes da interface
# formulario.atualizar.clicked.connect(reconhecimento_facial.main)
formulario.start.clicked.connect(reconhecimento_facial.reconhecimento)


formulario.show()
app.exec()