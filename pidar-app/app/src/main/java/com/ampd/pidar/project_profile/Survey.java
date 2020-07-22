package com.ampd.pidar.project_profile;

import java.util.ArrayList;
import java.util.ListIterator;

public class Survey {
    private int index = 0;

    private ListIterator<Question> li;

    public Survey() {
        ArrayList<Question> questions = new ArrayList<>();



        Question q1 = new Question();
        q1.setQuestion("¿Eres Colombiano y mayor de 16 años?");
        q1.setType(QuestionType.YES_NO);
        q1.setComment("Es requisito habilitante que los beneficiarios, sean de nacionalidad Colombiana y mayores de 16 años");
        questions.add(q1);


        Question q2 = new Question();
        q2.setQuestion("¿Tienes antecedentes de tipo judicial fiscal o disciplinario?");
        q2.setComment("Es requisito habilitante que los beneficiarios, No tener antecedentes de tipo judicial, fiscal o disciplinario");
        q2.setType(QuestionType.YES_NO);
        questions.add(q2);


        ListQuestion q3 = new ListQuestion();
        q3.setQuestion("¿Cuál es la cadena productiva que desea impactar?");
        q3.setType(QuestionType.LIST);

        ArrayList<String> chains = new ArrayList<>();
        chains.add("Arroz");
        chains.add("Café");
        q3.setOptions(chains);
        questions.add(q3);

        Question q4 = new Question();
        q4.setQuestion("¿Cuál es el número de beneficiarios directos que busca impactar con la propuesta?");
        q4.setComment("");
        q4.setType(QuestionType.NUMERIC);
        questions.add(q4);


        li = questions.listIterator();
    }

    public Question getNextQuestion() {


        if (li.hasNext()) {

            Question question = li.next();
            return question;
        }


        return null;

    }
}
