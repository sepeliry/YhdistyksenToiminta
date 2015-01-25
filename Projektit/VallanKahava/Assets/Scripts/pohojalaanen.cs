using UnityEngine;
using System.Collections;

public class pohojalaanen : MonoBehaviour 
{
	public float nalaka;
	// Use this for initialization
	void Start () 
	{
		nalaka = 100;
	}
	
	// Update is called once per frame
	void Update () 
	{
		Debug.Log (nalaka.ToString());
	}


}
