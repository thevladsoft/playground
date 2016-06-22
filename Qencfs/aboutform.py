# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

#    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
#        QDialog.__init__(self,parent,name,modal,fl)

#class Ui_AboutForm(object):
#    def setupUi(self, AboutForm):
class NAboutForm(QtGui.QMainWindow):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QtGui.QMainWindow.__init__(self,parent)

        AboutForm.setObjectName("AboutForm")
        if not name:
            self.setObjectName("AboutForm")

        AboutForm.setEnabled(True)
        #AboutForm.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(400)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(AboutForm.sizePolicy().hasHeightForWidth())
        AboutForm.setSizePolicy(sizePolicy)

        #AboutForm.setObjectName("AboutForm")
        #AboutForm.resize(400, 300)

        self.pushButton = QtGui.QPushButton(AboutForm)
        self.pushButton.setGeometry(QtCore.QRect(160, 250, 92, 26))
        self.pushButton.setObjectName("pushButton")
        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),QtGui.qApp.quit)

        self.label = QtGui.QLabel(AboutForm)
        self.label.setGeometry(QtCore.QRect(150, 80, 231, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(AboutForm)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 341, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame = QtGui.QFrame(AboutForm)
        self.frame.setGeometry(QtCore.QRect(10, 50, 121, 121))
        self.frame.setAutoFillBackground(True)
        self.frame.setStyleSheet("background-image: url(file_locked.png);")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtGui.QLabel(AboutForm)
        self.label_3.setGeometry(QtCore.QRect(150, 100, 231, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(AboutForm)
        self.label_4.setGeometry(QtCore.QRect(150, 120, 231, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(AboutForm)
        self.label_5.setGeometry(QtCore.QRect(150, 60, 231, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(AboutForm)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 361, 71))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        AboutForm.setWindowTitle(QtGui.QApplication.translate("AboutForm", "qEncfm About", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("AboutForm", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AboutForm", "Mail: kbarcza[]blackpanther.hu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AboutForm", "About qEncrypted Filesystem Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AboutForm", "Company: blackPanther Europe", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AboutForm", "Webpage: http://www.blackpanther.hu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AboutForm", "Developer: Charles Barcza", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AboutForm", "qEncfsm a Qt4 frontend to encfs encryption utility. \nI'm inspirated by kencfs2 and I used more code from\n Supported distro: blackPanther OS ", None, QtGui.QApplication.UnicodeUTF8))

#import images_rc
#import systray_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #QtCore.QObject.connect(app,QtCore.SIGNAL("lastWindowClosed()"),app,SLOT("quit()"))
    AboutForm = QtGui.QDialog()
    ui = NAboutForm()
    #ui.setupUi(NAboutForm)
    AboutForm.show()
    sys.exit(app.exec_())
    #app.setMainWidget(w)
    #w.show()
    #app.exec_loop()

