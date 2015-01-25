using UnityEngine;
using System.Collections;

public class sammutus : MonoBehaviour {

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () 
	{
		if (Input.GetKey(KeyCode.Escape))
		{
			Application.Quit();
		}
		else if (Input.GetKey(KeyCode.R))
		{
			Application.LoadLevel (Application.loadedLevel);
		}
	}

	void OnMouseDown()
	{
		Application.LoadLevel (Application.loadedLevel);
	}
}
