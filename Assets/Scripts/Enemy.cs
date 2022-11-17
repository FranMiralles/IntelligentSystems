using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour
{
    
   void OnTriggerEnter2D(Collider2D other){
   	if(other.gameObject.tag == "Box"){
   		Destroy(other.gameObject);
   		Destroy(gameObject);
   	}
   }
   
   void OnCollisionEnter2D(Collision2D other){
   	if(other.gameObject.tag == "Player"){
   		Destroy(other.gameObject);
   	}
   }
}
