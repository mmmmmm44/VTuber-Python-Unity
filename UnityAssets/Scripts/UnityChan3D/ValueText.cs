using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ValueText : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }

    public void UpdateValueText(System.Single value)
    {
        this.GetComponent<Text>().text = string.Format("{0:0.0000}", value);
    }
}
