// Source: https://github.com/UnityTechnologies/UniteNow20-Persistent-Data/blob/main/FileManager.cs

using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class HiyoriPref
{

    public float ear_max_threshold;
    public float ear_min_threshold;

    public float iris_left_ceiling;
    public float iris_right_ceiling;
    public float iris_up_ceiling;
    public float iris_down_ceiling;

    public float mar_max_threshold;
    public float mar_min_threshold;

    public bool change_mouth_form;
    public float mouth_dist_max;
    public float mouth_dist_min;

    // default constructor to create initial value
    public HiyoriPref(float ear_max_threshold = 0.385f,
                      float ear_min_threshold = 0.30f,
                      float iris_left_ceiling = 0.2f,
                      float iris_right_ceiling = 0.85f,
                      float iris_up_ceiling = 0.9f,
                      float iris_down_ceiling = 0.2f,
                      float mar_max_threshold = 1.0f,
                      float mar_min_threshold = 0.0f,
                      bool change_mouth_form = false,
                      float mouth_dist_max = 65.0f,
                      float mouth_dist_min = 55.0f)
    {
        this.ear_max_threshold = ear_max_threshold;
        this.ear_min_threshold = ear_min_threshold;
        this.iris_left_ceiling = iris_left_ceiling;
        this.iris_right_ceiling = iris_right_ceiling;
        this.iris_up_ceiling = iris_up_ceiling;
        this.mar_max_threshold = mar_max_threshold;
        this.mar_min_threshold = mar_min_threshold;
        this.change_mouth_form = change_mouth_form;
        this.mouth_dist_max = mouth_dist_max;
        this.mouth_dist_min = mouth_dist_min;
    }

    public string ToJson()
    {
        return JsonUtility.ToJson(this);
    }

   public void LoadFromJson(string a_Json)
   {
       JsonUtility.FromJsonOverwrite(a_Json, this);
   }
}

public interface ISaveable
{
    void PopulateSaveData(HiyoriPref a_SaveData);
    void LoadFromSaveData(HiyoriPref a_SaveData);
}
