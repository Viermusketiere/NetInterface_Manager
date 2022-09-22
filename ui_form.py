# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QScrollArea, QSizePolicy, QSplitter,
    QToolBar, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1101, 748)
        self.actionImport_Presets = QAction(mainWindow)
        self.actionImport_Presets.setObjectName(u"actionImport_Presets")
        self.actionExport_Presets = QAction(mainWindow)
        self.actionExport_Presets.setObjectName(u"actionExport_Presets")
        self.actionRefresh = QAction(mainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.layoutPreset = QVBoxLayout(self.verticalLayoutWidget)
        self.layoutPreset.setSpacing(6)
        self.layoutPreset.setContentsMargins(11, 11, 11, 11)
        self.layoutPreset.setObjectName(u"layoutPreset")
        self.layoutPreset.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 535, 678))
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 100, 235, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setSpacing(6)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.layoutPreset.addWidget(self.scrollArea)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.layoutAdapters = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layoutAdapters.setSpacing(6)
        self.layoutAdapters.setContentsMargins(11, 11, 11, 11)
        self.layoutAdapters.setObjectName(u"layoutAdapters")
        self.layoutAdapters.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_Adapters = QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea_Adapters.setObjectName(u"scrollArea_Adapters")
        self.scrollArea_Adapters.setWidgetResizable(True)
        self.scrollAreaWidgetContents_Adapters = QWidget()
        self.scrollAreaWidgetContents_Adapters.setObjectName(u"scrollAreaWidgetContents_Adapters")
        self.scrollAreaWidgetContents_Adapters.setGeometry(QRect(0, 0, 535, 678))
        self.scrollArea_Adapters.setWidget(self.scrollAreaWidgetContents_Adapters)

        self.layoutAdapters.addWidget(self.scrollArea_Adapters)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(mainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1101, 22))
        self.menuMen = QMenu(self.menuBar)
        self.menuMen.setObjectName(u"menuMen")
        mainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(mainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        self.mainToolBar.setLayoutDirection(Qt.RightToLeft)
        mainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)

        self.menuBar.addAction(self.menuMen.menuAction())
        self.menuMen.addAction(self.actionImport_Presets)
        self.menuMen.addAction(self.actionExport_Presets)
        self.mainToolBar.addAction(self.actionRefresh)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Network Interface Manager", None))
        self.actionImport_Presets.setText(QCoreApplication.translate("mainWindow", u"Import Presets", None))
        self.actionExport_Presets.setText(QCoreApplication.translate("mainWindow", u"Export Presets", None))
        self.actionRefresh.setText(QCoreApplication.translate("mainWindow", u"Refresh", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"IP", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Subnetzmaske", None))
        self.menuMen.setTitle(QCoreApplication.translate("mainWindow", u"Presets", None))
    # retranslateUi

