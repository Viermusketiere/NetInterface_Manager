# This Python file uses the following encoding: utf-8
from cProfile import label
import sys
import networkWin as nw
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFormLayout, QWidget, QFrame

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_mainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # self.ui.pushButton.clicked.connect(self.printIf)
        self.ui.actionRefresh.triggered.connect(self.printIf)

    def printIf(parent):
        interfaces = nw.getAdapterInfo()

        frame = QFrame(parent.ui.scrollAreaWidgetContents_Adapters)
        frame.show()
        formLayout1 = QFormLayout(frame)
        
        labelIP1 = QLabel()
        labelIP1.setText('IP')
        labelIP1.show()
        labelSM1 = QLabel()
        labelSM1.setText('Subnetzmaske')
        labelSM1.show()
        formLayout1.addWidget(labelIP1)
        formLayout1.addWidget(labelSM1)

        # parent.ui.scrollAreaWidgetContents_Adapters.setWidget(formLayout1)


        print("Done")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

