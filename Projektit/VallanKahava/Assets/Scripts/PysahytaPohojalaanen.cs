﻿using UnityEngine;
using System.Collections;

public class PysahytaPohojalaanen : MonoBehaviour 
{

	// Use this for initialization
	void Start () 
	{
	
	}
	
	// Update is called once per frame
	void Update () 
	{
	
	}

	void OnTriggerEnter(Collider other) 
	{
		other.gameObject.rigidbody.velocity = new Vector3(0, 0, 0);
		//other.gameObject.GetComponents<LiikutaPohojalaasta>()
	}
}
