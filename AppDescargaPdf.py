from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread
from componentes import Ui_DescargaDePDF
import sys

from inicio import pdf_cap


class ProcesoPrincipal(QThread):
     def __init__(self, componentes):
          super().__init__()
          
          self.componentes = componentes
     
     def run(self):
          self.componentes.componentes.info.setText("Iniciando Descarga ...")
          self.proceso = pdf_cap()
          if self.proceso == True:
               self.componentes.componentes.info.setText("FIN PROCESO!!")
          else:
               self.componentes.componentes.info.setText("Algo salio mal con el Excel.")




class DescargaPDF(QMainWindow):
     def __init__(self):
          super().__init__()

          self.componentes = Ui_DescargaDePDF()
          self.componentes.setupUi(self)
          self.componentes.btn.clicked.connect(self.boton)
     
     def boton(self):
          
          self.hilo = ProcesoPrincipal(self)
          self.hilo.start()


if __name__ == "__main__":
     app = QApplication(sys.argv)
     aplicacion = DescargaPDF()
     aplicacion.show()
     sys.exit(app.exec_())

