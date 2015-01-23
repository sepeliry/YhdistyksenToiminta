#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tämä tiedosto esittelee ja selittää auki 14.1.2015 Seinäjoen pelikerhon 
#  tapaamisessa kirjoitetun puunkasvatusohjelman lähdekoodin. 
# Jos et ehtinyt tapaamiseen, tai jokin asia meni sivu suun, lue
#  allaolevat kommentit ja koodit huolella. Jatketaan tästä sitten seuraavassa
#  tapaamisessa 21.1.2015 niin, että tästä "lelusta" tulee oikea peli.


##################
# 0. Valmistelut
##################
# "import" tuo tämän ohjelman käyttöön erilaisia valmispalikoita.
# "from ... import ..." taasen tietyt valmispalikat.
#  esimerkiksi alla oleva rivi tuo matematiikkamodulista ("math")
#  apuohjelmat, joilla voi laskea sinin ja kosinin. Lisäksi tuodaan käyttöön
#  muuttuja "pi", joka pitää sisällään piin likiarvon (3.14...)
from math import sin, cos, pi
# Seuraavat importit puolestaan ottavat käyttöön Kivy-ohjelmointikirjaston 
#  eri ominaisuuksia:
#  * ohjelman rungon (App)
#  * käyttöliittymän osasen pohjan (Widget)
#  * värit ja viivanpiirto-ominaisuuden (Color, Line)
# Näet vähän alempana miten ja mihin näytä tarvitaan.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
 
##################
# 1. L-systeemit
##################
# L-systeemi on malli kasvien rakenteelle ja kasvulle. Siinä yksinkertaisten
#  sääntöjen avulla voidaan tuottaa monimuotoisia kasvien, eliöiden ja 
#  fraktaalien näköisiä kuvioita.
# Lue L-systeemeistä lisää täältä: http://fi.wikipedia.org/wiki/L-systeemi
axiom = "X"
rules = {"F":"FF", "X":"F[+X]-X"}
# Alla oleva aliohjelma "kasvattaa" L-systeemin kun sille annetaan
#  alkutilanne "start", säännöt "rules" ja syvyys "depth", eli kuinka
#  monta kertaa L-systeemin sääntöjä sovelletaan.
def grow(start, rules, depth):
    # Jos ei enää tarvitse soveltaa sääntöjä, palautetaan alkutilanne.
    if depth==0:
        return start
    # Uusi L-syseemi rakennetaan pala kerrallaan tähän "output"-muuttujaan.
    output = ""
    # Nyt otamme yksi kerrallaan start-muuttujan kirjaimia ja teemme niille
    #  sääntöjen mukaiset korvaukset. Jos kirjanta ei ole säännöstössä se 
    #  otetaan mukaan sellaisenaan "output"-muuttujaan.
    for c in start:
        if c in rules:
            output+=rules[c]
        else:
            output+=c
    # Tässä tehdään rekursio, eli kutsutaan aliohjelmaa itseään sen itsensä 
    #  sisältä. Tämän sisäistäminen voi sattua vähän päähän, mutta ideana 
    #  tässä on, että voimme soveltaa sääntöjä uudestaan ja uudestaan aina
    #  edellisen kierroksen tulokseen (nyt "output"-muuttujassa). Huomaa
    #  myös, että "depth" on aina yhtä pienempi, kunnes se on lopulta 0,
    #  jolloin grow ei enää tee start-merkkijonolle mitään (ja rekursio
    #  siis päättyy)-
    return grow(output, rules, depth-1)
    
# Kokeillaan, että aliohjelma toimii. Python-tulkkiin pitäisi tulostua 
#  merkkijono "FFFF[+FF[+F[+X]-X]-F[+X]-X]-FF[+F[+X]-X]-F[+X]-X", joka siis
#  on L-systeemi, joka lähtee merkkijonosta "X" ja johon on 3 kertaa sovellettu 
#  annettuja sääntöjä.
print( grow(axiom, rules, 3) )

