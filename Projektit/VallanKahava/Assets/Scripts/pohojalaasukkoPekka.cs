using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public class pohojalaasukkoPekka : MonoBehaviour 
{
	private double kohoreLuku;
	private int kohoreInreksi;
	public GameObject kirkko;
	public GameObject kauppa;
	public GameObject poliisi;
	public GameObject koulu;

	/* Maksimis statti voi olla 100 */
	
	/* Tarphet ja niiren arvot */
	public Dictionary<string, double> tarveLista =
		new Dictionary<string, double>()
	{
		{"rauhallisuus", 80.0},
		{"rahna", 15.0},
		{"ruaka", 10.0},
		{"tiato", 40.0},
		{"terveys", 5.0},
		{"ahkeruus", 5.0},
		{"toivo", 30.0}

	};


	//VÄLIAIKAISESTI TÄNNE
	private double tuamioLaskuri = 1.0;
	
	/* HUAMIO! Tasta alahappain kaikki rivit pyarahtaa vaan KERRAN kunnes toisim
		 mainitahan */

	/* Paikat ja niiren resurssit */

	//VÄLIAIKAISESTI TÄNNE
	private Dictionary<string, double> resurssiLista =
		new Dictionary<string, double>()
	{
		{"kirkko", 0.0},
		{"tyo", 0.0},
		{"sairaala", 0.0},
		{"oppi", 0.0},
		{"fallesmanni", 0.0},
		{"kauppa", 0.0},
		{"fallesmanni", 0.0}
	};
	
	/* Suunta muarostuu hengen tarpehen mukahan ja sem mihina on resurssia */
	
	private string suunta = "fallesmanni";
	
	/* Vertailuhun kaytettavien lukujen pohojalista */
	
	private List<double> tarveVertaaluLista = new List<double>();
	
	/* Kohthen valinthan kaytettavien nimien lista */
	
	/* Laskutoimitus kohthelle */
	
	/*Alakuarvot, nottei tuu virheeta */
	
	double tarve1 = 0;
	double tarve2 = 0; 
	
	List<string> paikkaLista = new List<string>();

	void Start()
	{
		foreach (string paikka in resurssiLista.Keys)
		{
			paikkaLista.Add(paikka);
		}
	}

	void Update()
	{
		VahennetaanStatseja ();
		TarkistaMesotaanko ();
		/* HUAMIO! Tasta alahappain kaikki rivit pyarahtaa AINA PER TIKITYS kunnes toisim
		 mainitahan */
		/*foreach(string tarvet in tarveLista.Keys)
		{
			tarveLista[tarvet]-=1.0 * tuamioLaskuri;
			
			
		}*/

		/* Kayrahan kaikki lapi ja kattotahan mita itte tarvittoo eniten */
		
		foreach (string paikka in resurssiLista.Keys)
		{
			if (paikka == "kirkko")
			{
				tarve1 = tarveLista["toivo"];
				tarve2 = tarveLista["rauhallisuus"];
				tarveVertaaluLista[0] = resurssiLista[paikka]*(100-tarve1)*(100-tarve2);
			}
			
			if (paikka == "tyo")
			{
				tarve1 = tarveLista["rahna"];
				tarve2 = tarveLista["tiato"];
				tarveVertaaluLista[1] = resurssiLista[paikka]*(100-tarve1)*(100-tarve2);
			}
			if (paikka == "sairaala")
			{
				tarve1 = tarveLista["terveys"];
				tarve2 = tarveLista["rauhallisuus"];
				tarveVertaaluLista[2] = resurssiLista[paikka]*(100-tarve1)*(100-tarve2);
				
			}
			if (paikka == "fallesmanni")
			{
				tarve1 = tarveLista["rauhallisuus"];
				tarve2 = tarveLista["ahkeruus"];
				tarveVertaaluLista[3] = resurssiLista[paikka]*(100-tarve1)*(100-tarve2);
			}
			if (paikka == "oppi")
			{
				tarve1 = tarveLista["tiato"];
				tarve2 = tarveLista["ahkeruus"];
				tarveVertaaluLista[4] = resurssiLista[paikka]*(100-tarve1)*(100-tarve2);
			}
			if (paikka == "kauppa")
			{
				tarve1 = tarveLista["ruaka"];
				tarve2 = tarveLista["terveys"];
				tarveVertaaluLista[5] = resurssiLista[paikka]*(100-tarve1)*(100-tarve2);
			}
			
		}

		/* Inreksin valinta  */
		
		kohoreLuku = tarveVertaaluLista.Max();
		
		kohoreInreksi = tarveVertaaluLista.IndexOf(kohoreLuku);
	}

	void VahennetaanStatseja()
	{
		tarveLista ["tiato"] = tarveLista ["tiato"] - 0.01;
		tarveLista ["ruaka"] = tarveLista ["ruaka"] - 0.01;
		tarveLista ["rauhallisuus"] = tarveLista ["rauhallisuus"] - 0.01;
		tarveLista ["toivo"] = tarveLista ["toivo"] - 0.01;
		/*foreach(string tarvet in tarveLista.Keys)
		{
			tarveLista[tarvet]= tarveLista[tarvet] - 1.0 * 0.1;
		}*/
	}

	void TarkistaMesotaanko()
	{
		if (tarveLista ["rauhallisuus"] <= 0)
		{
			renderer.material.SetColor("_Color", Color.red); 
			gameObject.GetComponent<LiikutaPohojalaasta> ().Riehu(poliisi);
			poliisi.GetComponent<rajayta>().Rajahyta();
		}
		else if (tarveLista ["tiato"] <= 0)
		{
			renderer.material.SetColor("_Color", Color.red); 
			gameObject.GetComponent<LiikutaPohojalaasta> ().Riehu(koulu);
			koulu.GetComponent<rajayta>().Rajahyta();
		}

		else if (tarveLista ["ruaka"] <= 0)
		{
			renderer.material.SetColor("_Color", Color.red); 
			gameObject.GetComponent<LiikutaPohojalaasta> ().Riehu(kauppa);
			kauppa.GetComponent<rajayta>().Rajahyta();
		}
		else if (tarveLista ["toivo"] <= 0) 
		{
			renderer.material.SetColor("_Color", Color.red); 
			gameObject.GetComponent<LiikutaPohojalaasta> ().Riehu(kirkko);
			kirkko.GetComponent<rajayta>().Rajahyta();
		}
	}
	

	/*{"rauhallisuus", 80.0},
	{"rahna", 80.0},
	{"ruaka", 80.0},
	{"tiato", 80.0},
	{"terveys", 80.0},
	{"ahkeruus", 80.0},
	{"toivo", 80.0}*/
}
