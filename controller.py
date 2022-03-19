from sre_parse import State
from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_Dialog
from PyQt5.QtGui import QPixmap
import sys
from urllib import request

class MainWindow_controller(QtWidgets.QDialog):
    state = 0
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super(MainWindow_controller,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.onAccepted)
        self.ui.buttonBox.rejected.connect(self.onCancelled)
        
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.textBrowser.setText('Happy World!')

    def disp(self , s):
        self.ui.textBrowser.setText(s)
        
    def onAccepted(self):
        self.state = 1
    
    def onCancelled(self):
        self.state = 0
        
    def SetImage(self , url):
        
        data = request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.ui.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())
