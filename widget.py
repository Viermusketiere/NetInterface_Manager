# This Python file uses the following encoding: utf-8
import sys
import psutil

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.printIf)

    def printIf(arggg):
        addrs = psutil.net_if_addrs()
        # print(addrs.keys())

        for entry in addrs:
            print(entry)
            for value in range(0, len(addrs[entry]) -1):
                if addrs[entry][value][0] == -1:
                    print("Link")
                if addrs[entry][value][0] == 2:
                    print("IPv4")
                    print(addrs[entry][value][1])   #IP
                    print(addrs[entry][value][2])   #SN Mask
                if addrs[entry][value][0] == 23:
                    print("IPv6")
                    print(addrs[entry][value][1])   #IP
                print(" ")
            print("======================================")

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

