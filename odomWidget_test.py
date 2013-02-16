#!/usr/bin/env python
import odomWidgetImport
import sys
from PyQt4 import QtGui, QtCore

class robotWidget(QtGui.QWidget):
    
    def __init__(self):
        super(robotWidget, self).__init__()
        
        self.initUI()
        
    
        
    def initUI(self):


        hbox = QtGui.QHBoxLayout(self)

        ######################################
        ##### Setting up the top left box ####
        ##### (the box with the sliders)  ####
        ######################################
        
        vbox = QtGui.QGridLayout()
        vbox.setSpacing(0)
        vbox.setColumnMinimumWidth(0, 50)
        vbox.setColumnMinimumWidth(1, 400)
        
        lcd1 = QtGui.QLCDNumber(self)
        sld1 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        lbl1 = QtGui.QLabel('Red', self)
        lbl1.setText("<font style='color: red;'>Red</font>")
        sld1.setMaximum(255)
        vbox.addWidget(lcd1, 1, 2)
        vbox.addWidget(sld1, 1, 1)
        vbox.addWidget(lbl1, 1, 0)

        sld1.valueChanged.connect(lcd1.display)
        def setValue1(rvalue):
            global r
            r = rvalue
        self.connect(sld1, QtCore.SIGNAL('valueChanged(int)'), setValue1)



        lcd2 = QtGui.QLCDNumber(self)
        sld2 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        lbl2 = QtGui.QLabel('Green', self)
        lbl2.setText("<font style='color: green;'>Green</font>")
        sld2.setMaximum(255)
        vbox.addWidget(lcd2, 2, 2)
        vbox.addWidget(sld2, 2, 1)
        vbox.addWidget(lbl2, 2, 0)
        sld2.valueChanged.connect(lcd2.display)
        def setValue2(gvalue):
            global g
            g = gvalue
        self.connect(sld2, QtCore.SIGNAL('valueChanged(int)'), setValue2)



        lcd3 = QtGui.QLCDNumber(self)
        sld3 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        lbl3 = QtGui.QLabel("Blue", self)
        lbl3.setText("<font style='color: blue;'>Blue</font>")
        sld3.setMaximum(255)
        vbox.addWidget(lcd3, 3, 2)
        vbox.addWidget(sld3, 3, 1)
        vbox.addWidget(lbl3, 3, 0)
        sld3.valueChanged.connect(lcd3.display)
        def setValue3(bvalue):
            global b
            b = bvalue
        self.connect(sld3, QtCore.SIGNAL('valueChanged(int)'), setValue3)

        
        topleft = QtGui.QFrame(self)
        topleft.setLayout(vbox)

        ######################################
        #### Setting up the top right box ####
        #### (Displays iRobot Odometry)   ####
        ######################################

        odomGrid = QtGui.QGridLayout()
        odomGrid.setSpacing(30)

        lbl4 = QtGui.QLabel("Theta", self)
        lcd4 = QtGui.QLCDNumber(self)
        odomGrid.addWidget(lbl4, 1, 0)
        odomGrid.addWidget(lcd4, 1, 1)
        global theta
        theta = int(4)
        lcd4.display(theta)

        lbl5 = QtGui.QLabel("X Coordinate", self)
        lcd5 = QtGui.QLCDNumber(self)
        odomGrid.addWidget(lbl5, 2, 0)
        odomGrid.addWidget(lcd5, 2, 1)
        global X
        X = int(4)
        lcd5.display(X)

        lbl6 = QtGui.QLabel("Y Coordinate", self)
        lcd6 = QtGui.QLCDNumber(self)
        odomGrid.addWidget(lbl6, 3, 0)
        odomGrid.addWidget(lcd6, 3, 1)
        global Y
        Y = int(4)
        lcd6.display(Y)

        lbl7 = QtGui.QLabel("Current State:", self)
        global state
        state = "Keyboard"
        lbl8 = QtGui.QLabel(state, self)
        odomGrid.addWidget(lbl7, 4, 0)
        odomGrid.addWidget(lbl8, 4, 1)
        
        
        topright = QtGui.QFrame(self)
        topright.setLayout(odomGrid)


        ######################################
        #### Setting up the bottom box    ####
        #### (COOL STUFF??)               ####
        ######################################
        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
        self.setGeometry(300, 300, 1000, 480)
        self.setWindowTitle('Robot Control Panel')
        self.show()
        
    def onChanged(self, text):
        
        self.lbl.setText(text)
        self.lbl.adjustSize()        

        
if __name__ == '__main__':
    """
    this simply runs listener
    """
    global odometry
    listener() # initializes code to listen for the dock
    ros_services()
    odometry = odomClass.Odometry()
    odometryDraw()
    app = QtGui.QApplication(sys.argv)
    widget = robotWidget()
    sys.exit(app.exec_())
    print "Bye!"
    rospy.spin() #this stops the code from completing.  It will allow other 
        #processes, like listening, to happen, and the code won't end.
   
