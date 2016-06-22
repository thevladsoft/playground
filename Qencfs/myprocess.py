##/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) Big-Cat Software Association, 2006.
#
# GILDE project. 
# (Graphical Interfaces to Learn Debian Easily)
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version. Please read the COPYING file.
#


import sys, re, os
import tempfile
from PyQt4 import QtCore, QtGui, QtXml
from time import sleep

from colors import Colors

class MyProcess:
    def __init__(self, editor, workdir, params, inputs, mode):
        #print "create MyQProcess........\n"
        #self.myprocess=MyQProcess(workdir, params)
        Colors.debug("WorkDir:", workdir)
        print "\ncreate MyThread......... \n"
        self.mode=mode
        self.thread=MyThread(workdir, params, editor, inputs, mode)
        print "\ncreate MyThread end ....\n"

    def cancelProcess(self):
        print "start cancelProcess"
        if self.thread.process.isRunning():
            self.thread.process.tryTerminate()
        while self.thread.process.isRunning():
            sleep(0.01)
        print "Process terminated"
        print "Process mode = "+self.mode
        sleep(0.5)
##        if self.thread.running():
##            self.thread.terminate()
##        while self.thread.running():
##            sleep(0.1)
        print "closing thread"
        print "Thread closed"
#  user option force to terminate, future feature
#        if self.thread.running():
#            self.thread.terminate()
#            print "Thread closed"

class MyQProcess(QtCore.QProcess):
    def __init__(self, workdir, params):
        QtCore.QProcess.__init__(self)
        Colors.debug("WorkDir:", workdir)
        #print "1:"+
        #self.startDetached(QtCore.QDir(workdir))
        self.setWorkingDirectory(QtCore.QDir(workdir))
        #.absolutePath()
	for param in params:
    	    self.addArgument(param)

        #workingDirectory = self.resolveDataDir(name)
        #process.setWorkingDirectory(workingDirectory)
        #Colors.debug("Setting working directory:", workingDirectory)

        #process.start(sys.executable, [executable])

class MyThread(QtCore.QThread):
    def __init__(self, workdir, params, editor, inputs, mode):
        QtCore.QThread.__init__(self)
#        self.process=process
        print "create MyQProcess......\n"
        #print "WorkDir:"+workdir, params, editor, inputs, mode +"\n\n" 
        self.process=MyQProcess(workdir, params)
        self.editor=editor
        self.inputs=inputs
##        editor.clear()
        self.mode=mode
        if (self.mode=="normal"):
            self.editor.setMaxLogLines(500)
        if (self.mode=="fast"):
            self.editor.setMaxLogLines(500)

        self.start(MyThread.NormalPriority)

    def run(self):
        if (self.mode=="normal"):
            self.MyProcessAPI_Color_Normal()
        if (self.mode=="fast"):
            self.MyProcessAPI_Color_Fast()
        if (self.mode=="line"):
            self.MyProcessAPI_Color_Line()

#-----------------------------------------------------------------------------------------
# Normal
#-----------------------------------------------------------------------------------------
    def MyProcessAPI_Color_Normal(self):
        self.process.connect(self.process, SIGNAL("readyReadStdout()"), self.printlnOutSlot_Normal)
        self.process.connect(self.process, SIGNAL("readyReadStderr()"), self.printlnErrSlot_Normal)
        processstarted=self.process.start()
        self.msleep(10)
        if not processstarted:
            self.editor.append("Can't start process")
            self.process.tryTerminate()
        else:
#            self.process.closeStdin()
            for inputstr in self.inputs:
                self.process.writeToStdin(inputstr)
            while self.process.isRunning():
                self.msleep(10)

            self.msleep(200)
            print "Flushing std and err out..."
            self.printlnOutSlot_Normal()
            self.printlnErrSlot_Normal()
            print "Process finished: Normal."

    # Normal
    def printlnOutSlot_Normal(self):
        while self.process.canReadLineStdout():
            printline='<font color="#000000">'+unicode(self.process.readLineStdout(), "utf-8")
            # debug line stdout
            print printline
            self.editor.append(printline)
 #           self.msleep(1)
    # Normal
    def printlnErrSlot_Normal(self):
        while self.process.canReadLineStderr():
            printline='<font color="#FF0000">'+unicode(self.process.readLineStderr(), "utf-8")
            # debug line errout
            print printline
            if not printline[22:50]=="Unable to get Terminal Size.":
                self.editor.append(printline)
 #           self.msleep(1)

#-----------------------------------------------------------------------------------------
# Fast
#-----------------------------------------------------------------------------------------
    def MyProcessAPI_Color_Fast(self):
        processstarted=self.process.start()
        self.msleep(10)
        if not processstarted:
            self.editor.append("Can't start process")
            self.process.tryTerminate()
        else:
            self.process.closeStdin()
            while self.process.isRunning():
                self.msleep(100)
                self.editor.setText("Log: UNMOUNTING ENCRYPTED FILE SYSTEM...")
                self.editor.append(self.process.readLineStdout())
            self.printlnOutSlot_Fast()
            self.printlnErrSlot_Fast()
#            self.msleep(200)
            print "Process finished: Fast."
    # Fast
    def printlnOutSlot_Fast(self):
        while self.process.canReadLineStdout():
            printline='<font color="#000000">'+unicode(self.process.readLineStdout(), "utf-8")
            # debug line stdout
            # print self.printline
        try:
            self.editor.setText("Log: UNMOUNTING ENCRYPTED FILE SYSTEM...")
            self.editor.append(printline)
        except:
            pass
    # Fast
    def printlnErrSlot_Fast(self):
        while self.process.canReadLineStderr():
            printline='<font color="#FF0000">'+unicode(self.process.readLineStderr(), "utf-8")
            # debug line errout
            # print self.printline
            self.editor.append(printline)

#-----------------------------------------------------------------------------------------
# Line
#-----------------------------------------------------------------------------------------
    def MyProcessAPI_Color_Line(self):
        processstarted=self.process.start()
        self.msleep(10)
        if not processstarted:
            self.process.tryTerminate()
        else:
            self.process.closeStdin()
#            while self.process.isRunning():
#                self.msleep(100)
            print "Process finished: Line."
