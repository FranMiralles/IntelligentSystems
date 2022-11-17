using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
	float velocidad;
	Rigidbody2D rbd;
	float horizontal;
	bool canjump;
	SpriteRenderer sr;
	Animator an;
	public GameObject box;
	public GameObject FirePoint;
	
    void Start()
    {
        rbd = gameObject.GetComponent<Rigidbody2D>();
        sr = gameObject.GetComponent<SpriteRenderer>();
        an = gameObject.GetComponent<Animator>();
        velocidad = 5f;
        canjump = false;
    }


    void Update()
    {
    	horizontal = Input.GetAxisRaw("Horizontal");
    	
    	if(horizontal > 0){
    		rbd.velocity = new Vector2(horizontal * velocidad, rbd.velocity.y);
    		sr.flipX = false;
    		an.SetBool("Run", true);
    		
    	}else if(horizontal < 0){
    		rbd.velocity = new Vector2(horizontal * velocidad, rbd.velocity.y);
    		sr.flipX = true;
    		an.SetBool("Run", true);
    	}
    	else{
    		rbd.velocity = new Vector2(0, rbd.velocity.y);
    		an.SetBool("Run", false);
    	}
    	
    	if(Input.GetKeyDown("up")&& canjump){
    		rbd.AddForce(new Vector2(0, 300f));
    		canjump = false;
    		an.SetBool("Jump", true);
    	}
    	
    	if(rbd.velocity.y < 0){
    		an.SetBool("Fall", true);
    	}
    	
    	//Ataque
    	
    	if(Input.GetKeyDown("space")){
    		//Instantiate();
    		Instantiate(box, FirePoint.transform.position, FirePoint.transform.rotation);
    	}
    }
    
    void OnCollisionEnter2D(Collision2D other){
    	if(other.gameObject.tag == "Ground"){
    		an.SetBool("Jump", false);
    		an.SetBool("Fall", false);
    		canjump = true;
    	}
    }
}
