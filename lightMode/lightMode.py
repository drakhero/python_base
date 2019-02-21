import sys,random,math
from PyQt4 import QtGui,QtCore

import numpy as ny

class lightMode(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('光照模型')
        self.resize(1200,600)
        self.center()
        self.initUI()
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)
    def initUI(self):
        checkBox1 = QtGui.QCheckBox('红色光源', self)
        checkBox1.setGeometry(50, 50, 300, 20)

        checkBox2 = QtGui.QCheckBox('绿色光源', self)
        checkBox2.setGeometry(50, 100, 300, 20)

        checkBox3 = QtGui.QCheckBox('蓝色光源', self)
        checkBox3.setGeometry(50, 150, 300, 20)



    def draw(self,qp):
        a = 900
        b = 500
        c = 20
        r = 200
        f = 0   #循环变量
        t = 0
        d = 3000 #视距

        f = 0
        t = 0
        add = 0.11
        qp.setPen(QtGui.QPen(QtCore.Qt.black,2))
        while t<=3.14:
            f = 0
            while f<=3.14*2:
                x = r*math.sin(f)*math.cos(t)+a
                y = r*math.sin(f)*math.sin(t)+b
                z = r*math.cos(f)+c

                # x = r * sinψcosθ, y = r * sinψsinθ, z = r * cosψ, 其中0≤ψ≤π, 0≤θ≤2
                # π

                x2 = x/(1+z/d)
                y2 = y/(1+z/d)

                f += add

                x3 = r * math.sin(f) * math.cos(t) + a
                y3 = r * math.sin(f) * math.sin(t) + b
                z3 = r * math.cos(f) + c

                x4 = x3 / (1 + z3 / d)
                y4 = y3 / (1 + z3 / d)

                f -= add
                # x2 = d*(y-x)/(x-z+math.sqrt(2)*r)
                # y2 = 2*d*y/(math.sqrt(2)*x-math.sqrt(2)*z+2*r)
                qp.drawLine(int(x2),int(y2),int(x4),int(y4))
                #print(x2,y2)
                f += add
            t += add

    def paintEvent(self,e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

def main():

    app = QtGui.QApplication(sys.argv)
    lm = lightMode()
    lm.show()

    sys.exit(app.exec_())

main()