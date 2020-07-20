package com.ampd.pidar

import com.ampd.pidar.project_profile.ListQuestion
import com.ampd.pidar.project_profile.Survey
import org.junit.Test

import org.junit.Assert.*

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
class PidarUnitTest {
    @Test
    fun getNextQuestion_Test() {
        var survey =  Survey();
        var question = survey.nextQuestion;
        assertNotNull(question)

        var question2 = survey.nextQuestion;

        assertEquals("¿Tienes antecedentes de tipo judicial fiscal o disciplinario?", question2.question)
    }


    @Test
    fun getChainProduction_Test() {
        var survey =  Survey();
        var question = survey.nextQuestion;
        var question2 = survey.nextQuestion;
        var question3 = survey.nextQuestion as ListQuestion;


        assertFalse( question3.options.isEmpty())
    }
}