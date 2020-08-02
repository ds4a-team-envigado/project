package com.ampd.pidar.project_profile;

public class Question {
    private String question;
    private String comment;

    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }

    private String answer="";
    private String name ="";

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }



    private QuestionType type;

    private boolean isNegativeYes = false;

    public boolean isNegativeYes() {
        return isNegativeYes;
    }

    public void setNegativeYes(boolean negativeYes) {
        isNegativeYes = negativeYes;
    }

    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }

    public QuestionType getType() {
        return type;
    }

    public void setType(QuestionType type) {
        this.type = type;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
}
