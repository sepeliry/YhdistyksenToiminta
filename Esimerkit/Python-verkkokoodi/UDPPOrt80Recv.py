#!/usr/bin/env python3.3
import socket
import select

#HUOM! Kommentoinnit perustuvat kirjoittajan käsityksiin.
#Suhtautukaa termistöön ja kuvauksiin varauksella :)

#Koodi hakee oman tietokoneen ulkoisen IP-osoitteen.
#Myös muita verkkosivuja kuin googlea pitäisi pystyä käyttämään.

def getExternalIP():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('google.com', 80))
    ip = sock.getsockname()[0]
    sock.close()
    return ip


ServerIP = getExternalIP()

#Kannalle (socket) määritellään protokolla (AF_INET)
#ja yhteystyyppi (Datagrammien heittely)

kolmossukka = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#SOL_SOCKET-osiosta en itse tiedä tarkemmin
#SO_REUSEADDR tarkoittaa ennakkovaroitusta pythonille, että jos kanta on jo
#käytössä, sitä pystytään käyttää tarvittaessa uudelleen. Tämä vain sen
#takia, ettei tarvitse temppuilla jatkuvasti uudelleenkäynnistyksen
#tai muiden hidasteiden kanssa.

kolmossukka.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

#Varataan järjestelmäresurssi, joka koostuu tietokoneen ulkoisesta
#IP-osoitteesta ja portista 80. Portti 80 on yleensä auki, koska verkkoselai-
#met käyttävät sitä. Porteilla on tarkoituksensa, konsultoi esimerkiksi Wiki-
#pediaa ongelmien ennustamiseksi, mikäli haluat käyttää muuta porttia.

kolmossukka.bind((ServerIP, 80))


#h = 0

#Asetetaan tietokone luuppiin
while 1:
    #Estetään portin jumiutuminen...? :)
    
    kolmossukka.setblocking(0)

    #Luuppi nappaa avatusta portista tullutta
    #viestiä 0.005 sekunnin aikaväleillä. Datagrammit ovat vain hetken
    #aikaa olemassa, joten ne pitää napata nopeasti kiinni.

    ready = select.select([kolmossukka], [], [], 0.005)

    #Jos luuppi saa jotakin haaviinsa...
    if ready[0]:
        #Napataan siitä 1024 symbolia. Suositellaan käytettäväksi jotakin
        #2:n potenssia.
        data = kolmossukka.recvfrom(1024)
        #Tulostetaan data käyttäjälle
        print(data)
    #h += 1
