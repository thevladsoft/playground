# -*- coding: utf-8 -*-

#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#* http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles Barcza *
#*************************************************************************************(c)2002-2016********

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(427, 455)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        Dialog.setFont(font)
        self.startButton = QtGui.QPushButton(Dialog)
        self.startButton.setEnabled(True)
        self.startButton.setGeometry(QtCore.QRect(130, 410, 158, 34))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 290, 401, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.toolBox = QtGui.QToolBox(Dialog)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 421, 191))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Sans"))
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_1 = QtGui.QWidget()
        self.page_1.setGeometry(QtCore.QRect(0, 0, 411, 129))
        self.page_1.setAutoFillBackground(False)
        self.page_1.setObjectName(_fromUtf8("page_1"))
        self.groupBox = QtGui.QGroupBox(self.page_1)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.isoBttn = QtGui.QPushButton(self.groupBox)
        self.isoBttn.setGeometry(QtCore.QRect(40, 30, 141, 25))
        self.isoBttn.setObjectName(_fromUtf8("isoBttn"))
        self.overlayTitle = QtGui.QGroupBox(self.page_1)
        self.overlayTitle.setGeometry(QtCore.QRect(0, 80, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.overlayTitle.setFont(font)
        self.overlayTitle.setObjectName(_fromUtf8("overlayTitle"))
        self.downloadGroup = QtGui.QGroupBox(self.page_1)
        self.downloadGroup.setGeometry(QtCore.QRect(220, 80, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.downloadGroup.setFont(font)
        self.downloadGroup.setObjectName(_fromUtf8("downloadGroup"))
        self.downloadCombo = QtGui.QComboBox(self.downloadGroup)
        self.downloadCombo.setGeometry(QtCore.QRect(10, 20, 181, 22))
        self.downloadCombo.setObjectName(_fromUtf8("downloadCombo"))
        self.groupBox_2 = QtGui.QGroupBox(self.page_1)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 0, 191, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 161, 51))
        self.label_3.setStyleSheet(_fromUtf8("font: 9pt \"Sans Serif\";\n"
"text-decoration: underline;"))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/liveusb-header.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.toolBox.addItem(self.page_1, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 411, 129))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label = QtGui.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(40, 0, 321, 41))
        self.label.setStyleSheet(_fromUtf8("font: 75 11pt \"Nimbus Sans L\";\n"
"font: italic 14pt \"Sans Serif\";"))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/liveusb-header.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 200, 401, 23))
        self.progressBar.setProperty(_fromUtf8("value"), 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar_3 = QtGui.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(10, 260, 401, 23))
        self.progressBar_3.setProperty(_fromUtf8("value"), 0)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.progressBar_2 = QtGui.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 230, 401, 23))
        self.progressBar_2.setProperty(_fromUtf8("value"), 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "blackPanther OS - GeekBench GUI", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setWhatsThis(QtGui.QApplication.translate("Dialog", "This button will begin the LiveUSB creation process.  This entails optionally downloading a release (if an existing one wasn\'t selected),  extracting the ISO to the USB device, creating the persistent overlay, and installing the bootloader.", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("Dialog", "Run Benchark", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setWhatsThis(QtGui.QApplication.translate("Dialog", "This is the status console, where all messages get written to.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setWhatsThis(QtGui.QApplication.translate("Dialog", "This button allows you to browse for an existing Live CD ISO that you have previously downloaded.  If you do not select one, a release will be downloaded for you automatically.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "GeekBench Path: /usr/bin/geekbench", None, QtGui.QApplication.UnicodeUTF8))
        self.isoBttn.setText(QtGui.QApplication.translate("Dialog", "Manual select", None, QtGui.QApplication.UnicodeUTF8))
        self.isoBttn.setShortcut(QtGui.QApplication.translate("Dialog", "Alt+B", None, QtGui.QApplication.UnicodeUTF8))
        self.overlayTitle.setWhatsThis(QtGui.QApplication.translate("Dialog", "By allocating extra space on your USB stick for a persistent overlay, you will be able to store data and make permanent modifications to your live operating system.  Without it, you will not be able to save data that will persist after a reboot.", "comment!", QtGui.QApplication.UnicodeUTF8))
        self.overlayTitle.setTitle(QtGui.QApplication.translate("Dialog", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadGroup.setWhatsThis(QtGui.QApplication.translate("Dialog", "If you do not select an existing Live CD, the selected release will be downloaded for you.", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadGroup.setTitle(QtGui.QApplication.translate("Dialog", "Last Benchmark\'s Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">blackPanther Europe</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"www.blackpantheros.eu\"><span style=\" text-decoration: underline; color:#0000c0;\">www.blackpantheros.eu</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:info@blackpantheros.eu\"><span style=\" text-decoration: underline; color:#0000c0;\">info@blackpantheros.eu</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:14pt; font-weight:400; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> blackPanther OS Benchmark Tool </p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">based on GeekBench 3</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Dialog", "Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setWhatsThis(QtGui.QApplication.translate("Dialog", "This is the progress bar that will indicate how far along in the LiveUSB creation process you are", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar_3.setWhatsThis(QtGui.QApplication.translate("Dialog", "This is the progress bar that will indicate how far along in the LiveUSB creation process you are", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar_2.setWhatsThis(QtGui.QApplication.translate("Dialog", "This is the progress bar that will indicate how far along in the LiveUSB creation process you are", None, QtGui.QApplication.UnicodeUTF8))

#import resources_rc
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

