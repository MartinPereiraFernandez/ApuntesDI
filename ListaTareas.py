import sys

from PyQt6.QtWidgets import *


class FiestraPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.tarjetaTarea = QLabel("Tarea: ")
        self.tarea = QLineEdit()
        lineaTarea = QHBoxLayout()
        lineaTarea.addWidget(self.tarjetaTarea)
        lineaTarea.addWidget(self.tarea)

        self.botonAnadir = QPushButton("Anadir")
        self.botonAnadir.clicked.connect(self.anadir)

        self.listaTareas = QListWidget()

        self.botonEliminar = QPushButton("Eliminar")

        self.botonEliminarLista = QPushButton("Eliminar todos")
        self.botonEliminarLista.clicked.connect(self.eliminarTodos)

        lineaBotonesEliminar = QHBoxLayout()
        lineaBotonesEliminar.addWidget(self.botonEliminar)
        lineaBotonesEliminar.addWidget(self.botonEliminarLista)

        self.numeroTareas = QLabel(f"Numero de Tareas: {self.listaTareas.count()}")

        principal = QVBoxLayout()
        principal.addLayout(lineaTarea)
        principal.addWidget(self.botonAnadir)
        principal.addWidget(self.listaTareas)
        principal.addLayout(lineaBotonesEliminar)
        principal.addWidget(self.numeroTareas)

        self.setLayout(principal)

    def anadir(self):
        texto = self.tarea.text().strip()
        self.listaTareas.addItem(texto)
        self.tarea.clear()
        self.actualizarContador()


    def eliminarTodos(self):
        self.listaTareas.clear()
        self.actualizarContador()


    def actualizarContador(self):
        self.numeroTareas.setText(f"Numero de Tareas: {self.listaTareas.count()}")


app =QApplication(sys.argv)
FP = FiestraPrincipal()
FP.show()
app.exec()
