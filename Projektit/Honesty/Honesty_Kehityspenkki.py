import sys
from os import listdir as ldi
from PySide.QtCore import *
from PySide.QtGui import *

#Getting the center point of a graphics object for centered rotation
#tranX = self.boundingRect().size().toTuple()[0]/2
#tranY = self.boundingRect().size().toTuple()[1]/2

#class RightClickMenu(QWidget):
#    def __init__(self, parent = None):
#        super(RightClickMenu.self).__init__(parent)

ympLista = []
argLista = []

pathToGameFiles = str(sys.path[0])

print("Path to game files: "+str(pathToGameFiles))

print("Image file in the game folder: "+pathToGameFiles+"/"+"ArgumenttiPlaceholder.jpg") #*.jpg")))


#global widgettiKeskus
#widgettiKeskus = {}

"""
Argumentin rakenne keskuskirjastossa:
avaimena toimii ClickableBox-objekti

Sisältönä toimii lista, joka näyttää seuraavalta:
[string(Argumentin sisältö),
string(argumentoineen pelaajan ID),
[hyväksynnät ja hylkäykset eri pelaajilta],
[Yhteydet muihin argumentteihin],
boolean(valmis vai ei),
boolean(Poistettu vai ei),
tuple(argumentin paikkanäkymä koordinaateissa)]

"""
#global argumenttiKeskus
#argumenttiKeskus = {}

"""
Yhteyden rakenne keskuskirjastossa:
Avaimena toimii Connection-objekti (TODO)

Sisältönä toimii lista, joka näyttää seuraavalta:
[[yhteyden alkupäässä oleva argumentti, yhteyden loppupäässä
oleva argumentti], string(argumentoineen pelaajan ID),
boolean(poistettu vai ei),[tuple(yhteyden alkupää näkymässä),
tuple(yhteyden loppupää näkymässä)]]
"""

#global yhteysKeskus
#yhteysKeskus = {}

"""
Pelaajadatan rakenne keskuskirjastossa:
Avaimena toimii pelaajan ID (TODO), pelaajan ID säilyy kentällä
myös sen jälkeen, kun hän on lähtenyt pois.

Sisältönä toimii lista, joka näyttää seuraavalta:
[boolean(Pelaajan läsnäolo, esim. disconnected?),
int(pelaajan pisteet),
[pelaajan muodostamat argumentit ja logfalit],
[pelaajan luomat yhteydet],
boolean(vuorodata siitä, onko pelaajan vuoro vai ei)]

"""

#global pelaajaKeskus
#pelaajaKeskus = {}

#global argumenttiNumero
#argumenttiNumero = 0

if "/" in sys.path[0]:
    print("Backslash identified")            
else:
    print("Frontslash identified")

class GraphicsArea(QGraphicsView):

    def __init__(self, parent=None):
        super(GraphicsArea, self).__init__(parent)       


class ClickableBox(QGraphicsRectItem):    

    def __init__(self, parent=None):
        super(ClickableBox, self).__init__(parent)

        #self.setDragEnabled(True)

        #print(dir(self))

        #self.setFlag(QGraphicsItem.ItemIsSelectable)
        #self.setFlag(QGraphicsItem.ItemIsMovable)
        #self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        #self.setAcceptDrops(True)


        #self.setParentItem()

        #print(form)
        
        #global argumenttiKeskus
        #global pelaajaKeskus      
        """
        Sisältönä toimii lista, joka näyttää seuraavalta:
        [string(Argumentin sisältö),
        string(argumentoineen pelaajan ID),
        [hyväksynnät ja hylkäykset eri pelaajilta],
        [Yhteydet muihin argumentteihin],
        boolean(valmis vai ei),
        boolean(Poistettu vai ei),
        tuple(argumentin paikkanäkymä koordinaateissa)]
        """
        print(self.scenePos())

        """
        argumenttiKeskus[self] =  ["",
                                   "PlayerID",
                                   [],
                                   [],
                                   False,
                                   False,
                                   self.scenePos()]
        """
        
        #self.setAcceptDrops(True)
        #self.setDragEnabled(True)        

        #self.buttonShow = QPushButton(self)
        #self.buttonShow.setText("Button with menu")
        #self.buttonShow.setMenu(self.menu)
        
        #self.layout = QVBoxLayout(self)
        #self.layout.addWidget(self.buttonShow)
        
        
    def mousePressEvent(self, event):
        
        print("deep")

        print(event.button())

        if event.button() == Qt.MouseButton.LeftButton:
            print("prr")
            self.dragActive = True
            
            #print(dir(event))
            #print(dir(self))
            #print(self.scene())
            nayttamo = self.scene()

            moveTarget = self
            
            #print(self.parentItem())
            #print("AARDVAARK")
            
            #nelo = ClickableBox()
            #nayttamo.addItem(nelo)
            #nel = nelo.setRect(100,100,144,154)
            #ympLista.append(nelo)
            #print(dir(nelo))

            #nelo.setData("RREE")
            
            
            #print(dir(nayttamo))

            #nayttamo.addItem(ClickableBox(

            
            #self.addWidget
            
            
        #print(dir(event))
        #print(self)
        #print(dir(self))
        ##print(event.type())
        #print(self.parentWidget())
        #print(dir(event))
        #print(event.scenePos())
        #self.dragEnterEvent(QGraphicsSceneDragDropEvent.DragEnter)
            

    def mouseReleaseEvent(self, event):

        self.oldMove = "z"
        print(str(event.button())+" hurr")
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragActive = False
        
        
        #soundThread()
           
    
    def mouseMoveEvent(self, event):

        
        
        jiit = "i"

        
        
        #moveTarget.newMove = (traX,traY)        

        #def dragEnterEvent(self, event):

        

        """

        #FIXME: Vain ensimmäisenä klikattu laatikko drag&droppautuu
        try:

            #
            moveTarget.setPos(moveTarget.scenePos().toTuple()[0]+moveTarget.newMove[0]-moveTarget.oldMove[0],moveTarget.scenePos().toTuple()[1]+moveTarget.newMove[1]-moveTarget.oldMove[1])
            #self.setPos(self.scenePos().toTuple()[0]+self.newMove[0]-self.oldMove[0],self.scenePos().toTuple()[1]+self.newMove[1]-self.oldMove[1])
            #self.setPos(self.scenePos().toTuple()[0]+self.newMove[0],self.scenePos().toTuple()[1]+self.newMove[1])

            #midStorage = self.scenePos().toTuple()
            midStorage = moveTarget.scenePos().toTuple()

            #argumenttiKeskus[self][6] = midStorage #self.scenePos().toTuple()
            #print("SELF: "+str(self))
            #print(self)
        except:
            pass            
        moveTarget.oldMove = (traX,traY)
        """
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
    
