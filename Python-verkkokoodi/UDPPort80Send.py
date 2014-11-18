#!/usr/bin/env python3.3
import socket

Message = 'Halloota halloo'

#Lähettäessä viesti itselle haetaan oman tietokoneen ulkoinen IP
#ulkoiselta verkkosivulta, tässä googlelta.

def getExternalIP():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('google.com', 80))
    ip = sock.getsockname()[0]
    sock.close()
    return ip

#Vaihda ServerIP kaverin koneen ulkoiseksi IP:ksi, jos haluat
#heittää jotakin viestiä kaverille.

ServerIP = getExternalIP()

#Nämä rivit on selitetty vastaanottopuolen koodissa.

lähetyssukka = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
lähetyssukka.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

#Lähetyssocketin sitominen kannattaa tehdä johonkin, joka ei ole tärkeiden
#ohjelmien tiellä (kts. Wikipedia)
lähetyssukka.bind((ServerIP, 8144))

z = 0
#Rajoitetaan lähettäminen kahteensataan viestiin, jottei verkon ylläpitäjä
#suutu meille ;)
while z < 200:
    #Lähetetään viesti, raakoina symboleina formaatissa utf-8.
    #Lähetyssuuntana osoite ServerIP, portti 80
    lähetyssukka.sendto(bytes(Message,'utf-8'),(ServerIP,80))
    z += 1
#Suljetaan portti käytön jälkeen, ettei se jää roikkumaan auki.
#Tämä on ymmärtääkseni vain hyvän käytännön mukaista.
lähetyssukka.close()
