package com.ampd.pidar

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import com.ampd.pidar.project_profile.ModelInteractor
import com.ampd.pidar.project_profile.PidarModelResponse
import com.squareup.picasso.Picasso
import kotlinx.android.synthetic.main.activity_summary.*
import timber.log.Timber

class SummaryActivity : AppCompatActivity(), ModelInteractor.ModelResponseDelegate {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_summary)
        evaluateProject();
    }

    private fun evaluateProject(){
        donwloadChart();
       var modelInteractor =  ModelInteractor();
        modelInteractor.evaluate(this)


    }

    private  fun donwloadChart(){

        var department = PidarForm.getInstance().department

        var chartURL = "https://adrimages.s3-eu-west-1.amazonaws.com/fig_${department.toLowerCase()}.png"

        chartURL = chartURL.replace(' ', '_')
        Timber.d(chartURL)
        Picasso.get().load(chartURL).into(chart);
    }



    override fun didSuccessfully(modelResponse: PidarModelResponse) {
        Timber.d("didSuccessfully")
        showSummaryResponse(modelResponse)
    }

    override fun didNotSuccessfully() {
        Timber.d("didNotSuccessfully")
    }

    private fun showSummaryResponse(modelResponse: PidarModelResponse){
        progess.visibility = View.GONE
        summary_layout.visibility = View.VISIBLE

        var proba = modelResponse.evaluate

        if(proba.length>2)
            proba = proba.substring(0,2)

        probability.setText("${proba}%")
        PidarForm.getInstance().clear()
    }
}