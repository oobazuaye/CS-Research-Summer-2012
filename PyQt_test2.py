import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    
        
    def initUI(self):

        vbox = QtGui.QGridLayout()
        vbox.setSpacing(10)

        
        lcd1 = QtGui.QLCDNumber(self)
        sld1 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        vbox.addWidget(lcd1, 1, 0)
        vbox.addWidget(sld1, 1, 1)
        
        sld1.valueChanged.connect(lcd1.display)
        def setValue1(rvalue):
            global r
            r = rvalue
        self.connect(sld1, QtCore.SIGNAL('valueChanged(int)'), setValue1)



        lcd2 = QtGui.QLCDNumber(self)
        sld2 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        vbox.addWidget(lcd2, 2, 0)
        vbox.addWidget(sld2, 2, 1)
        sld2.valueChanged.connect(lcd2.display)
        def setValue2(gvalue):
            global g
            g = gvalue
        self.connect(sld2, QtCore.SIGNAL('valueChanged(int)'), setValue2)



        lcd3 = QtGui.QLCDNumber(self)
        sld3 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        vbox.addWidget(lcd3, 3, 0)
        vbox.addWidget(sld3, 3, 1)
        sld3.valueChanged.connect(lcd3.display)
        def setValue3(bvalue):
            global b
            b = bvalue
        self.connect(sld3, QtCore.SIGNAL('valueChanged(int)'), setValue3)

        lcd4 = QtGui.QLCDNumber(self)
        vbox.addWidget(lcd4, 4, 0)
        global theta
        theta = 4
        lcd4.display(theta)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 480, 640)
        self.setWindowTitle('Big Widget!')
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
