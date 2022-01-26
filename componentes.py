
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DescargaDePDF(object):
    def setupUi(self, DescargaDePDF):
        DescargaDePDF.setObjectName("DescargaDePDF")
        DescargaDePDF.resize(500, 230)
        DescargaDePDF.setStyleSheet("#fondo {\n"
"    background-color: #2c3e50;\n"
"}\n"
"\n"
"#titulo {\n"
"    color: #ecf0f1;\n"
"    font-size: 22px;\n"
"    font-family: Poppins;\n"
"}\n"
"\n"
"#btn {\n"
"    border-style: None;\n"
"    font-size: 16px;\n"
"    font-family: Poppins;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #f1c40f;\n"
"    color: #f1c40f; \n"
"}\n"
"\n"
"#btn::hover {\n"
"    border-style: None;\n"
"    background-color: #1abc9c;\n"
"    font-size: 16px;\n"
"    font-family: Poppins;\n"
"    color: #ecf0f1; \n"
"    border-radius: 5px;\n"
"    border: 2px solid #bdc3c7;\n"
"}\n"
"\n"
"#info {\n"
"    font-family: Poppins;\n"
"    color: #ecf0f1;\n"
"    font-size: 14px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(DescargaDePDF)
        self.centralwidget.setObjectName("centralwidget")
        self.fondo = QtWidgets.QFrame(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 500, 230))
        self.fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fondo.setObjectName("fondo")
        self.titulo = QtWidgets.QLabel(self.fondo)
        self.titulo.setGeometry(QtCore.QRect(0, 10, 501, 51))
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setIndent(0)
        self.titulo.setObjectName("titulo")
        self.btn = QtWidgets.QPushButton(self.fondo)
        self.btn.setGeometry(QtCore.QRect(160, 90, 181, 41))
        self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn.setObjectName("btn")
        self.info = QtWidgets.QLabel(self.fondo)
        self.info.setGeometry(QtCore.QRect(70, 160, 361, 31))
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        DescargaDePDF.setCentralWidget(self.centralwidget)

        self.retranslateUi(DescargaDePDF)
        QtCore.QMetaObject.connectSlotsByName(DescargaDePDF)

    def retranslateUi(self, DescargaDePDF):
        _translate = QtCore.QCoreApplication.translate
        DescargaDePDF.setWindowTitle(_translate("DescargaDePDF", "MainWindow"))
        self.titulo.setText(_translate("DescargaDePDF", "DESCARGA DE PDFS DESDE TSDOCS"))
        self.btn.setText(_translate("DescargaDePDF", "Iniciar"))
        # self.info.setText(_translate("DescargaDePDF", "Descargando informacion ..."))
