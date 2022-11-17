using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BoxBehaviour : MonoBehaviour
{
    float speed;
    Rigidbody2D rbd;
    
    void Start()
    {
        rbd = gameObject.GetComponent<Rigidbody2D>();
        speed = 2f;
        Destroy(gameObject, 3f);
    }

    void Update()
    {
        rbd.velocity = new Vector2(speed, 0);
    }
}
