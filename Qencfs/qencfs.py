# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qencfs.ui'
#
# Created: Tue Sep  1 19:16:32 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 455)
        self.toolBox = QtGui.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 371, 73))
        self.page.setObjectName("page")
        self.groupBox = QtGui.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(0, -1, 371, 71))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 92, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 30, 92, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 30, 92, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 371, 73))
        self.page_2.setObjectName("page_2")
        self.groupBox_3 = QtGui.QGroupBox(self.page_2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 0, 371, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 30, 92, 26))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_8.setGeometry(QtCore.QRect(140, 30, 92, 26))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_9.setGeometry(QtCore.QRect(270, 30, 92, 26))
        self.pushButton_9.setObjectName("pushButton_9")
        self.toolBox.addItem(self.page_2, "")
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 381, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 30, 92, 26))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 30, 92, 26))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 30, 92, 26))
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 70, 231, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 100, 241, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(27, 0, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.toolBox_2 = QtGui.QToolBox(Form)
        self.toolBox_2.setGeometry(QtCore.QRect(10, 280, 371, 161))
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 361, 93))
        self.page_3.setObjectName("page_3")
        self.checkBox_3 = QtGui.QCheckBox(self.page_3)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 50, 121, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtGui.QCheckBox(self.page_3)
        self.checkBox_4.setGeometry(QtCore.QRect(150, 50, 91, 23))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton_10 = QtGui.QPushButton(self.page_3)
        self.pushButton_10.setGeometry(QtCore.QRect(260, 50, 92, 26))
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit = QtGui.QLineEdit(self.page_3)
        self.lineEdit.setGeometry(QtCore.QRect(160, 0, 191, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtGui.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 111, 17))
        self.label_2.setObjectName("label_2")
        self.checkBox_5 = QtGui.QCheckBox(self.page_3)
        self.checkBox_5.setGeometry(QtCore.QRect(20, 20, 121, 23))
        self.checkBox_5.setObjectName("checkBox_5")
        self.toolBox_2.addItem(self.page_3, "")
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 361, 93))
        self.page_4.setObjectName("page_4")
        self.textBrowser = QtGui.QTextBrowser(self.page_4)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 361, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.toolBox_2.addItem(self.page_4, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(1)
        self.toolBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Create & delete encrypted local filesystems", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Encoding", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("Form", "Local Filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Create & delete encrypted device filesystems", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Form", "Encoding", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Form", "Device Filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Mount and umoint encrypted filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Mount", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "Unmount", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Open encrypted folder after mounting", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Form", "Hide menu and sidebar on filemanager", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "qEncrypted Filesystem Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Form", "Start with system", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Form", "Start trayed", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Form", "Hide in panel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Enter password", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setText(QtGui.QApplication.translate("Form", "Show password", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), QtGui.QApplication.translate("Form", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), QtGui.QApplication.translate("Form", "Actions Log", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
