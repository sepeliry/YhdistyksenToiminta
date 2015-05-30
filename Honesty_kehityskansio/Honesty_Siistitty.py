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

global clickTarget
clickTarget = None

global clickTargetPos
clickTargetPos = None

global bubbleSizeX
bubbleSizeX = 154

global bubbleSizeY
bubbleSizeY = 154

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


#Debug category list, add and remove keywords below to
#take a look at specific events

debugList = []

#debugList.append("leftClick")
#debugList.append("argumentCreation")
#debugList.append("argumentLeftClick")
debugList.append("argumentTextSize")
debugList.append("mousePressEvent")

#debugList.append()

if "/" in sys.path[0]:
    print("Backslash identified")            
else:
    print("Frontslash identified")

class GraphicsArea(QGraphicsView):

    def __init__(self, parent=None):
        super(GraphicsArea, self).__init__(parent)

        global taustaView

class ArgumentDialog(QDialog):
    def __init__(self, parent=None):
        super(ArgumentDialog, self).__init__(parent)

        self.setWindowTitle("New argument")

        #Bottom layout
        shelves = QVBoxLayout()

        #Sublayouts
        topRow = QHBoxLayout()
        midRow = QHBoxLayout()
        botRow = QHBoxLayout()

        shelves.addSpacing(20)
        shelves.addLayout(topRow)
        shelves.addSpacing(20)
        shelves.addLayout(midRow)
        shelves.addSpacing(20)
        shelves.addLayout(botRow)
        shelves.addSpacing(20)

        #Defining the widgets
        instrLabel = QLabel("Give your argument a form")
        argSpace = QTextEdit()
        okButton = QPushButton("Done")
        cancelButton = QPushButton("Cancel")

        #Adding the widgets to the layouts
        
        topRow.addWidget(instrLabel)
        midRow.addWidget(argSpace)
        botRow.addWidget(okButton)
        botRow.addWidget(cancelButton)

        #Activating the bottom layout
        self.setLayout(shelves)

        #Button functionality

        def argFinished():
            #Move the contents of the argument from
            #TextEdit to the target bubble
            global clickTarget
            #print("parent: "+self.parent())
            if "argumentCreation" in debugList:
                #print(dir(clickTarget))
            
                #print(dir(self))
                #print("TextEdit: "+str(dir(argSpace)))
                print("Contained text: "+argSpace.toPlainText())
            #clickTarget.addText

            
            newArgText = QGraphicsTextItem(argSpace.toPlainText(),
                                           parent = clickTarget,
                                           scene = widgettiKeskus["TaustaScene"])

            #print(dir(clickTarget))
            #print(clickTarget.mapFromScene())
            #newArgText.setPos()
            global bubbleSizeX            
            global bubbleSizeY

            if "argumentTextSize" in debugList:
                dirTarget = newArgText.toGraphicsObject().boundingRect().size()
                print(dir(dirTarget))
                print("argumentTextSize dirTarget:"+str(dirTarget))

            #Getting the text size to position it correctly
            textSize = newArgText.toGraphicsObject().boundingRect().size().toTuple()

            #newArgText.toGraphicsObject().boundingRect().size()

            newArgText.setPos(clickTargetPos[0]+bubbleSizeX/2-textSize[0]/2,
                              clickTargetPos[1]+bubbleSizeY/2-textSize[1]/2)

            
            
            #print(dir(newArgText))
            print(clickTarget.pos())
            
            #newArgText.setParentItem(clickTarget)
            

            #textMap.setX(newArgText.x())
            

            if "argumentCreation" in debugList:
                #print(dir(newArgText))
                print("Text inserted into argument")
                print(clickTarget.pos())
                #print(dir(textMap))
                
            self.close()

            
            #clickTarget.setText("rr")
            
            

        def argCancel():
            #Remove the target bubble
            
            self.close()
        
        self.connect(okButton,SIGNAL("clicked()"),argFinished)
        self.connect(cancelButton,SIGNAL("clicked()"),argCancel)
    


class ClickableBox(QGraphicsEllipseItem):    

    def __init__(self, parent=None):
        super(ClickableBox, self).__init__(parent)

        self.setFlag(QGraphicsItem.ItemIsMovable,True)        


    def mousePressEvent(self,event):

        if "mousePressEvent" in debugList:
            print("MousePress event registered")

        
        
        

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
        if event.button() == Qt.MouseButton.LeftButton:
            if "argumentLeftClick" in debugList:
                print("argumentLeftClick category acknowledged")
                

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

        #self.setParent(taustaScene)

        #print(dir(self))
        
        def newArg():

            if "argumentCreation" in debugList:
                
                print("New argument created")

            self.addAction("New connected argument")

            #print(dir(self))

            #keke = widgettiKeskus["Mouse"]
            nelo = ClickableBox()
            taustaScene.addItem(nelo)

            global clickTarget

            clickTarget = nelo
            #poXY = self.mapFromGlobal(widgettiKeskus["Mouse"]).toTuple()
            #poX = poXY[0]
            #poY = poXY[1]
            #print(self.children())
            #xyrr = QCursor().pos().toTuple()
            #print(dir(QCursor()))
            #print(xyrr)

            #Getting the correct coordinates for relocation
            #TODO: when interested, implement this better

            paikkaX = self.posStorage[0]-30
            paikkaY = self.posStorage[1]-60

            #Setting the position for the created item
            
            #nel =

            #Setting the size 
            global bubbleSizeX
            global bubbleSizeY

            
            
            nelo.setRect(paikkaX,paikkaY,bubbleSizeX,bubbleSizeY)

            global clickTargetPos
            clickTargetPos = [paikkaX, paikkaY]

            #Opening a dialog box where the argument is
            #given form (Label, text body, ok and cancel buttons)

            argDialog = ArgumentDialog()
            argDialog.exec_()
            
            #argLista.append(nelo)   self.actionHello = QAction(self)
            #self.actionHello.setText("Woop")    
            

        def logFal():
            print("New logical fallacy proposed")

            lfBox = ClickableBox()
            taustaScene.addItem(nelo)

            paikkaX = self.posStorage[0]-30
            paikkaY = self.posStorage[1]-60
            
            #lFal =
            lfBox.setRect(paikkaX,paikkaY,154,154)

            #newEv = QGraphicsSceneMouseEvent(QEvent.Type(0))
            #print(self.pos())

            #print(newEv.scenePos())
            #print(QGraphicsSceneMouseEvent(self.event()).scenePos())
            #print(self.pos().toTuple())

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
        
    def contextMenuEvent(self,event):

        if "contextMenu" in debugList:            
            print("contextmenu position: "+str(event.scenePos().toTuple()))

        #hiiriPaikka = event.scenePos().toTuple()

        qMe = EmptyAreaMenu(self.parent())
        xEv = event.screenPos().toTuple()[0]
        yEv = event.screenPos().toTuple()[1]
        qMe.posStorage = event.scenePos().toTuple()
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

        #def startArgDialog():
            

        #self.connect(EmptyAreaMenu, SIGNAL("Argument()"),startArgDialog)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
                     


