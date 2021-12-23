// Reference: https://youtu.be/uD7y4T4PVk0
using System.Collections.Generic;
using UnityEngine;

public static class SaveDataManager
{
    public static bool SaveJsonData(IEnumerable<ISaveable> a_Saveables)
    {
        UnityChanPref unityChanPref = new UnityChanPref();
        foreach (var saveable in a_Saveables)
        {
            saveable.PopulateSaveData(unityChanPref);
        }

        bool isSuccess = FileManager.WriteToFile("UnityChanPrefData01.dat", unityChanPref.ToJson());

        if (isSuccess)
        {
            Debug.Log("Save successful");
        }

        return isSuccess;
    }

    public static bool LoadJsonData(IEnumerable<ISaveable> a_Saveables)
    {

        bool isSuccess = FileManager.LoadFromFile("UnityChanPrefData01.dat", out var json);

        if (isSuccess)
        {
            UnityChanPref unityChanPref = new UnityChanPref();
            unityChanPref.LoadFromJson(json);

            foreach (var saveable in a_Saveables)
            {
                saveable.LoadFromSaveData(unityChanPref);
            }

            Debug.Log("Load complete");
        }

        return isSuccess;
    }
}
