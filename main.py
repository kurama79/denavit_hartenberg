'''
Tarea 04 - Simulacion DEnavit Hatenberg
    En este programa haremos una simulacion en la cual veremos un brazo con 4 articulaciones, en las cuales
    podemos variar sus angulos y ver la posicion fianl del extremo del brazo con ayuda de obtencion de la
    matriz Denavit Hatenberg por eslabon.

'''

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar ) 
import numpy as np
import sys
import p_fkdh as fk
from armgui import *

class testqt5(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        #init
        self.initState()
        self.draw2()
        self.labels1.setText("Angle 1: "+str(self.hslider1.value())+u'\N{DEGREE SIGN}')
        self.labels2.setText("Angle 2: "+str(self.hslider2.value())+u'\N{DEGREE SIGN}')
        self.labels3.setText("Angle 3: "+str(self.hslider3.value())+u'\N{DEGREE SIGN}') 
        self.labels4.setText("Angle 4: "+str(self.hslider4.value())+u'\N{DEGREE SIGN}') 

        #process
        self.pushButton_reset.clicked.connect(self.initState)
        self.pushButton1.clicked.connect(self.draw1)
        self.pushButton2.clicked.connect(self.draw2)
        self.hslider1.valueChanged.connect(self.s1label)
        self.hslider2.valueChanged.connect(self.s2label)
        self.hslider3.valueChanged.connect(self.s3label)
        self.hslider4.valueChanged.connect(self.s4label)

    def initState(self):
        j1=90
        j2=60
        j3=-60
        j4=-60
        self.hslider1.setProperty("value", j1)
        self.hslider2.setProperty("value", j2)
        self.hslider3.setProperty("value", j3)
        self.hslider4.setProperty("value", j4)

        self.MplWidget.canvas.axes.view_init(20, -120)
        self.draw2()

    def s1label(self):
        self.labels1.setText("Angle 1: "+str(self.hslider1.value())+u'\N{DEGREE SIGN}')
        self.draw2()
    def s2label(self):
        self.labels2.setText("Angle 2: "+str(self.hslider2.value())+u'\N{DEGREE SIGN}')
        self.draw2()
    def s3label(self):
        self.labels3.setText("Angle 3: "+str(self.hslider3.value())+u'\N{DEGREE SIGN}')
        self.draw2() 

    def s4label(self):
        self.labels4.setText("Angle 4: "+str(self.hslider4.value())+u'\N{DEGREE SIGN}')
        self.draw2() 

    def draw1(self): 
        j1=self.hslider1.value()
        j2=self.hslider2.value()
        j3=self.hslider3.value()
        j4=self.hslider4.value()
        j=fk.dh_par(j1,j2,j3,j4)
        Tm=fk.dh_kine(j)
        print(Tm)
        ee=fk.el_xyzpos(Tm)
        p0,p1,p2,p3,p4,p5=fk.el_pos2base(Tm)
        x,y,z = ee[0,:],ee[1,:],ee[2,:]

        self.MplWidget.canvas.axes.clear () 
        self.MplWidget.canvas.axes.plot (x,y,z,marker='o', color='green', linewidth=2, markersize=0)
        self.MplWidget.canvas.axes.set_xlabel('x')
        self.MplWidget.canvas.axes.set_ylabel('y')
        self.MplWidget.canvas.axes.set_zlabel('z')
        
        self.MplWidget.canvas.axes.set_xlim([-100,100])
        self.MplWidget.canvas.axes.set_ylim([0,100])
        self.MplWidget.canvas.axes.set_zlim([0,100])

        self.MplWidget.canvas.draw()   

    def draw2(self): 
        j1=self.hslider1.value()
        j2=self.hslider2.value()
        j3=self.hslider3.value()
        j4=self.hslider4.value()
        j=fk.dh_par(j1,j2,j3,j4)
        Tm=fk.dh_kine(j)
        ee=fk.el_xyzpos(Tm)
        p0,p1,p2,p3,p4,p5=fk.el_pos2base(Tm)
        X1,Y1,Z1=ee[0,0:3],ee[1,0:3],ee[2,0:3]
        X2,Y2,Z2=ee[0,2:4],ee[1,2:4],ee[2,2:4]
        X3,Y3,Z3=ee[0,3:5],ee[1,3:5],ee[2,3:5]
        X4,Y4,Z4=ee[0,4:6],ee[1,4:6],ee[2,4:6]

        self.MplWidget.canvas.axes.clear () 
        self.MplWidget.canvas.axes.plot (X1,Y1,Z1, color='green', marker='o', linestyle='solid', linewidth=5, markersize=10)
        self.MplWidget.canvas.axes.plot (X2,Y2,Z2, color='red', marker='o', linestyle='solid', linewidth=5, markersize=10)
        self.MplWidget.canvas.axes.plot (X3,Y3,Z3, color='blue', marker='o', linestyle='solid', linewidth=5, markersize=10)
        self.MplWidget.canvas.axes.plot (X4,Y4,Z4, color='goldenrod', marker='o', linestyle='solid', linewidth=5, markersize=10)
        x4=X4[1]
        y4=Y4[1]
        z4=Z4[1]
        self.MplWidget.canvas.axes.text(x4,y4,z4,'({:.2f}, {:.2f}, {:.2f})'.format(x4,y4,z4), weight='bold', fontsize=12,)
        self.MplWidget.canvas.axes.set_xlabel('x')
        self.MplWidget.canvas.axes.set_ylabel('y')
        self.MplWidget.canvas.axes.set_zlabel('z')
        
        self.MplWidget.canvas.axes.set_xlim([-120,120])
        self.MplWidget.canvas.axes.set_ylim([-20,120])
        self.MplWidget.canvas.axes.set_zlim([0,40])

        self.MplWidget.canvas.draw() 

app = QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=testqt5(MainWindow)
MainWindow.show()
app.exec_()