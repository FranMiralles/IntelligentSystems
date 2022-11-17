using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class PruebaFichero : MonoBehaviour
{
	StreamWriter sw = null;
	StreamReader sr = null;
		
	
	// Start is called before the first frame update
	void Start()
	{
        	//Application.persistentDataPath
        		string saveFilePath = "../Prueba/Assets/Files/Data.txt";
        		sw = new StreamWriter(saveFilePath);
        		sr = new StreamReader(saveFilePath);
        		
        		sw.WriteLine("Hola");
        		sw.Close();
        		sr.Close();
        	
	}

    // Update is called once per frame
    void Update()
    {
        
    }
}
