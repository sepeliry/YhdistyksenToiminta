import sys
from PySide.QtCore import *
from PySide.QtGui import *
import inspect

#Getting the center point of a graphics object for centered rotation
#tranX = self.boundingRect().size().toTuple()[0]/2
#tranY = self.boundingRect().size().toTuple()[1]/2

class GraphicsArea(QGraphicsView):    

    def __init__(self, parent=None):
        super(GraphicsArea, self).__init__(parent)



class ClickableBox(QGraphicsRectItem):

    

    def __init__(self, parent=None):
        super(ClickableBox, self).__init__(parent)    

        #self.setAcceptDrops(True)
        #self.setDragEnabled(True)
        
    def mousePressEvent(self, event):
        
        print("deep")

        print(dir(event))
        #print(self)
        #print(dir(self))
        ##print(event.type())
        #print(self.parentWidget())
        #print(dir(event))
        #print(event.scenePos())
        #self.dragEnterEvent(QGraphicsSceneDragDropEvent.DragEnter)
            

    def mouseReleaseEvent(self, event):

        print("DragDrop memory cleared")
        self.oldMove = "z"
        #soundThread()
           
    
    def mouseMoveEvent(self, event):

        
        
        traX = event.scenePos().toTuple()[0]
        traY = event.scenePos().toTuple()[1]
        
        self.newMove = (traX,traY)
        
        try:
            
            self.setPos(self.scenePos().toTuple()[0]+self.newMove[0]-self.oldMove[0],self.scenePos().toTuple()[1]+self.newMove[1]-self.oldMove[1])
        except:
            pass            
        self.oldMove = (traX,traY)

"""
class MovableImage():

    def __init__(self, parent=None):
        super(MovableImage, self).__init__(parent) 

    def mousePressEvent(self, event):
        
        print("suup")
        #print(event.type())
        #print(dir(event))
        #print(event.scenePos())            

    def mouseReleaseEvent(self, event):

        print("rop")
        print(self.isUnderMouse)
    
    def mouseMoveEvent(self, event):

        print("diip")

        
        #Getting the center point of a graphics object for centered rotation
        tranX = self.boundingRect().size().toTuple()[0]/2
        tranY = self.boundingRect().size().toTuple()[1]/2
        
        #Moving the center point
        #self.translate(tranX,tranY)

        print(self.pos())
        
        traX = event.scenePos().toTuple()[0]
        traY = event.scenePos().toTuple()[1]
        #print(traX,traY)
        #print(self.parentObject())
        self.setPos(traX-30-tranX,traY-30-tranY)

        #self.translate(-tranX,-tranY)
"""
    

    #def dragEnterEvent(self, event):

    #    print(event.mimeData)
    


class GrSc(QGraphicsScene):

    def __init__(self, parent=None):
        super(GrSc, self).__init__(parent) 

    #def mousePressEvent(self, event):
        
    #print("woop")
        
    

class Form(QDialog):    

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        #Hierarchy:

        #MainWindow
        #Layout
        #GraphicsView
        #GraphicsScene
        #MovableSquare

        #A graphics scene demands a graphics view item
        graphicsArea = GraphicsArea()

        print("Interactive? "+str(graphicsArea.isInteractive()))
        
        #Initialization of the scene
        sce = GrSc()

        #Layout for proper positioning
        layout = QHBoxLayout()      

        disruptionTable = QTabWidget()
        #layout.addWidget(disruptionTable)

        #Adding the graphics area into the layout
        layout.addWidget(graphicsArea)
        self.setLayout(layout)

        #Applying the scene to the graphics view
        graphicsArea.setScene(sce)

        #Backround color change
        sce.setBackgroundBrush(Qt.green)

        #Adding the rectangle to the
        rer = sce.addRect(0,0,20,100)

        ymp = sce.addEllipse(0,-50,34,34)

        #ympHila = QDrag(ymp)

        print(dir(ymp))

        clickBox = ClickableBox()

        secClickBox = ClickableBox()

        #print(clickBox.GraphicsItemFlags)

        #ima = MovableImage()

        #ima.load("/home/arad/Kuvat/plasmaball.jpg")

        #sce.addItem(ima)
        

        """
        TOIMIVAA, MUTTA EI KÄYTÖSSÄ
        
        pMap = pMap.scaled(100,100)        
        
        sce.addPixmap(pMap)

        pMap.fill("red")

        """

        #print(dir(pMap))

        anoPMap = QPixmap(200,200)

        #anoPMap = anoPMap.scaled(200,200)

        #anoPMap.fill("orange")

        #sce.addPixmap(anoPMap)

        ima = QImage()

        #formPx = pMap.toImage()

        #print(type(formPx))

        clickBox.setRect(100,100,144,154)

        secClickBox.setRect(100,100,190,190)

        sce.addItem(clickBox)

        sce.addItem(secClickBox)

        


        #qS = QSound("/home/arad/Musiikki/SoundClips/swamp-01.wav")

        #qS.play()



        #print(qS.isAvailable())

        #print(qS.isFinished())
    
        #print(dir(qS))

        #print(dir(sce))

        #print(rer.pos().y())

        #clickBox.grabMouse()

        #clickBox.color("red")

        #self.connect(moFi,SIGNAL("pressed()"),notif)

        #moBu = MouseBoop()

        #moEv = QMouseEvent(bool, rer, "LeftButton", Qt.MouseButtons, KeyboardModifiers = "LeftShift", "lol")
        
        #inspect.getargspec(QMouseEvent)


        #print(dir(sce))

        #kEv = QKeyEvent("M","R")

        #print(sce.keyPressEvent())

        #print(rer.mousePressEvent(True))

        #print(dir(sce))        

        def notifyM():
            print("Mouse click received")

        #self.connect(clickBox, SIGNAL("honk"), notifyM)        

        #moAr = MouseArea(rer)

        #self.connect(rer, SIGNAL("mousePressEvent()"), notifyM)

        #print(rer.pos().toTuple())

        #Rescaling if necessary
        #rer.scale(1.5,1.5)

        def centralRotate():
            #Getting the center point of a graphics object for centered rotation
            tranX = rer.boundingRect().size().toTuple()[0]/2
            tranY = rer.boundingRect().size().toTuple()[1]/2

            #Moving the center point
            rer.translate(tranX,tranY)

            #Finding the object position to apply relative movement
            poX, poY = rer.pos().toTuple()

            #print(sce.mousePressEvent == True)
            
            #Moving the object itself
            #rer.setPos(poX+3,poY)

            #Rotating the object
            rer.rotate(45)

            #Restoring the rotation point so future rotations are not violated
            rer.translate(-tranX,-tranY)


        #Creating a timer
        timer = QTimer(self)

        #Connecting the timer ticks to movement
        self.connect(timer, SIGNAL("timeout()"), centralRotate)

        #Timer tick intervals and initiation
        timer.start(240)        

        #Window name
        self.setWindowTitle("Central rotation animation")

    
    

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
                     


