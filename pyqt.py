import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    #win.setGeometry(xpos,ypos,width,height)
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("HEllo, ITS EE")

    label = QtWidgets.QLabel(win)
    label.setText("The Label")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())
window()