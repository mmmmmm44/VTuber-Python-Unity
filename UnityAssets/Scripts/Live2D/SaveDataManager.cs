// Reference: https://youtu.be/uD7y4T4PVk0
using System.Collections.Generic;
using UnityEngine;

public static class SaveDataManager
{
    public static bool SaveJsonData(IEnumerable<ISaveable> a_Saveables)
    {
        HiyoriPref hiyoriPref = new HiyoriPref();
        foreach (var saveable in a_Saveables)
        {
            saveable.PopulateSaveData(hiyoriPref);
        }

        bool isSuccess = FileManager.WriteToFile("HiyoriPrefData01.dat", hiyoriPref.ToJson());

        if (isSuccess)
        {
            Debug.Log("Save successful");
        }

        return isSuccess;
    }

    public static bool LoadJsonData(IEnumerable<ISaveable> a_Saveables)
    {

        bool isSuccess = FileManager.LoadFromFile("HiyoriPrefData01.dat", out var json);

        if (isSuccess)
        {
            HiyoriPref hiyoriPref = new HiyoriPref();
            hiyoriPref.LoadFromJson(json);

            foreach (var saveable in a_Saveables)
            {
                saveable.LoadFromSaveData(hiyoriPref);
            }

            Debug.Log("Load complete");
        }

        return isSuccess;
    }
}
