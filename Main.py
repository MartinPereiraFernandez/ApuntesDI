import sys

from PyQt6.QtWidgets import *


class FiestraPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.texto1 = QLabel("Texto 1")
        self.texto2 = QLabel("Texto 2")

        bandejaHorizontal = QHBoxLayout()
        bandejaHorizontal.addWidget(self.texto1)
        bandejaHorizontal.addWidget(self.texto2)

        self.setLayout(bandejaHorizontal)

app = QApplication(sys.argv)
FP = FiestraPrincipal()
FP.show()
app.exec()
