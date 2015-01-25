using UnityEngine;
using System.Collections;

public class klikkaaNahtavyytta : MonoBehaviour 
{
	public GameObject pohjalaanen;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () 
	{
		
	}

	public void ValittuPohjalaanen(GameObject pohojalaanen_)
	{
		pohjalaanen = pohojalaanen_;
	}

	void OnMouseDown()
	{
		pohjalaanen.GetComponent<LiikutaPohojalaasta>().Osoote = transform.gameObject;
		if (gameObject.name == "LakeudenRisti") 
		{
			if (pohjalaanen.name.Contains ("nainen")) 
			{
				pohjalaanen.GetComponent<aanetPohojalaanen>().KirkkoNainen();
			}
			else if (pohjalaanen.name.Contains ("mies")) 
			{
				pohjalaanen.GetComponent<aanetPohojalaanen>().KirkkoMies();
			}
		}
		else if (gameObject.name == "Koulu") 
		{
			if (pohjalaanen.name.Contains ("nainen")) 
			{
				pohjalaanen.GetComponent<aanetPohojalaanen>().KouluNainen();
			}
			else if (pohjalaanen.name.Contains ("mies")) 
			{
				pohjalaanen.GetComponent<aanetPohojalaanen>().KouluMies();
			}
		}
		else if (gameObject.name == "Kauppa") 
		{
			if (pohjalaanen.name.Contains ("nainen")) 
			{
				pohjalaanen.GetComponent<aanetPohojalaanen>().KauppaNainen();
			}
			else if (pohjalaanen.name.Contains ("mies")) 
			{
				pohjalaanen.GetComponent<aanetPohojalaanen>().KauppaMies();
			}
		}
		else if (gameObject.name == "Poliisi") 
		{
			if (pohjalaanen.name.Contains ("nainen")) 
			{
				pohjalaanen.GetComponent<aanetPohojalaanen>().PoliisiNainen();
			}
			else if (pohjalaanen.name.Contains ("mies")) 
			{
				pohjalaanen.GetComponent<aanetPohojalaanen>().PoliisiMies();
			}
		}
	}
}
