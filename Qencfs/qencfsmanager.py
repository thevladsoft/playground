#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
#*********************************************************************************************************
#*   __     __               __     ______                __   __                      _______ _______   *
#*  |  |--.|  |.---.-..----.|  |--.|   __ \.---.-..-----.|  |_|  |--..-----..----.    |       |     __|  *
#*  |  _  ||  ||  _  ||  __||    < |    __/|  _  ||     ||   _|     ||  -__||   _|    |   -   |__     |  *
#*  |_____||__||___._||____||__|__||___|   |___._||__|__||____|__|__||_____||__|      |_______|_______|  *
#* http://www.blackpantheros.eu | http://www.blackpanther.hu - kbarcza[]blackpanther.hu * Charles Barcza *
#*************************************************************************************(c)2002-2016********

## Written by Charles Barcza kbarcza@blackpanther.hu
##    blackPanther OS - www.blackpanther.hu
##

import sys, re, os, string, signal
import tempfile, shutil
from time import sleep

from PyQt4 import QtCore, QtGui

from myprocess import *

import aboutform
#
#icon = "/usr/share/qEfm/file_locked.png"

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.createActions()
        self.createTrayIcon()
        
        self.trayIcon.show()

        Form.setObjectName("Form")
        Form.resize(397, 455)
        self.toolBox = QtGui.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 371, 73))
        self.page.setObjectName("page")
        self.groupLocalFS = QtGui.QGroupBox(self.page)
        self.groupLocalFS.setGeometry(QtCore.QRect(0, -1, 371, 71))
        self.groupLocalFS.setObjectName("groupLocalFS")

        self.createButton = QtGui.QPushButton(self.groupLocalFS)
        self.createButton.setGeometry(QtCore.QRect(10, 30, 92, 26))
        self.createButton.setObjectName("createButton")
        self.connect(self.createButton,QtCore.SIGNAL("clicked()"),self.slotCreate)

        self.encodingButton = QtGui.QPushButton(self.groupLocalFS)
        self.encodingButton.setGeometry(QtCore.QRect(150, 30, 92, 26))
        self.encodingButton.setObjectName("encodingButton")
        self.connect(self.encodingButton,QtCore.SIGNAL("clicked()"),self.slotEncodingWidget)
        
        self.deleteButton = QtGui.QPushButton(self.groupLocalFS)
        self.deleteButton.setGeometry(QtCore.QRect(270, 30, 92, 26))
        self.deleteButton.setObjectName("deleteButton")
        self.connect(self.deleteButton,QtCore.SIGNAL("clicked()"),self.slotDelete)
        
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 371, 73))
        self.page_2.setObjectName("page_2")
        self.groupDeviceFS = QtGui.QGroupBox(self.page_2)
        self.groupDeviceFS.setGeometry(QtCore.QRect(0, 0, 371, 71))
        self.groupDeviceFS.setObjectName("groupDeviceFS")

        self.createDevButton = QtGui.QPushButton(self.groupDeviceFS)
        self.createDevButton.setGeometry(QtCore.QRect(10, 30, 92, 26))
        self.createDevButton.setObjectName("createDevButton")
        self.connect(self.createDevButton,QtCore.SIGNAL("clicked()"),self.slotCreateDev)

        self.encodingDevButton = QtGui.QPushButton(self.groupDeviceFS)
        self.encodingDevButton.setGeometry(QtCore.QRect(140, 30, 92, 26))
        self.encodingDevButton.setObjectName("encodingDevButton")
        self.connect(self.encodingDevButton,QtCore.SIGNAL("clicked()"),self.slotEncodingDev)

        self.deleteDevButton = QtGui.QPushButton(self.groupDeviceFS)
        self.deleteDevButton.setGeometry(QtCore.QRect(270, 30, 92, 26))
        self.deleteDevButton.setObjectName("deleteDevButton")
        self.connect(self.deleteDevButton,QtCore.SIGNAL("clicked()"),self.slotDeleteDev)

        self.toolBox.addItem(self.page_2, "")
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 381, 131))
        self.groupBox_2.setObjectName("groupBox_2")

        self.mountButton = QtGui.QPushButton(self.groupBox_2)
        self.mountButton.setGeometry(QtCore.QRect(10, 30, 92, 26))
        self.mountButton.setObjectName("mountButton")
        self.connect(self.mountButton,QtCore.SIGNAL("clicked()"),self.slotMount)

        self.showButton = QtGui.QPushButton(self.groupBox_2)
        self.showButton.setGeometry(QtCore.QRect(140, 30, 92, 26))
        self.showButton.setObjectName("showButton")
        self.connect(self.showButton,QtCore.SIGNAL("clicked()"),self.slotShow)

        self.umountButton = QtGui.QPushButton(self.groupBox_2)
        self.umountButton.setGeometry(QtCore.QRect(270, 30, 92, 26))
        self.umountButton.setObjectName("umountButton")
        self.connect(self.umountButton,QtCore.SIGNAL("clicked()"),self.slotUmount)

        self.checkPopup = QtGui.QCheckBox(self.groupBox_2)
        self.checkPopup.setGeometry(QtCore.QRect(20, 70, 231, 23))
        self.checkPopup.setObjectName("checkPopup")
        self.connect(self.checkPopup,QtCore.SIGNAL("toggled(bool)"),self.slotPopupafter)

        self.checkHideaddress = QtGui.QCheckBox(self.groupBox_2)
        self.checkHideaddress.setGeometry(QtCore.QRect(20, 100, 241, 23))
        self.checkHideaddress.setObjectName("checkHideaddress")
        self.connect(self.checkHideaddress,QtCore.SIGNAL("toggled(bool)"),self.slotHideaddress)

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

        self.checkStartWith = QtGui.QCheckBox(self.page_3)
        self.checkStartWith.setGeometry(QtCore.QRect(20, 50, 121, 23))
        self.checkStartWith.setObjectName("checkStartWith")
        self.connect(self.checkStartWith,QtCore.SIGNAL("toggled(bool)"),self.slotStartwith)

        self.checkStartTrayed = QtGui.QCheckBox(self.page_3)
        self.checkStartTrayed.setGeometry(QtCore.QRect(150, 50, 91, 23))
        self.checkStartTrayed.setObjectName("checkStartTrayed")
        self.connect(self.checkStartTrayed,QtCore.SIGNAL("toggled(bool)"),self.slotandHide)

        self.hideToTrayButton = QtGui.QPushButton(self.page_3)
        self.hideToTrayButton.setGeometry(QtCore.QRect(260, 50, 92, 26))
        self.hideToTrayButton.setObjectName("hideToTrayButton")

        self.passwordline = QtGui.QLineEdit(self.page_3)
        self.passwordline.setGeometry(QtCore.QRect(160, 0, 191, 27))
        self.passwordline.setObjectName("passwordline")

        self.label_2 = QtGui.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 111, 17))
        self.label_2.setObjectName("label_2")

        self.checkShow = QtGui.QCheckBox(self.page_3)
        self.checkShow.setGeometry(QtCore.QRect(20, 20, 121, 23))
        self.checkShow.setObjectName("checkShow")
	self.connect(self.checkShow,QtCore.SIGNAL("toggled(bool)"),self.slotShowpassword)
        #self.notShowpassword()

        self.toolBox_2.addItem(self.page_3, "")
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 361, 93))
        self.page_4.setObjectName("page_4")

        self.textEdit1 = QtGui.QTextBrowser(self.page_4)
        self.textEdit1.setGeometry(QtCore.QRect(0, 0, 361, 91))
        self.textEdit1.setObjectName("textEdit1")
        self.toolBox_2.addItem(self.page_4, "")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #self.Showpassword()
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupLocalFS.setTitle(QtGui.QApplication.translate("Form", "Create && delete encrypted local filesystems", None, QtGui.QApplication.UnicodeUTF8))
        self.createButton.setText(QtGui.QApplication.translate("Form", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.encodingButton.setText(QtGui.QApplication.translate("Form", "Encoding", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("Form", "Local Filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.groupDeviceFS.setTitle(QtGui.QApplication.translate("Form", "(Later!) Create && delete encrypted device filesystems", None, QtGui.QApplication.UnicodeUTF8))
        self.createDevButton.setText(QtGui.QApplication.translate("Form", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.encodingDevButton.setText(QtGui.QApplication.translate("Form", "Encoding", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteDevButton.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Form", "Device Filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Mount and umount encrypted filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.mountButton.setText(QtGui.QApplication.translate("Form", "Mount", None, QtGui.QApplication.UnicodeUTF8))
        self.showButton.setText(QtGui.QApplication.translate("Form", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.umountButton.setText(QtGui.QApplication.translate("Form", "Unmount", None, QtGui.QApplication.UnicodeUTF8))
        self.checkPopup.setText(QtGui.QApplication.translate("Form", "Open encrypted folder after mounting", None, QtGui.QApplication.UnicodeUTF8))
        self.checkHideaddress.setText(QtGui.QApplication.translate("Form", "Open in konqueror (default: dolphin)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "qEncrypted Filesystem Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.checkStartWith.setText(QtGui.QApplication.translate("Form", "Start with system", None, QtGui.QApplication.UnicodeUTF8))
        self.checkStartTrayed.setText(QtGui.QApplication.translate("Form", "Start trayed", None, QtGui.QApplication.UnicodeUTF8))
        self.hideToTrayButton.setText(QtGui.QApplication.translate("Form", "Hide in panel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Enter password", None, QtGui.QApplication.UnicodeUTF8))
        self.checkShow.setText(QtGui.QApplication.translate("Form", "Show password", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), QtGui.QApplication.translate("Form", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), QtGui.QApplication.translate("Form", "Actions Log", None, QtGui.QApplication.UnicodeUTF8))

        ## end original qt code

        self.user_kencfs=os.path.expanduser("~/.kencfs2")
        print self.user_kencfs
        self.user_dot_encrypted=os.path.expanduser("~/.kencfs2/.encrypted")
        print self.user_dot_encrypted
        self.user_encrypted=os.path.expanduser("~/.kencfs2/encrypted")
        print self.user_encrypted

        self.user_startwith=os.path.expanduser("~/.kencfs2/start_with_kde.flag")

        print self.user_startwith


        self.encfsbinary="encfs"
        self.fusermountbinary="fusermount"

        mountedstate=self.setbuttons()
        #fix passwd hide input
    	self.slotShowpassword()
        if mountedstate:
            self.textEdit1.setText("Log: ENCRYPTED FILESYSTEM IS MOUNTED")
        else:
	    #print "---------------------------------------------"
            self.textEdit1.setText("Log: ENCRYPTED FILESYSTEM IS NOT MOUNTED")

        self.open_after_mount=os.path.expanduser("~/.kencfs2/open_after_mount.flag")


        if os.path.exists(self.open_after_mount):
            self.checkPopup.setChecked(1)
        else:
            self.checkPopup.setChecked(0)

# new in version 2
        self.hide_address=os.path.expanduser("~/.kencfs2/hide_address.flag")
        self.start_trayed=os.path.expanduser("~/.kencfs2/start_trayed.flag")


        if os.path.exists(self.hide_address):
            self.checkHideaddress.setChecked(1)
        else:
            self.checkHideaddress.setChecked(0)


        if os.path.exists(self.user_startwith):
            self.checkStartWith.setChecked(1)
        else:
            self.checkStartWith.setChecked(0)


        if os.path.exists(self.start_trayed):
            self.checkStartTrayed.setChecked(1)
#            self.parent.systray.setInactive()
        else:
            self.checkStartTrayed.setChecked(0)

# Variables (new in version 2)

# calling from encodingconnect:
#    def __init__(self, parent):
#        EncodingWidget.__init__(self, parent)
#        self.parent.parX="Value"

#inputfields=("x", "\n", - fix
#self.encodingIndex, "\n",
        self.encodingIndex="1"

#Please select a key size in bits.  The cipher you have chosen
#supports sizes from 128 to 256 bits in increments of 64 bits.
#"128", "\n",
        self.key_size="128"
#Select a block size in bytes.  The cipher you have chosen
#supports sizes from 64 to 4096 bytes in increments of 16.
#"512", "\n",
        self.block_size="512"
#The following filename encoding algorithms are available:
#1. Block : Block encoding, hides file name size somewhat
#2. Null : No encryption of filenames
#3. Stream : Stream encoding, keeps filenames as short as possible
#"1", "\n",
        self.filename_encoding="1"
#Enable filename initialization vector chaining?
#This makes filename encoding dependent on the complete path,
#rather then encoding each path element individually.
#This is normally desireable, therefor the default is Yes.
#Any response that does not begin with 'n' will mean Yes: Yes
#"Yes", "\n",
        self.vector_chaining="Yes"
#Enable per-file initialization vectors?
#This adds about 8 bytes per file to the storage requirements.
#It should not affect performance except possibly with applications
#which rely on block-aligned file io for performance.
#The default here is Yes.
#Any response that does not begin with 'n' will mean Yes: Yes
#"Yes", "\n",
        self.per_file_vectors="Yes"
#Enable filename to IV header chaining?
#This makes file data encoding dependent on the complete file path.
#If a file is renamed, it will not decode sucessfully unless it
#was renamed by encfs with the proper key.
#If this option is enabled, then hard links will not be supported
#in the filesystem.
#The default is No.
#Any response that does not begin with 'y' will mean No: No
#"No", "\n",
        self.iv_header_chaining="No"
#1.
#Enable block authentication code headers
#on every block in a file?  This adds about 12 bytes per block
#to the storage requirements for a file, and significantly affects
#performance but it also means [almost] any modifications or errors
#within a block will be caught and will cause a read error.
#The default here is No.
#Any response that does not begin with 'y' will mean No: No
#"No", "\n",

#2.
#Enable filename to IV header chaining?
#Any response that does not begin with 'y' will mean No: y

#Add random bytes to each block header?
#This adds a performance penalty, but ensures that blocks
#have different authentication codes.  Note that you can
#have the same benefits by enabling per-file initialization
#vectors, which does not come with as great of performance
#penalty.
#Select a number of bytes, from 0 (no random bytes) to 8: 8

        self.headers_every_block="No"
#        self.headers_every_block="8"
#str(self.passwordline.text()), "\n", - O.K.
#str(self.passwordline.text()), "\n") - O.K.



    def setVisible(self, visible):
	print "Debug: create Visible..."
        self.minimizeAction.setEnabled(visible)
        self.maximizeAction.setEnabled(not self.isMaximized())
        #self.restoreAction.setEnabled(self.isMaximized() or not visible)
        super(MainWindow, self).setVisible(visible)

    def closeEvent(self, event):
	print "Debug: Close Event..."
        if self.trayIcon.isVisible():
            QtGui.QMessageBox.information(self, self.tr("Systray"),
                    self.tr("The program will keep running in the system "
                            "tray. To terminate the program, choose "
                            "<b>Quit</b> in the context menu of the system "
                            "tray entry."))
            self.hide()
            event.ignore()

#-----------------------------------------------------------------------------------------
# Button associated slots and exit processes
#-----------------------------------------------------------------------------------------

    def slotMount(self):

        #cmdlineout=(self.encfsbinary +' --extpass="kdialog --password qEncryptedFilesystemManager" ' + self.user_dot_encrypted +" "+ self.user_encrypted)
        dest_dirs = self.user_dot_encrypted +"  "+ self.user_encrypted
        #cmdlineout=(self.encfsbinary, self.user_dot_encrypted, self.user_encrypted, "-S")
        inputfields=(str(self.passwordline.text()), "\n")
        print "\nMount directories....\n"
        
        # temporally disabled problem with setWorkingDirectory()
        #self.currentprocess = MyProcess(self.textEdit1, self.user_kencfs, cmdlineout, inputfields, "normal")
        #self.currentprocess.thread.process.connect(self.currentprocess.thread.process, QtCore.SIGNAL("processExited()"), self.mountExited)

        #mission = os.popen2(command + dest_dirs)
        command = self.encfsbinary +' --extpass="kdialog --password qEncrypted_Filesystem_Manager" ' + dest_dirs
        print command + "\n"
        stdin, stdouterr = os.popen4(command)
        output = stdouterr.read()
        print output
        
	sleep(0.2)
        self.mountExited()


    def mountExited(self):
        mountedstate=self.setbuttons()
        ##? self.notShowpassword()
# Stupid code for suse bug
        incorrectpassword=0
        ##? messageeditortext=str(self.textEdit1.text())
        ##? if not messageeditortext=="":
        ##?     incorrectpwdmessage="password incorrect"
        ##?     incorrectpassword=messageeditortext.count(incorrectpwdmessage)

        if mountedstate:
            self.textEdit1.setText("Log: ENCRYPTED FILESYSTEM HAS BEEN MOUNTED.")
            desktop = os.popen("cat $HOME/.config/user-dirs.dirs | grep DESKTOP | sed -e 's|XDG_DESKTOP_DIR=||' -e 's|\"||g' -e 's|$|\/Crypted|'" , "r").readline()
            print "\nCheck:" +desktop

            #os.system("ln -sf " + self.user_encrypted + " " + desktop)
            #print "\nLinking...."
            
# popuphandler:
            if self.checkPopup.isChecked():
#                sleep(0.2)
                self.slotShow()
        elif not incorrectpassword==0:
            QtGui.QMessageBox.warning(self, "Incorrect password!", "Please enter the correct password\ninto the password field!\n")
        else:
            QtGui.QMessageBox.warning(self, "Mounting error!", "Cannot mount encrypted file system.\nPlease close all applications incuding\nkonqueror using the encrypted folder!\nMaybe the password is not correct or\nthe kernel module fuse cannot be inserted.\n")



    def slotUmount(self):
# Format: $FUSERMOUNT -u $TARGET;
        #cmdlineout=(self.fusermountbinary, "-u", self.user_encrypted)

        #self.currentprocess = MyProcess(self.textEdit1, self.user_kencfs, cmdlineout, "", "fast")
        #self.currentprocess.thread.process.connect(self.currentprocess.thread.process, QtCore.SIGNAL("processExited()"), self.umountExited)

        # temporally disabled problem with setWorkingDirectory()
        command = self.fusermountbinary + " -u " + self.user_encrypted
        print command + "\n"
        stdin, stdouterr = os.popen4(command)
        output = stdouterr.read()
        print output
        
	self.umountExited()

    def umountExited(self):
        mountedstate=self.setbuttons()
        if not mountedstate:
            self.textEdit1.setText("Log: ENCRYPTED FILESYSTEM HAS BEEN UNMOUNTED.")
        else:
            QtGui.QMessageBox.warning(self, "Unmounting error!", "Cannot unmount encrypted file system.\nPlease close all applications incuding\nkonqueror using the encrypted folder!\n")


    def slotCreate(self):
        if os.path.exists(self.user_dot_encrypted):
            try:
                shutil.rmtree(self.user_dot_encrypted)
                
                print "\n createCreate...\n"

                self.executeCreate()

                self.createButton.setEnabled(1)
                self.encodingButton.setEnabled(1)
                self.deleteButton.setEnabled(0)
                self.mountButton.setEnabled(0)
                self.showButton.setEnabled(0)
                self.umountButton.setEnabled(0)

            except:
                QtGui.QMessageBox.warning(self, "Error!", "Cannot delete encrypted file system.\nPlease close all applications incuding\nkonqueror using the encrypted folder and unmount it before!\n")
        else:
            self.executeCreate()


    def executeCreate(self):

        if str(self.passwordline.text())=="":
            self.textEdit1.setText("Log: PLEASE CHOOSE A PASSWORD ENTER IT INTO THE PASSWORD FIELD UNDER OPTIONS!")
            QtGui.QMessageBox.warning(self, "Error!", "PLEASE CHOOSE A PASSWORD ENTER IT INTO THE PASSWORD FIELD UNDER OPTIONS!")

        else:
    	    os.makedirs(self.user_dot_encrypted)
    	    os.makedirs(self.user_encrypted)
        	#os.mkdir(self.user_encrypted)
        	#commands.getoutput('mkdir -p', self.user_dot_encrypted)
    	    
    	    cmdlineout=(self.encfsbinary, self.user_dot_encrypted, self.user_encrypted, "-S")

            print "encoding index: "
            print self.encodingIndex

            if self.encodingIndex=="3":
#                if self.cbIvheaderchaining.isChecked():
                if self.iv_header_chaining=="yes":
                    inputfields=("x", "\n", self.encodingIndex, "\n", self.filename_encoding, "\n", self.vector_chaining, "\n", self.per_file_vectors, "\n", self.iv_header_chaining, "\n", self.headers_every_block, "\n", str(self.passwordline.text()), "\n", str(self.passwordline.text()), "\n")
                else:
#                if self.cbVectorchaining.isChecked() and self.cbPerfilevectors.isChecked():
                    if self.vector_chaining=="Yes" and self.per_file_vectors=="Yes":
                        inputfields=("x", "\n", self.encodingIndex, "\n", self.filename_encoding, "\n", self.vector_chaining, "\n", self.per_file_vectors, "\n", self.iv_header_chaining, "\n", self.headers_every_block, "\n", str(self.passwordline.text()), "\n", str(self.passwordline.text()), "\n")
                    else:
                        inputfields=("x", "\n", self.encodingIndex, "\n", self.filename_encoding, "\n", self.vector_chaining, "\n", self.per_file_vectors, "\n", self.iv_header_chaining, "\n", str(self.passwordline.text()), "\n", str(self.passwordline.text()), "\n")

            else:
                if self.iv_header_chaining=="yes":
                    inputfields=("x", "\n", self.encodingIndex, "\n", self.key_size, "\n", self.block_size, "\n", self.filename_encoding, "\n", self.vector_chaining, "\n", self.per_file_vectors, "\n", self.iv_header_chaining, "\n", self.headers_every_block, "\n", str(self.passwordline.text()), "\n", str(self.passwordline.text()), "\n")
                else:
                    if self.vector_chaining=="Yes" and self.per_file_vectors=="Yes":
                        inputfields=("x", "\n", self.encodingIndex, "\n", self.key_size, "\n", self.block_size, "\n", self.filename_encoding, "\n", self.vector_chaining, "\n", self.per_file_vectors, "\n", self.iv_header_chaining, "\n", self.headers_every_block, "\n", str(self.passwordline.text()), "\n", str(self.passwordline.text()), "\n")
                    else:
                        inputfields=("x", "\n", self.encodingIndex, "\n", self.key_size, "\n", self.block_size, "\n", self.filename_encoding, "\n", self.vector_chaining, "\n", self.per_file_vectors, "\n", self.iv_header_chaining, "\n", str(self.passwordline.text()), "\n", str(self.passwordline.text()), "\n")

                print "index is not 3"
            print "Input fields:"
            print inputfields

            #self.currentprocess = MyProcess(self.textEdit1, self.user_kencfs, cmdlineout, inputfields, "normal")
            #self.currentprocess.thread.process.connect(self.currentprocess.thread.process, QtCore.SIGNAL("processExited()"), self.createExited)
    	    command = self.encfsbinary +" "+ self.user_dot_encrypted +" "+ self.user_encrypted
    	    print command + "\n"
    	    stdin, stdouterr = os.popen4(command)
    	    output = stdouterr.read()
    	    print output
        
	    sleep(0.2)


    def createExited(self):
        mountedstate=self.setbuttons()
        self.notShowpassword()

        if mountedstate:

            if self.checkPopup.isChecked():
                self.slotShow()

            else:
                sleep(0.1)
            self.textEdit1.append("\nLog: ENCRYPTED FILESYSTEM HAS BEEN CREATED AND MOUNTED.")

        else:
            QtGui.QMessageBox.warning(self, "Mounting error!", "Cannot create/mount encrypted file system.\nPlease close all applications incuding\nkonqueror using the encrypted folder!\nMaybe the kernel module fuse cannot be inserted.\n")


    def slotDelete(self):
	print "Activate Delete Button.....\n"

        r = QtGui.QMessageBox.question(self, "Delete encrypted file system",
            "All of the encrypted content will be lost if\nyou proceed! Do you really want to delete\nwhole content of the encrypted folder?\n",
            "&Delete", "&Abort")
        if r == 1:

            return
        if r == 0:
            os.chdir(self.user_kencfs)
            try:
                shutil.rmtree(self.user_dot_encrypted)
                shutil.rmtree(self.user_encrypted)
                self.createButton.setEnabled(1)
                self.encodingButton.setEnabled(1)
                self.deleteButton.setEnabled(0)
                self.mountButton.setEnabled(0)
                self.showButton.setEnabled(0)
                self.umountButton.setEnabled(0)

            except:
                QtGui.QMessageBox.warning(self, "Error!", "Cannot delete encrypted file system.\nPlease close all applications incuding konqueror using the encrypted folder and unmount it before!\n")


    def slotShow(self):
        if self.checkHideaddress.isChecked():
            os.system("konqueror --profile /usr/lib/qefm/encryptedprofil " + self.user_encrypted +" &")
        else:
            os.system("dolphin " + self.user_encrypted +" &")


# A parent call:
    def slotHidetoTray(self):
        self.parent.systray.setInactive()


#-----------------------------------------------------------------------------------------
# Checkbox associated slots
#-----------------------------------------------------------------------------------------

    def slotShowpassword(self):
        if self.checkShow.isChecked():
            self.passwordline.setEchoMode(QtGui.QLineEdit.Normal)
        else:
            self.passwordline.setEchoMode(QtGui.QLineEdit.Password)


    def slotPopupafter(self):
        os.chdir(self.user_kencfs)

        if not self.checkPopup.isChecked():
            try:
                os.remove("open_after_mount.flag")
            except:
                pass
        else:
            flag_file=open("open_after_mount.flag", "w")

            flag_file.close()
        sleep(0.2)

    def slotHideaddress(self):
        os.chdir(self.user_kencfs)

        if not self.checkHideaddress.isChecked():
            try:
                os.remove("hide_address.flag")
            except:
                pass
        else:
            flag_file=open("hide_address.flag", "w")

            flag_file.close()
        sleep(0.2)

    def slotandHide(self):
        os.chdir(self.user_kencfs)

        if not self.checkStartTrayed.isChecked():
            try:
                os.remove("start_trayed.flag")
            except:
                pass
        else:
            flag_file=open("start_trayed.flag", "w")

            flag_file.close()
        sleep(0.2)


    def slotStartwith(self):
        os.chdir(self.user_kencfs)

        if self.checkStartWith.isChecked():
            flag_file=open("start_with_kde.flag", "w")
            flag_file.close()

            output = os.popen("ls $HOME/.kde4/Autostart/* | grep qencfsm", "r").readline()
            print "\nCheck:" +output
            if output=="":
                QtGui.QMessageBox.warning(self, "Q-EncFSm: Warning!", "The file 'startkde' has not been patched yet!\n\nPlease edit this script file manually according to\nthe instructions can be found in the following file:\n/usr/share/qencfsm/startkde/readme.startkde!\n")
            else:
        	print " OK\n"

        else:
            try:
                os.remove("start_with_kde.flag")

            except:
                pass

        sleep(0.2)


#-----------------------------------------------------------------------------------------
# General functions
#-----------------------------------------------------------------------------------------

    def setbuttons(self):

        sleep(0.2)

        os.chdir("/etc")
        mtabfile=open("mtab", "r")
        mtab_raws=mtabfile.readlines()
        mtabfile.close()

        mounted=False

        encfsstr="encfs"

        for mountline in mtab_raws:

            trimmountline=mountline[0:-1]
            if not trimmountline.count(encfsstr)==0:

                print "mtab line starts with encfs:"
                print trimmountline

                if not trimmountline.count(self.user_encrypted)==0:

                    print "and contains the user home encrypted fs"

                    mounted=True
                    break


        if not os.path.exists(self.user_dot_encrypted):
            self.createButton.setEnabled(1)
            self.encodingButton.setEnabled(1)
            self.deleteButton.setEnabled(0)
            self.createDevButton.setEnabled(0)
            self.encodingDevButton.setEnabled(0)
            self.deleteDevButton.setEnabled(0)
            self.mountButton.setEnabled(0)
            self.showButton.setEnabled(0)
            self.umountButton.setEnabled(0)
        else:
            if mounted:
                self.createButton.setEnabled(0)
                self.encodingButton.setEnabled(0)
                self.deleteButton.setEnabled(0)
                self.mountButton.setEnabled(0)
                self.showButton.setEnabled(1)
                self.umountButton.setEnabled(1)
        	self.createDevButton.setEnabled(0)
        	self.encodingDevButton.setEnabled(0)
        	self.deleteDevButton.setEnabled(0)
            else:
                self.createButton.setEnabled(0)
                self.encodingButton.setEnabled(0)
                self.deleteButton.setEnabled(1)
                self.mountButton.setEnabled(1)
                self.showButton.setEnabled(0)
                self.umountButton.setEnabled(0)
        	self.createDevButton.setEnabled(0)
        	self.encodingDevButton.setEnabled(0)
        	self.deleteDevButton.setEnabled(0)

        return mounted


    def notShowpassword(self):
	self.notShowpassword()
        self.passwordline.clear()
        if self.checkShow.isChecked():
            self.checkShow.setChecked(0)
            self.passwordline.setEchoMode(QLineEdit.Password)


#-----------------------------------------------------------------------------------------
# encoding widget slot
#-----------------------------------------------------------------------------------------

    def slotEncodingWidget(self):

        encodingform = encodingconnect.encodingConnect(self)
        encodingform.show()
        print "Old encoding parameters:"
        print self.encodingIndex
        print self.key_size
        print self.block_size
        print self.filename_encoding
        print self.vector_chaining
        print self.per_file_vectors
        print self.iv_header_chaining
        print self.headers_every_block

#-----------------------------------------------------------------------------------------
# New features for device encrypt
#-----------------------------------------------------------------------------------------


    def slotCreateDev(self):
        print "UI slotCreateDev(): Not implemented yet \n>"

    def slotDeleteDev(self):
        print "UI slotDeleteDev(): Not implemented yet\n>"

    def slotEncodingDev(self):
        print "UI slotEncodingDev(): Not implemented yet\n>"

#-----------------------------------------------------------------------------------------
# Toolbar contex menu associated slots
#-----------------------------------------------------------------------------------------

    def slotHelp(self):
        help = helpconnect.HelpConnect(self)
        help.show()


    def slotAboutQEncfsm(self):
        aboutqencfsm = aboutform.AboutForm(self)
        aboutqencfsm.show()
        #about = aboutform.NAboutForm(self)
        #about.show()
        #QtGui.QMessageBox.aboutQt(self, "qEncrypted Filesystem Manager")
        #QtGui.QMessageBox.information(None, self.tr("qEncrypted Filesystem Manager"),
        #        self.tr("About:\n\n"
        #    		"qEncrypted Filesystem Manager\n\n"
        #                "Developer: Chareles Barcza \n"
        #                "Contact  : kbarcza@blackpanther.hu\n"
        #                "Webpage  : www.blackPanther.hu" ))

    def slotAboutQT(self):
        QtGui.QMessageBox.aboutQt(self, "About Qt4")

#-----------------------------------------------------------------------------------------
# tray icon
#-----------------------------------------------------------------------------------------


    def setIcon(self, index):
    	print "Debug: create setIcon..."
        icon = self.iconComboBox.itemIcon(index)
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)

        self.trayIcon.setToolTip(self.iconComboBox.itemText(index))

    def iconActivated(self, reason):
        if reason in (QtGui.QSystemTrayIcon.Trigger, QtGui.QSystemTrayIcon.DoubleClick):
            self.iconComboBox.setCurrentIndex(
                    (self.iconComboBox.currentIndex() + 1)
                    % self.iconComboBox.count())
        elif reason == QtGui.QSystemTrayIcon.MiddleClick:
            self.showMessage()

    def showMessage(self):
        icon = QtGui.QSystemTrayIcon.MessageIcon(
             self.typeComboBox.itemData(
                 self.typeComboBox.currentIndex()).toInt()[0])
        self.trayIcon.showMessage(self.titleEdit.text(),
                self.bodyEdit.toPlainText(), icon,
                self.durationSpinBox.value() * 1000)

    def messageClicked(self):
        QtGui.QMessageBox.information(None, self.tr("Systray"),
                self.tr("Sorry, I already gave what help I could.\nMaybe you "
                        "should try asking a human?"))


    def createMessageGroupBox(self):
        self.messageGroupBox = QtGui.QGroupBox(self.tr("Balloon Message"))

        typeLabel = QtGui.QLabel(self.tr("Type:"))

        self.typeComboBox = QtGui.QComboBox()
        self.typeComboBox.addItem(self.tr("None"),
                QtCore.QVariant(QtGui.QSystemTrayIcon.NoIcon))
        self.typeComboBox.addItem(self.style().standardIcon(
                QtGui.QStyle.SP_MessageBoxInformation), self.tr("Information"),
                QtCore.QVariant(QtGui.QSystemTrayIcon.Information))
        self.typeComboBox.addItem(self.style().standardIcon(
                QtGui.QStyle.SP_MessageBoxWarning), self.tr("Warning"),
                QtCore.QVariant(QtGui.QSystemTrayIcon.Warning))
        self.typeComboBox.addItem(self.style().standardIcon(
                QtGui.QStyle.SP_MessageBoxCritical), self.tr("Critical"),
                QtCore.QVariant(QtGui.QSystemTrayIcon.Critical))
        self.typeComboBox.setCurrentIndex(1)

        self.durationLabel = QtGui.QLabel(self.tr("Duration:"))

        self.durationSpinBox = QtGui.QSpinBox()
        self.durationSpinBox.setRange(5, 60)
        self.durationSpinBox.setSuffix(" s")
        self.durationSpinBox.setValue(15)

        durationWarningLabel = QtGui.QLabel(self.tr("(some systems might "
                "ignore this hint)"))
        durationWarningLabel.setIndent(10)

        titleLabel = QtGui.QLabel(self.tr("Title:"))

        self.titleEdit = QtGui.QLineEdit(self.tr("Cannot connect to network"))

        bodyLabel = QtGui.QLabel(self.tr("Body:"))

        self.bodyEdit = QtGui.QTextEdit()
        self.bodyEdit.setPlainText(self.tr("Don't believe me. Honestly, I "
                "don't have a clue.\nClick this balloon for details."))

        self.showMessageButton = QtGui.QPushButton(self.tr("Show Message"))
        self.showMessageButton.setDefault(True)

        messageLayout = QtGui.QGridLayout()
        messageLayout.addWidget(typeLabel, 0, 0)
        messageLayout.addWidget(self.typeComboBox, 0, 1, 1, 2)
        messageLayout.addWidget(self.durationLabel, 1, 0)
        messageLayout.addWidget(self.durationSpinBox, 1, 1)
        messageLayout.addWidget(durationWarningLabel, 1, 2, 1, 3)
        messageLayout.addWidget(titleLabel, 2, 0)
        messageLayout.addWidget(self.titleEdit, 2, 1, 1, 4)
        messageLayout.addWidget(bodyLabel, 3, 0)
        messageLayout.addWidget(self.bodyEdit, 3, 1, 2, 4)
        messageLayout.addWidget(self.showMessageButton, 5, 4)
        messageLayout.setColumnStretch(3, 1)
        messageLayout.setRowStretch(4, 1)
        self.messageGroupBox.setLayout(messageLayout)

    def createActions(self):
	print "Debug: createAction...."
        self.minimizeAction = QtGui.QAction(self.tr("Mi&nimize"), self)
        #self.connect(self.minimizeAction,QtCore.SIGNAL("triggered()"),self.closeEvent(0))
        self.connect(self.minimizeAction,QtCore.SIGNAL("triggered()"),self.clickEvent)
        #self.minimizeAction.triggered.connect(self.hide)

        self.maximizeAction = QtGui.QAction(self.tr("Ma&ximize"), self)
        self.connect(self.maximizeAction,QtCore.SIGNAL("triggered()"),self.showMaximized)
        #self.maximizeAction.triggered.connect(self.showMaximized)

        self.aboutQEncfsm = QtGui.QAction(self.tr("&About qEncfsm"), self)
        self.connect(self.aboutQEncfsm,QtCore.SIGNAL("triggered()"),self.slotAboutQEncfsm)

        self.aboutAction = QtGui.QAction(self.tr("&About Qt4"), self)
        self.connect(self.aboutAction,QtCore.SIGNAL("triggered()"),self.slotAboutQT)
        #self.restoreAction.triggered.connect(self.showNormal)

        self.quitAction = QtGui.QAction(self.tr("&Quit"), self)
        self.connect(self.quitAction,QtCore.SIGNAL("triggered()"),QtGui.qApp.quit)
        #self.quitAction.triggered.connect(QtGui.qApp.quit)

    def createTrayIcon(self):
	print "Debug: createTrayIcon...."
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addAction(self.aboutQEncfsm)
        self.trayIconMenu.addAction(self.aboutAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
	self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon("file_locked.png"), app)
        #self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

    def clickEvent(self):
	print "Debug: createEvent..."
        self.hide()
    	self.trayIcon.show() #thanks @mojo
    	#event.ignore()
    	#if self.okayToClose(): 
    	#user asked for exit
    	#    self.trayIcon.hide()
    	#    event.accept()
    	#else:
    	#"minimize"
    	#    self.hide()
    	#    self.trayIcon.show() #thanks @mojo
    	#    event.ignore()
    
    def __icon_activated(self, reason):
    	if reason == QtGui.QSystemTrayIcon.DoubleClick:
    	    self.show()
#-----------------------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    if not QtGui.QSystemTrayIcon.isSystemTrayAvailable():
        QtGui.QMessageBox.critical(None, QtCore.QObject.tr(app, "Systray"),
                QtCore.QObject.tr(app, "I couldn't detect any system tray on "
                    "this system."))
        sys.exit(1)
    # define close button to hide function 
    #QtGui.QApplication.setQuitOnLastWindowClosed(False)
    # end define close button to hide function 
    Form = QtGui.QWidget()
    ui = MainWindow()
    #ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

