package com.ampd.pidar;

public class PidarForm {

    private String department = "";

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

}
