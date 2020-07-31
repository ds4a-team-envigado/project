package com.ampd.pidar;

import com.ampd.pidar.geolocation.Municipality;
import com.ampd.pidar.project_profile.Question;

import java.util.ArrayList;

public class PidarForm {

    private String department = "";
    private ArrayList<Question> surveyQuestions  = new ArrayList<Question>();

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

    public void addQuestion(Question question){
        surveyQuestions.add(question);
    }

    public ArrayList<Question> getSurveyQuestions() {
        return surveyQuestions;
    }

    public void clear(){
        surveyQuestions.clear();
    }
}
