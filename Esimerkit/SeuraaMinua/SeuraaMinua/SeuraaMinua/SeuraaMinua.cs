using System;
using System.Collections.Generic;
using Jypeli;
using Jypeli.Assets;
using Jypeli.Controls;
using Jypeli.Widgets;

using System.Net.Sockets;
using System.Net;
using System.Text;
using System.Linq;

public class SeuraaMinua : PhysicsGame
{
    UdpClient lahetin;
    UdpClient vastaanotin;
    string omaIP;

    public override void Begin()
    {
        PhysicsObject pallo = new PhysicsObject(30, 30);
        pallo.Color = Color.Red;
        Add(pallo);
        AddCollisionHandler(pallo, CollisionHandler.DestroyObject);

        Level.CreateBorders();
        Camera.ZoomToLevel();

        Keyboard.Listen(Key.Escape, ButtonState.Released, ConfirmExit, "");
        Keyboard.Listen(Key.Space, ButtonState.Released, KysyKaverinIP, "");
        Mouse.ListenMovement(0.1, HiiriLiikkuu, "", pallo);

        LuoKentta1();


        // Verkkopelin alustus
        omaIP = Dns.GetHostEntry(Dns.GetHostName()).AddressList.FirstOrDefault(ip => ip.AddressFamily == AddressFamily.InterNetwork).ToString();
        //omaIP = "192.168.1.17";
        MessageDisplay.Add(omaIP); // Näytä oma IP
        lahetin = new UdpClient(27002);
        vastaanotin = new UdpClient(27001);
        vastaanotin.BeginReceive(ViestiTullut, vastaanotin);
    }

    void LuoKentta1()
    {
        // Pyörivä esimerkkipalikka
        PhysicsObject palikka = PhysicsObject.CreateStaticObject(200, 50);
        Add(palikka);
        palikka.AngularDamping = 1.0;
        palikka.AngularVelocity = 3;

        // Pelaajan paikka
        Mouse.PositionOnScreen = new Vector(200, 0);
    }

    void HiiriLiikkuu(AnalogState analogState, PhysicsObject pallo)
    {
        pallo.Position = Mouse.PositionOnScreen;
        pallo.Stop();

        foreach (var go in GetObjects(s => s.Tag is IPAddress))
        {
            string IPJaPaikka = omaIP + ";POS;" + pallo.Position.ToString();
            lahetin.Send(
                Encoding.ASCII.GetBytes(IPJaPaikka),
                IPJaPaikka.Length, go.Tag.ToString(), 27001);
        }
    }

    void LisaaKaverinPallo(IPAddress ip)
    {
        GameObject kaverinPallo = new GameObject(30, 30);
        kaverinPallo.IsVisible = false;
        kaverinPallo.Tag = ip;
        Add(kaverinPallo);
    }

    public void KysyKaverinIP()
    {
        InputWindow iw = new InputWindow("Anna kaverin IP");
        iw.TextEntered += KaveriLisatty;
        Add(iw);
    }

    public void KaveriLisatty(InputWindow ikkuna)
    {
        IPAddress address;
        if (IPAddress.TryParse(ikkuna.InputBox.Text, out address))
        {
            LisaaKaverinPallo(address);
        }
    }

    public void ViestiTullut(IAsyncResult ar)
    {
        // Lue lähetetty viesti (tämä on vaikein juttu kirjoittaa)
        UdpClient c = (UdpClient)ar.AsyncState;
        IPEndPoint receivedIpEndPoint = new IPEndPoint(IPAddress.Any, 0);
        Byte[] receivedBytes = c.EndReceive(ar, ref receivedIpEndPoint);
        string receivedText = ASCIIEncoding.ASCII.GetString(receivedBytes);

        // Erota siitä IP ja koordinaatti
        string[] palat = receivedText.Split(';');
        IPAddress lahettajanIP;

        if (IPAddress.TryParse(palat[0], out lahettajanIP))
        {
            if (palat[1] == "POS")
            {
                string lips = lahettajanIP.ToString();
                // Sinuun otti yhteyttä uusi kaveri
                if (GetObjectsWithTag(lips).Count == 0)
                {
                    LisaaKaverinPallo(lahettajanIP);
                }

                // Päivitä paikka
                GameObject kaveri = GetObjectsWithTag(lips).First();
                kaveri.Position = Vector.Parse(palat[2]);
                kaveri.IsVisible = true;
            }
        }

        // Jatka kuuntelemista
        c.BeginReceive(ViestiTullut, ar.AsyncState);
    }
}
