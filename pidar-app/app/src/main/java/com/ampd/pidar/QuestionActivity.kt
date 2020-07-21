package com.ampd.pidar

import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import androidx.appcompat.app.AppCompatActivity
import com.ampd.pidar.project_profile.ListQuestion
import com.ampd.pidar.project_profile.Question
import com.ampd.pidar.project_profile.QuestionType
import com.ampd.pidar.project_profile.Survey
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.content_question.*

class QuestionActivity : AppCompatActivity() {


    val survey: Survey = Survey();
    lateinit var currentQuestion: Question;


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_question)
        setSupportActionBar(findViewById(R.id.toolbar))

        showNextQuestion()


        yes_answer.setOnClickListener { view ->
            yesOnClick(view);
        }

        no_answer.setOnClickListener { view ->
            noOnClick(view);
        }


        next_button.setOnClickListener { view ->
            nextOnClick(view);
        }
    }

    private fun noOnClick(view: View) {
        showUserMessage(currentQuestion.comment, view)
    }

    private fun nextOnClick(view: View?) {
        showNextQuestion()

    }


    private fun yesOnClick(view: View?) {
        showNextQuestion()

    }


    private fun showUserMessage(message: String, view: View){
        Snackbar.make(view, message, Snackbar.LENGTH_LONG)
            .setAction("Action", null).show()
    }


    private fun  showNextQuestion(){
        hideQuestionOptions()

        currentQuestion  = survey.nextQuestion
        question.text = currentQuestion.question
        if(currentQuestion.type == QuestionType.YES_NO){
            yes_no_layout.visibility = View.VISIBLE;

        }

        if(currentQuestion.type == QuestionType.LIST){
            options_layout.visibility = View.VISIBLE
            next_button.visibility = View.VISIBLE

            val questionList = currentQuestion as ListQuestion;
            val categories = questionList.getOptions()
            val dataAdapter: ArrayAdapter<String> =
                ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, categories)

            dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

            options_spinner.adapter = dataAdapter
        }

        if(currentQuestion.type == QuestionType.NUMERIC){
            numeric_layout.visibility = View.VISIBLE;
            next_button.visibility = View.VISIBLE
        }
    }

    private fun hideQuestionOptions(){
        yes_no_layout.visibility = View.GONE
        options_layout.visibility = View.GONE
        numeric_layout.visibility = View.GONE
        next_button.visibility = View.GONE

    }
}