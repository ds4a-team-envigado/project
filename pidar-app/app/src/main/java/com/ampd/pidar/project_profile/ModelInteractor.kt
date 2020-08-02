package com.ampd.pidar.project_profile

import com.ampd.pidar.PidarForm
import com.ampd.pidar.network.APIController
import com.ampd.pidar.network.ServiceVolley
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import org.jetbrains.annotations.NotNull
import timber.log.Timber

class ModelInteractor {

    fun evaluate(
        responseActionDelegate: @NotNull ModelResponseDelegate
    ) {

        val service = ServiceVolley()
        val apiController = APIController(service)
        val path = "http://54.217.47.179:5000/evaluate"

        var params =  HashMap<String, String>()
        params.put("department", PidarForm.getInstance().department)


        var questions = PidarForm.getInstance().surveyQuestions

        for(question in questions){
            params.put(question.name, question.answer)
        }


        Timber.d("params ${params}")



        apiController.postSimple(path, params) { response ->

            val json = response.toString()

            try{

                Timber.d("json ${json}")

                var modelResponse = Gson().fromJson(json, PidarModelResponse::class.java)


                responseActionDelegate.didSuccessfully(modelResponse)
            }catch (e: Exception){
                Timber.e(e)
                responseActionDelegate.didNotSuccessfully()
            }

        }


    }


    interface ModelResponseDelegate {
        fun didSuccessfully(modelResponse: PidarModelResponse)
        fun didNotSuccessfully()


    }
}