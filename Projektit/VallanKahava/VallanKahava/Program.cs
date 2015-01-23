/*
 * 
 * Paikat, johona pohojalaaset voi remuta:
 * kirkko
 * kirjasto
 * työ
 * sairaala
 * fallesmanni
 * kauppa
 *
 * Pelin tickit koostuvat n.3 sekunnin jaksoista, 
 * viikko koostuu 60 tickistä
 * Joka viikko pelaaja saa käyttöönsä 50 yksikköä resursseja
 * Resursseja voi allokoida paikkoihin niitä klikkaamalla
 * 
 * Pohojalaasia tuloo lisaa sairaalasta (% maharollisuus kun kay sairaalalla)
 * Pohojalaaset jaa viimeesehen lepohon kirkkohon (% maharollisuus kun kay kirkos)
 * Jos jompi kumpi naista on jo hajalla, peli ei kesta enaa kovan kauaa
 * 
 * Paikasta menoo neliasosa rikki, jos siala kay pohojalaanen ja sialei oo resurssia laitettuna
 * 
*/

using System;

namespace WhatDoAlgorithms
{
	class pohojalaasUkko
	{

		/* Maksimis statti voi olla 100 */

rauhallisuus = 80;
rahna= 80;
ruaka = 80;
tiato = 80;
terveys = 80;
ahkeruus = 80;
toivo = 80;




}
class pohojalaasAkka
{

}
class kirkko
{

	henki.toivo += 2;
	henki.rauhallisuus +=2;


}
class fallesmanni
{
	henki.rauhallisuus += 2;
	henki.ahkeruus += 2;
}

class kirjasto
{
	henki.tiato +=2;
	henki.ahkeruus +=2;
}
class kauppa
{
	henki.ruaka +=2;
	henki.terveys +=2;
}
class työ
{
	henki.rahna += 2;
	henki.tiato += 2;
}
class sairaala
{
	henki.terveys += 2;
	henki.rauhallisuus +=2;

}

class MainClass
{
	public static void Main (string[] args)
	{
		Console.WriteLine ("Hello World!");


	}

}
}