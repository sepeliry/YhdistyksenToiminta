using UnityEngine;
using System.Collections;

public class aanetPohojalaanen : MonoBehaviour 
{
	public AudioClip lopetusNainen;
	public AudioClip valintaNainen;
	public AudioClip kauppaNainen;
	public AudioClip kirkkoNainen;
	public AudioClip poliisiNainen;
	public AudioClip kouluNainen;
	public AudioClip lopetusMies;
	public AudioClip valintaMies;
	public AudioClip kauppaMies;
	public AudioClip kirkkoMies;
	public AudioClip poliisiMies;
	public AudioClip kouluMies;
	private AudioSource source;


	// Use this for initialization
	void Start () 
	{
		source = GetComponent<AudioSource>();
	}
	
	// Update is called once per frame
	void Update () 
	{
	}

	public void ValintaNainen()
	{
		source.PlayOneShot(valintaNainen,1);
	}
	public void KauppaNainen()
	{
		source.PlayOneShot(kauppaNainen,1);
	}
	public void KirkkoNainen()
	{
		source.PlayOneShot(kirkkoNainen,1);
	}

	public void PoliisiNainen()
	{
		source.PlayOneShot(poliisiNainen,1);
	}
	public void KouluNainen()
	{
		source.PlayOneShot(kouluNainen,1);
	}
	public void ValintaMies()
	{
		source.PlayOneShot(valintaMies,1);
	}
	public void KauppaMies()
	{
		source.PlayOneShot(kauppaMies,1);
	}
	public void KirkkoMies()
	{
		source.PlayOneShot(kirkkoMies,1);
	}
	public void PoliisiMies()
	{
		source.PlayOneShot(poliisiMies,1);
	}
	public void KouluMies()
	{
		source.PlayOneShot(kouluMies,1);
	}
	public void LopetusNainen()
	{
		source.PlayOneShot(lopetusNainen,1);
	}
	public void LopetusMies()
	{
		source.PlayOneShot(lopetusMies,1);
	}



}
