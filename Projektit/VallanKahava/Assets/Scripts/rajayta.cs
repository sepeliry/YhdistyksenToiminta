using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class rajayta : MonoBehaviour 
{
	private bool rajaytetaanko;
	private float odotus;
	public Text whatTeksti;
	private bool onkoRajaytetty;
	public AudioClip rajahdys;

	private AudioSource source;
	
		// Use this for initialization
	void Start () {
		rajaytetaanko = false;
		onkoRajaytetty = false;
		source = GetComponent<AudioSource>();
	}
	
	// Update is called once per frame
	void Update () 
	{
		if (rajaytetaanko && odotus < Time.time) 
		{
			gameObject.transform.Translate (Vector3.up * 0.5f);
			if(onkoRajaytetty == false)
			   {
				source.PlayOneShot(rajahdys,1);
				onkoRajaytetty = true;
			}

		}
	}

	public void Rajahyta()
	{
		odotus = Time.time + 1;
		rajaytetaanko = true;
		whatTeksti.text = "An Ostrobothnian has become furious!\n" +
			"You have created fury beyond all comprehension!\n" +
			"Prepare for the END!\n" +
			"What are your last actions on Earth?";
	}
}
