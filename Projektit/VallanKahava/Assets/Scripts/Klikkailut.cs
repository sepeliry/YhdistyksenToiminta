using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class Klikkailut : MonoBehaviour 
{
	public GameObject Kirkko;
	public GameObject Kauppa;
	public GameObject Koulu;
	public GameObject Poliisi;
	public Text statsit;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () 
	{
	
	}

	void OnMouseDown()
	{
		statsit.text = "Stats: \n" + "tiato(Knowledge):" + (int) gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["tiato"] + "\n";
		statsit.text = statsit.text + "rauhallisuus(Calmness):" + (int) gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["rauhallisuus"] + "\n";
		statsit.text = statsit.text + "ruaka(Food):" + (int) gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["ruaka"] + "\n";
		statsit.text = statsit.text + "toivo(Hope):" + (int) gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["toivo"] + "\n";
		Kirkko.GetComponent<klikkaaNahtavyytta>().ValittuPohjalaanen(transform.gameObject);
		Kauppa.GetComponent<klikkaaNahtavyytta>().ValittuPohjalaanen(transform.gameObject);
		Koulu.GetComponent<klikkaaNahtavyytta>().ValittuPohjalaanen(transform.gameObject);
		Poliisi.GetComponent<klikkaaNahtavyytta>().ValittuPohjalaanen(transform.gameObject);

		if (gameObject.name.Contains ("nainen")) 
		{
			gameObject.GetComponent<aanetPohojalaanen>().ValintaNainen();
		}

		if (gameObject.name.Contains ("mies")) 
		{
			gameObject.GetComponent<aanetPohojalaanen>().ValintaMies();
		}
	}
}
