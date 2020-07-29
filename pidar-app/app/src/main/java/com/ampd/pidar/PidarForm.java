package com.ampd.pidar;

import com.ampd.pidar.geolocation.Municipality;

import java.util.ArrayList;

public class PidarForm {

    private String department = "";

    private ArrayList<Municipality> municipalities  = new ArrayList<Municipality>();

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    private static PidarForm instance = null;

    private PidarForm() {

    }

    public static PidarForm getInstance() {
        if (instance == null) {
            synchronized (PidarForm.class) {
                if (instance == null) {
                    instance = new PidarForm();
                }
            }
        }
        return instance;
    }

    public ArrayList<Municipality> getMunicipalities() {
        return municipalities;
    }

    public void setMunicipalities(ArrayList<Municipality> municipalities) {
        this.municipalities = municipalities;
    }
}
