from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class FenPrincipal(QMainWindow):
  def __init__(self):
    super(FenPrincipal, self).__init__()
    self.setWindowIcon(QtGui.QIcon("favicon.ico"))
    self.navigateur = QWebEngineView()
    self.navigateur.setUrl(QUrl("http://aoje.netlify.app"))
    self.setCentralWidget(self.navigateur)
    self.showMaximized()

app = QApplication(sys.argv)
QApplication.setApplicationName("Aoje")
fenetre = FenPrincipal()
app.exec()