class EmptyAreaMenu(QMenu):    
    
    def __init__(self, parent=None):
        super(EmptyAreaMenu, self).__init__(parent) 

        #global kaikenNäyttämö

        

        def newArg():
            print("New argument created")
            #print(dir(self))
            #print(self.parent

            
            
            """
            nelo = ClickableBox()
            .addItem(nelo)
            nel = nelo.setRect(100,100,144,154)
            argLista.append(nelo)
            """

        def logFal():
            print("New logical fallacy proposed")

        def skip():
            print("Turn skipped")

        

        #The name of the menu (not displayed)        
        self.setTitle("Argument creation menu")

        #Available actions
        self.addAction("Argument")
        self.addAction("Logical fallacy")
        self.addAction("Skip turn")

        #Getting a grip on the menu choices
        argAct = self.actions()[0]
        falAct = self.actions()[1]
        skipAct = self.actions()[2]        

        #Functions triggered by the actions in the menu
        argAct.triggered.connect(newArg)
        falAct.triggered.connect(logFal)
        skipAct.triggered.connect(skip)

            

class GrSc(QGraphicsScene):

    def __init__(self, parent=None):
        super(GrSc, self).__init__(parent)

        global kaikenNäyttämö

        kaikenNäyttämö = self

    def mouseReleaseEvent(self, event):
        
        print(str(event.button())+" DURR")
        #soundThread()
        #print("Argumenttikeskus: "+str(argumenttiKeskus))
        
    def contextMenuEvent(self,event):

        qMe = EmptyAreaMenu(self.parent())
        xEv = event.screenPos().toTuple()[0]
        yEv = event.screenPos().toTuple()[1]
        qMe.exec_(qMe.actions(),QPoint(xEv,yEv))
        

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

        #print(dir(ymp))

        clickBox = ClickableBox()

        secClickBox = ClickableBox()

        #print(clickBox.GraphicsItemFlags)

        #ima = MovableImage()

        #sce.addItem(ima)
        

        """        
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

        clickBox.setRect(20,20,144,154)

        secClickBox.setRect(100,100,290,190)

        sce.addItem(clickBox)

        sce.addItem(secClickBox)
        
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

        global mouseMovement
        mouseMovement = (0,0)

        def movementTick():

            """
            TODO:
            Keksi keino arvioida aikasyklien välillä, miten varastoida hiiren liikahdukset
            try:
                mouseMovement = (self.newTraX-QMouseEvent.globalPos().toTuple()[0],
                                 self.newTraY-QMouseEvent.globalPos().toTuple()[1])
                self.newTraX = QMouseEvent.globalPos().toTuple()[0]
                #event.scenePos().toTuple()[0]
                self.newTraY = QMouseEvent.globalPos().toTuple()[1]
                #event.scenePos().toTuple()[1]
                mouseMovement = (self.newTraX,self.newTraX)
                #self.moveBy(traX-newTraX,traY-newTraY)
            except:
                pass
            """
        #Creating a timer
        dragTimer = QTimer(self)

        #Connecting the timer ticks to movement
        self.connect(dragTimer, SIGNAL("timeout()"), movementTick)

        #Timer tick intervals and initiation
        dragTimer.start(50)
        

        #Creating a timer
        timer = QTimer(self)

        #Connecting the timer ticks to movement
        self.connect(timer, SIGNAL("timeout()"), centralRotate)

        #Timer tick intervals and initiation
        timer.start(240)        

        #Window name
        self.setWindowTitle("Honesty kehityspenkki")

        #Right-click functionality

        """
        self.actionHello = QAction(self)
        self.actionHello.setText("Woop")

        self.menu = QMenu(self)
        self.menu.addAction(self.actionHello)
        self.setMenu(self.menu)
        """

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
                     


