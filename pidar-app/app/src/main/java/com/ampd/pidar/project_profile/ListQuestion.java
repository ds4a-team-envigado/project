package com.ampd.pidar.project_profile;

import java.util.ArrayList;

public class ListQuestion extends  Question {

    private ArrayList<String> options = new ArrayList<>();

    public ArrayList<String> getOptions() {
        return options;
    }

    public void setOptions(ArrayList<String> options) {
        this.options = options;
    }
}