######################################################
# 2. Kivy-ohjelma, joka piirtää L-systeemin ruudulle 
######################################################
# Aloitamme Kivy-ohjelman tekemisen määrittelemällä oman widgetin eli käyttö-
#  liittymän osasen (tekninen termi: käyttöliittymäkomponentti).
# Haluamme Widgetin, joka osaa piirtää L-systeemin määrittämän puun, joten
#  nimeämme sen asianmukaisesti "TreeWidget":iksi.
# Sivuhuomautus: Menemättä kovin syvälle olio-ohjelmointiin, mainittakoon,
#  että teemme tässä uuden luokan, joka perii ominaisuuksia kantaluokaltaan
#  (Pythonin avainsana "class" kertoo tästä). Käytännössä tämä tarkoittaa, 
#  että TreeWidget on siis myös Widget!
class TreeWidget(Widget):
    # __init__ on Pythonin sisäinen aliohjelma (kaksi alaviivaa kielii tästä)
    #  se on olio-ohjelmointitermein konstruktori, eli aliohjelma joka rakentaa
    #  uuden olion. Sitä kutsutaan kun teemme uuden TreeWidget:in.
    def __init__(self, **kwargs):
        # Alla oleva rivi varmistaa, että kaikki kantaluokka Widget:iin 
        #  liittyvät alustustoimenpiteet tulevat tehdyksi.
        super(TreeWidget, self).__init__(**kwargs)
        
        # HUOM! Nyt pääsemme varsinaiseen piirtämiseen. Käytämme Kivyn
        #  Color ja Line ominaisuuksia piirtämisen toteuttamiseen.
        with self.canvas:
            # Asetetaan väri. Väri annetaan muodossa Red, Green, Blue ja arvot
            #  ovat välillä 0.0-1.0. Esimerkin väri on vihreän sävy.
            Color(0.5,1.0,0.1)
            
            # Kasvatetaan uusi L-systeemi, joka siis on tarkoitus piirtää
            #  puuksi/kasviksi heti seuraavana.
            ls = grow(axiom, rules, 5)
            # ls = "FFFF[+FF[+F[+X]-X]-F[+X]-X]-FF[+F[+X]-X]-F[+X]-X"

            # Alla esittelemme pari apumuuttujaa:
            angle = 90 # tämänhetkinen piirtosuunta (kulma asteina)
            position = [400,100] # tämänhetkinen kynän paikka
            stack = [] # pino, jonne tallennamme kynän sijanteja ja suuntia
            
            # Luetaan ja tulkitaan L-systeemimerkkijonossa olevat piirto-ohjeet
            #  yksi kerrallaan.
            for c in ls:
                if c=="F":
                    # "F" käskyn tulee piirtää viiva angle-muuttujan määräämään
                    #  suuntaan.
                    # Lasketaan kuinka pitkä viivan tulee olla x ja y-suunnassa
                    #  käytämme siniä ja kosinia, joita varten kulma tulee 
                    #  muuttaa radiaaneiksi. Vakio 10 on viivan pituus.
                    dx = cos(angle/360.0*2*pi)*10
                    dy = sin(angle/360.0*2*pi)*10
                    # Kivyn Line haluaa piirtokäskyn listana numeroita
                    #  esim. [0,0,100,150] tulkitaan niin, että piirretään
                    #  viiva pisteestä (0,0) pisteeseen (100,150).
                    # Seuraavat 2 riviä rakentavat tämänmuotoisen käskyn.
                    end_position = [position[0]+dx, position[1]+dy]
                    Line( points=position+end_position )
                    # Kynä on nyt siirtynyt piirron päätepisteeseen, joten
                    #  päivitetään tilanne apumuuttujaan.
                    position = end_position
                elif c=="+":
                    # "+" käsky kääntää piirtosuuntaa oikealle.
                    angle+=10
                elif c=="-":
                    # "-" käsky kääntää piirtosuuntaa oikealle.
                    angle-=10
                elif c=="[":
                    # "[" käsky pistää nykyisen suunnan ja sijaniin talteen.
                    stack.append( (angle, position) )    
                elif c=="]":
                    # "]" käsky hakee viimeisimmän muistiin tallennetun 
                    #  suunnan ja sijainnin.
                    angle, position = stack.pop()

# Tämä on Kivy-ohjelmamme, joka näyttäytyy käyttäjälle yhtenä isona
#  TreeWidget:inä.             
class KivyTreeApp(App):
    def build(self):
        return TreeWidget()

# Tämä on Python-taikaa. Kivy-ohjelma luodaan ja ajetaan (run), vain kun tämä
#  tiedosto suoritetaan. __name__ ja "__main__" ovat Pythonin sisäisiä
#  muuttujia ja niiden arvoja. Nämä täytyy vain tietää.
if __name__=="__main__":
    KivyTreeApp().run()
    

    
    
            
            
