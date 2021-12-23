using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UISystem : MonoBehaviour
{

    private bool ui_popped_up;

    public GameObject model;

    public Button setting_btn;
    public Canvas setting_canvas;

    public Slider max_rotation_slider;
    public Slider ear_max_slider;
    public Slider ear_min_slider;
    public Toggle enable_auto_blink_toggle;
    public Slider mar_max_slider;
    public Slider mar_min_slider;

    public Text log_text;

    // Start is called before the first frame update
    void Start()
    {
        ui_popped_up = false;

        ShowUI(ui_popped_up);
    }

    // Update is called once per frame
    void Update()
    {
        // change the corresponding value in the controller script when the UI is popped up
        if(ui_popped_up)
        {
            model.GetComponent<UnityChanController>().max_rotation_angle = max_rotation_slider.value;
            model.GetComponent<UnityChanController>().ear_max_threshold = ear_max_slider.value;
            model.GetComponent<UnityChanController>().ear_min_threshold = ear_min_slider.value;
            model.GetComponent<UnityChanController>().mar_max_threshold = mar_max_slider.value;
            model.GetComponent<UnityChanController>().mar_min_threshold = mar_min_slider.value;
        }
    }

    // Initialize the UI components with the init values
    public void InitUI()
    {
        max_rotation_slider.value = model.GetComponent<UnityChanController>().max_rotation_angle;
        ear_max_slider.value = model.GetComponent<UnityChanController>().ear_max_threshold;
        ear_min_slider.value = model.GetComponent<UnityChanController>().ear_min_threshold;
        enable_auto_blink_toggle.isOn = model.GetComponent<UnityChanController>().isAutoBlinkActive;
        mar_max_slider.value = model.GetComponent<UnityChanController>().mar_max_threshold;
        mar_min_slider.value = model.GetComponent<UnityChanController>().mar_min_threshold;

        log_text.text = "";
    }

    // Called by the Setting Button and the "Close" Button
    // To show the setting panel (Canvas)
    public void ShowUI(bool toShow)
    {
        setting_canvas.GetComponent<Canvas>().enabled = toShow;
        ui_popped_up = toShow;
    }

    // On Value Changer Listener on the Toggle
    public void SetAutoBlinkActive(bool enabled)
    {
        model.GetComponent<UnityChanController>().EnableAutoBlink(enabled);
    }

    public void SaveData()
    {
        List<ISaveable> saveables = new List<ISaveable> {
            model.GetComponent<UnityChanController>()
        };

        bool isSuccess = SaveDataManager.SaveJsonData(saveables);

        if (isSuccess)
        {
            log_text.text = "Successfully Save Data";
        }
        else
        {
            log_text.text = "Failed to save data";
        }
    }

    public void LoadData()
    {
        List<ISaveable> saveables = new List<ISaveable> {
            model.GetComponent<UnityChanController>()
        };

        bool isSuccess = SaveDataManager.LoadJsonData(saveables);

        if (isSuccess)
        {
            log_text.text = "Successfully Load Data";
        }
        else
        {
            log_text.text = "Failed to load data";
        }
    }

}
