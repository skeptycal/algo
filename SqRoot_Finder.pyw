import math
from PySide import QtGui, QtCore
import sys


class SqRoot(QtGui.QMainWindow):
    def __init__(self):
        super(SqRoot, self).__init__()

        self.version = 'SqRoot Finder v1.0'
        self.UsrI()

    def UsrI(self):
        def root():
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("Please enter a valid number.")
            INPUT = textbox1.text()
            try:
                INPUT2 = float(INPUT)
            except ValueError:
                msgBox.exec_()
            label2.setText("The Square Root of %s is: " % INPUT2)
            ans = math.sqrt(INPUT2)
            ans_str = str(ans)
            label1.setText(ans_str)

        ExitAction = QtGui.QAction('&Exit', self)
        ExitAction.setShortcut('Ctrl+Q')
        ExitAction.triggered.connect(self.close)
        ExitAction.setStatusTip('Quits the application.')

        menuBar1 = self.menuBar()
        menu_one = menuBar1.addMenu('&File')
        menu_one.addAction(ExitAction)

        label1 = QtGui.QLabel(self)
        label1.setText("0.0")
        QtCore.QCoreApplication.processEvents()
        label1.resize(280, 27)
        label1.setStatusTip("Answer is shown in this line.")
        label1.move(105, 75)

        statusBar1 = self.statusBar()

        label2 = QtGui.QLabel(self)
        label2.setText("The square root of 0 is:")
        QtCore.QCoreApplication.processEvents()
        label2.resize(280, 27)
        label2.setStatusTip("Question is shown in this line.")
        label2.move(10, 60)

        button1 = QtGui.QPushButton('=Square Root', self)
        button1.resize(button1.sizeHint())
        button1.move(217, 62)
        button1.clicked.connect(root)
        button1.setStatusTip('Click to find SqRoot.')

        textbox1 = QtGui.QLineEdit(self)
        textbox1.resize(284, 27)
        textbox1.move(8, 30)
        textbox1.setToolTip("Enter a number (Decimal/Integer)")
        textbox1.setStatusTip('Enter a number (Decimal/Integer)')

        self.setWindowTitle(self.version)
        self.setFixedSize(300, 130)
        self.setStatusTip("Ready")
        self.show()


def main():
    application = QtGui.QApplication(sys.argv)
    ex = SqRoot()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
