# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_NameFormater(object):
    def setupUi(self, NameFormater):
        if not NameFormater.objectName():
            NameFormater.setObjectName(u"NameFormater")
        NameFormater.resize(347, 177)
        self.centralwidget = QWidget(NameFormater)
        self.centralwidget.setObjectName(u"centralwidget")
        self.inputLineEdit = QLineEdit(self.centralwidget)
        self.inputLineEdit.setObjectName(u"inputLineEdit")
        self.inputLineEdit.setGeometry(QRect(100, 40, 141, 22))
        self.capitalizeButton = QPushButton(self.centralwidget)
        self.capitalizeButton.setObjectName(u"capitalizeButton")
        self.capitalizeButton.setGeometry(QRect(70, 80, 75, 24))
        self.reverseButton = QPushButton(self.centralwidget)
        self.reverseButton.setObjectName(u"reverseButton")
        self.reverseButton.setGeometry(QRect(200, 80, 75, 24))
        self.outputLabel = QLabel(self.centralwidget)
        self.outputLabel.setObjectName(u"outputLabel")
        self.outputLabel.setGeometry(QRect(130, 10, 81, 16))
        NameFormater.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NameFormater)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 347, 22))
        NameFormater.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NameFormater)
        self.statusbar.setObjectName(u"statusbar")
        NameFormater.setStatusBar(self.statusbar)

        self.retranslateUi(NameFormater)

        QMetaObject.connectSlotsByName(NameFormater)
    # setupUi

    def retranslateUi(self, NameFormater):
        NameFormater.setWindowTitle(QCoreApplication.translate("NameFormater", u"MainWindow", None))
        self.capitalizeButton.setText(QCoreApplication.translate("NameFormater", u"Capitalize", None))
        self.reverseButton.setText(QCoreApplication.translate("NameFormater", u"Reverse", None))
        self.outputLabel.setText(QCoreApplication.translate("NameFormater", u"TextLabel", None))
    # retranslateUi

