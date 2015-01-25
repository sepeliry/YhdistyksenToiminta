using UnityEngine;
using System.Collections;
using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;

public class spaawnaa : MonoBehaviour 
{
	public List <GameObject> akka;
	public List <GameObject> ukko;
	public float spawnTimeSeconds;
	public Text skoret;
	private int pohjalaastenMaaraUkko;
	private int pohjalaastenMaaraAkka;
	private bool aijienVuoro;
	private bool peliLoppu;


	private float aika;


	// Use this for initialization
	void Start () 
	{
		aika = 0;//Time.time + spawnTimeSeconds;
		pohjalaastenMaaraUkko = 0;
		pohjalaastenMaaraAkka = 0;
		aijienVuoro = true;
		skoret.text = "Score 0";
		peliLoppu = false;
	}
	
	// Update is called once per frame
	void Update () 
	{

		if (aika < Time.time && peliLoppu == false) 
		{
			SpawnPohojalaanen();


		}
	}

	void SpawnPohojalaanen()
	{
		if (ukko.Count > pohjalaastenMaaraUkko && aijienVuoro == true) 
		{
			ukko[pohjalaastenMaaraUkko].SetActive (true);
			pohjalaastenMaaraUkko = pohjalaastenMaaraUkko + 1;
			aijienVuoro = false;
		}
		else if (akka.Count > pohjalaastenMaaraAkka && aijienVuoro == false) 
		{
			akka[pohjalaastenMaaraAkka].SetActive (true);
			pohjalaastenMaaraAkka = pohjalaastenMaaraAkka + 1;
			aijienVuoro = true;
		}
		//Instantiate (ukko, transform.position, Quaternion.identity);
		aika = aika + spawnTimeSeconds;
		skoret.text = "Score " + ((pohjalaastenMaaraUkko + pohjalaastenMaaraAkka) * 100).ToString ();
	}

	public void lopeta()
	{
		peliLoppu = true;
		pohjalaastenMaaraUkko = 0;
		pohjalaastenMaaraAkka = 0;
		aijienVuoro = true;
		skoret.text = "Score 0";
		for (int i = 0; i < ukko.Count; i++)
		{
			ukko[i].SetActive (false);
			akka[i].SetActive (false);
		}
	}
}
