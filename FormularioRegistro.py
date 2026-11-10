import sys

from PyQt6.QtWidgets import *


class FiestraPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.etiquetaNombre = QLabel("Nombre: ")
        self.nombre = QLineEdit()

        lineaNombre = QHBoxLayout()
        lineaNombre.addWidget(self.etiquetaNombre)
        lineaNombre.addWidget(self.nombre)


        self.etiquetaCurso = QLabel("Curso: ")
        self.curso = QComboBox()
        self.curso.addItems(["1DAM","2DAM","1DAW","2DAW"])

        lineaCurso = QHBoxLayout()
        lineaCurso.addWidget(self.etiquetaCurso)
        lineaCurso.addWidget(self.curso)


        self.etiquetaCondiciones = QLabel("Acepto las condiciones: ")
        self.condiciones = QCheckBox()

        lineaCondiciones = QHBoxLayout()
        lineaCondiciones.addWidget(self.etiquetaCondiciones)
        lineaCondiciones.addWidget(self.condiciones)


        self.botonEnviar = QPushButton("Enviar")
        self.botonEnviar.clicked.connect(self.enviar)



        principal = QVBoxLayout()
        principal.addLayout(lineaNombre)
        principal.addLayout(lineaCurso)
        principal.addLayout(lineaCondiciones)
        principal.addWidget(self.botonEnviar)

        self.setLayout(principal)


    def enviar(self):
        print(f"Formulario Enviado... {self.nombre.text()} de {self.curso.currentText()}")


        self.nombre.clear()
        self.curso.setCurrentIndex(0)


app = QApplication(sys.argv)
FP = FiestraPrincipal()
FP.show()
app.exec()