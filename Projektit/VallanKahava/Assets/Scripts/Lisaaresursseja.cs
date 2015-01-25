using UnityEngine;
using System.Collections;

public class Lisaaresursseja : MonoBehaviour 
{
	float MittariTaynna = 200;
	// Use this for initialization
	void Start () 
	{
	
	}
	
	// Update is called once per frame
	void Update () 
	{
	}

	void OnTriggerStay(Collider other) 
	{
		if (gameObject.name == "Koulu")
		{
			other.gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["tiato"] = other.gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["tiato"] + 1;
			//other.gameObject.GetComponent<pohojalaanen> ().tarveList = other.gameObject.GetComponent<pohojalaanen> ().oppi + 1;
			//other.gameObject.GetComponent<pohojalaanen> ().nalaka = other.gameObject.GetComponent<pohojalaanen> ().nalaka + 1;
			if (other.gameObject.GetComponent<pohojalaasukkoPekka> ().tarveLista["tiato"] > MittariTaynna) 
			{
				//other.gameObject.
				other.gameObject.GetComponent<LiikutaPohojalaasta> ().Osoote = transform.FindChild("ulostulo").gameObject;
			}
		}
		if (gameObject.name == "LakeudenRisti")
		{
			other.gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["toivo"] = other.gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["toivo"] + 1;
			//other.gameObject.GetComponent<pohojalaanen> ().tarveList = other.gameObject.GetComponent<pohojalaanen> ().oppi + 1;
			//other.gameObject.GetComponent<pohojalaanen> ().nalaka = other.gameObject.GetComponent<pohojalaanen> ().nalaka + 1;
			if (other.gameObject.GetComponent<pohojalaasukkoPekka> ().tarveLista["toivo"] > MittariTaynna) 
			{
				//other.gameObject.
				other.gameObject.GetComponent<LiikutaPohojalaasta> ().Osoote = transform.FindChild("ulostulo").gameObject;
			}
		}
		if (gameObject.name == "Kauppa")
		{
			other.gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["ruaka"] = other.gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["ruaka"] + 1;
			//other.gameObject.GetComponent<pohojalaanen> ().tarveList = other.gameObject.GetComponent<pohojalaanen> ().oppi + 1;
			//other.gameObject.GetComponent<pohojalaanen> ().nalaka = other.gameObject.GetComponent<pohojalaanen> ().nalaka + 1;
			if (other.gameObject.GetComponent<pohojalaasukkoPekka> ().tarveLista["ruaka"] > MittariTaynna) 
			{
				//other.gameObject.
				other.gameObject.GetComponent<LiikutaPohojalaasta> ().Osoote = transform.FindChild("ulostulo").gameObject;
			}
		}
		if (gameObject.name == "Poliisi")
		{
			other.gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["rauhallisuus"] = other.gameObject.GetComponent<pohojalaasukkoPekka>().tarveLista["rauhallisuus"] + 1;
			//other.gameObject.GetComponent<pohojalaanen> ().tarveList = other.gameObject.GetComponent<pohojalaanen> ().oppi + 1;
			//other.gameObject.GetComponent<pohojalaanen> ().nalaka = other.gameObject.GetComponent<pohojalaanen> ().nalaka + 1;
			if (other.gameObject.GetComponent<pohojalaasukkoPekka> ().tarveLista["rauhallisuus"] > MittariTaynna) 
			{
				//other.gameObject.
				other.gameObject.GetComponent<LiikutaPohojalaasta> ().Osoote = transform.FindChild("ulostulo").gameObject;
			}
		}




	}
}
