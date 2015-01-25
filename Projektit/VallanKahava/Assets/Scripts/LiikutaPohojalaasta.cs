using UnityEngine;
using System.Collections;

public class LiikutaPohojalaasta : MonoBehaviour 
{
	public GameObject NimisMias;
	public GameObject Osoote;
	public float liikkumisnopeus;
	public float kaantymissmuutti;
	public bool liikutaanko;
	public GameObject Sairaala;

	// Use this for initialization
	void Start () 
	{
	
	}
	
	// Update is called once per frame
	void Update () 
	{
		KaannaPohojalaastaSinneMissaOsooteOn ();
		LiikutaPohojalaastaEtiapain ();

	}

	void KaannaPohojalaastaSinneMissaOsooteOn()
	{
		if (Osoote.transform.position.x < transform.position.x) 
		{
			Quaternion target = Quaternion.Euler(0, 180, 0);
			transform.rotation = Quaternion.Slerp(transform.rotation, target, Time.deltaTime * kaantymissmuutti);
		}
		else if (Osoote.transform.position.x > transform.position.x) 
		{
			Quaternion target = Quaternion.Euler(0, 0, 0);
			transform.rotation = Quaternion.Slerp(transform.rotation, target, Time.deltaTime * kaantymissmuutti);
		}
	}

	void LiikutaPohojalaastaEtiapain()
	{
		if (liikutaanko) 
		{
			rigidbody.velocity = (Osoote.transform.position - transform.position) * liikkumisnopeus;
			//rigidbody.AddForce((Osoote.transform.position - transform.position) * liikkumisnopeus * Time.smoothDeltaTime);
		}
	}

	public void Riehu(GameObject Riehumisosoote)
	{
		liikkumisnopeus = liikkumisnopeus * 1;
		Osoote = Riehumisosoote;

		//Sairaala.GetComponent<spaawnaa> ().lopeta ();

	}
}
