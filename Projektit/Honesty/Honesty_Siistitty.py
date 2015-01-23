import sys
from os import listdir as ldi
from PySide.QtCore import *
from PySide.QtGui import *

ympLista = []
argLista = []

pathToGameFiles = str(sys.path[0])

print("Path to game files: "+str(pathToGameFiles))

print("Image file in the game folder: "+pathToGameFiles+"/"+"ArgumenttiPlaceholder.jpg") #*.jpg")))

#global hiiriPaikka
#hiiriPaikka = [0,0]


global widgettiKeskus
widgettiKeskus = {}

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

        global taustaView

class ClickableBox(QGraphicsEllipseItem):    

    def __init__(self, parent=None):
        super(ClickableBox, self).__init__(parent)

        self.setFlag(QGraphicsItem.ItemIsMovable,True)        


    def mousePressEvent(self,event):

        print("tss")
        
        

        #print(dir(event))

        #print(dir(self))
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
        #print(self.scenePos())
        
        #self.setAcceptDrops(True)
        #self.setFlag(QGraphicsItem.ItemIsMovable,True)

        """
        argumenttiKeskus[self] =  ["",
                                   "PlayerID",
                                   [],
                                   [],
                                   False,
                                   False,
                                   self.scenePos()]
        """

    def contextMenuEvent(self,event):

        qMe = ArgumentSettingsMenu(self.parent())
        xEv = event.screenPos().toTuple()[0]
        yEv = event.screenPos().toTuple()[1]
        qMe.exec_(qMe.actions(),QPoint(xEv,yEv))
        

class ArgumentSettingsMenu(QMenu):
    
     def __init__(self, parent=None):
        super(ArgumentSettingsMenu, self).__init__(parent)

        def newConnArg():

            print("New connected argument created")

        self.setTitle("Argument context menu")

        newConArg = self.actions()[0]

        newConArg.triggered.connect(newConnArg)

    
    
class EmptyAreaMenu(QMenu):    
    
    def __init__(self, parent=None):
        super(EmptyAreaMenu, self).__init__(parent)         

        global taustaScene

        def canArg():

            print("On hold. Cancelled.")

        #self.setParent(taustaScene)

        #print(dir(self))
        
        def newArg():
            
            print("New argument created")

            self.addAction("New connected argument")

            nelo = ClickableBox()
            taustaScene.addItem(nelo)
            
            paikkaX = self.posStorage[0]
            paikkaY = self.posStorage[1]

            kokoX = 144
            kokoY = 154

            fontSize = 1       #LateResources
            
            nel = nelo.setRect(paikkaX-kokoX/2,paikkaY-kokoY/2,kokoX,kokoY)

            tekstiOmin = QGraphicsSimpleTextItem(parent = nelo,scene = None)
            tekstiOmin.setText("Zuum")
            tekstiOmin.setPos(paikkaX-5*fontSize*len(tekstiOmin.text()),paikkaY-20)
            
            

        def logFal():
            print("New logical fallacy proposed")

            

            #newEv = QGraphicsSceneMouseEvent(QEvent.Type(0))
            #print(self.pos())

            #print(newEv.scenePos())
            #print(QGraphicsSceneMouseEvent(self.event()).scenePos())
            #print(self.pos().toTuple())

            #HINT: GrabVis

        def skip():
            print("Turn skipped")

        
        #The name of the menu (not displayed)        
        self.setTitle("Argument creation menu")

        #Available actions
        self.addAction("Cancel")
        self.addAction("Argument")
        self.addAction("Logical fallacy")
        self.addAction("Skip turn")

        #Getting a grip on the menu choices
        canAct = self.actions()[0]
        argAct = self.actions()[1]
        falAct = self.actions()[2]
        skipAct = self.actions()[3]        

        #Functions triggered by the actions in the menu

        canAct.triggered.connect(canArg)
        argAct.triggered.connect(newArg)
        falAct.triggered.connect(logFal)
        skipAct.triggered.connect(skip)
        
        #print(dir(self))
        #mopX = self.pos().toTuple()[0]
        #mopY = self.pos().toTuple()[1]

        #print(self.pos().toTuple())
            

class GrSc(QGraphicsScene):


    def __init__(self, parent=None):
        super(GrSc, self).__init__(parent)

        global widgettiKeskus
        widgettiKeskus["TaustaScene"] = self

        def refreshMousePos():

            print("ziip")
            #print(dir(self))
            #print(dir(self.mouseMoveEvent(self)))
            #widgettiKeskus["Mouse"] = (xEv,yEv)

        """
        #Create a mouse position refresh timer
        mouseRefTimer = QTimer(self)

        #Connect the mouse refresh to its timeout
        self.connect(mouseRefTimer, SIGNAL("timeout()"), refreshMousePos)

        #Timer tick intervals and initiation
        mouseRefTimer.start(40)  
        #print("Dooba")

        """
        
        #self.menuCoords = (xEv,yEv)

        #widgettiKeskus["Mouse"] = (xEv,yEv)        

        #print(widgettiKeskus)
        
    def contextMenuEvent(self,event):

        print(event.scenePos().toTuple())

        #hiiriPaikka = event.scenePos().toTuple()

        qMe = EmptyAreaMenu(self.parent())
        xEv = event.screenPos().toTuple()[0]
        yEv = event.screenPos().toTuple()[1]
        qMe.posStorage = event.scenePos().toTuple()
        qMe.exec_(qMe.actions(),QPoint(xEv,yEv))

        
        
        #print(taustaScene.children())
        #widgettiKeskus["Mouse"] = QPoint(xEv,yEv)
        #print(taustaScene.items())

    

        
    
        

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

        global taustaView
        taustaView = graphicsArea

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

        #Adding the rectangle to the scene
        rer = sce.addRect(0,0,20,100)

        

        #rer.setFlag(QGraphicsItem.ItemIsMovable,True)     

        def notifyM():
            print("Mouse click received")

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

        global taustaScene

        taustaScene = sce

        
        

        def refreshMousePos():
        

            #widgettiKeskus["Mouse"] 

            tu = QCursor()
            curse = QCursor.pos()

            #print(dir(tu))

            #print(dir(curse))
            
            #print(mousePosition)
            xEv = curse.x()
            yEv = curse.y()

            

            #mousePosition = (xEv,yEv)
            
            #print(curse)
            
            
        

        

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
                     


