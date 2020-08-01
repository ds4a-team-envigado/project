package com.ampd.pidar

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.text.TextUtils
import android.view.MenuItem
import android.view.View
import com.ampd.pidar.project_profile.ModelInteractor
import com.ampd.pidar.project_profile.PidarModelResponse
import com.squareup.picasso.Picasso
import kotlinx.android.synthetic.main.activity_summary.*
import kotlinx.android.synthetic.main.activity_summary.next_button


import timber.log.Timber

class SummaryActivity : AppCompatActivity(), ModelInteractor.ModelResponseDelegate {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_summary)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        evaluateProject();
    }


    override fun onOptionsItemSelected(item: MenuItem) = when (item.itemId) {
        android.R.id.home -> {
            onBackPressed()
            true
        }
        else -> false
    }


    private fun evaluateProject(){
        donwloadChart();
       var modelInteractor =  ModelInteractor();
        modelInteractor.evaluate(this)

        next_button.setOnClickListener { view ->
            showFinalInfo();
        }
    }


    fun showFinalInfo(){
        val intent = Intent(this, FinalInfoActivity::class.java)
        startActivity(intent)
    }

    private  fun donwloadChart(){

        var department = PidarForm.getInstance().department

        if(TextUtils.isEmpty(department))
            department = "ANTIOQUIA"

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

        PidarForm.getInstance().clear()

        if(TextUtils.isEmpty(proba)){
            probability.setText(":(")
            summary_no_chain.visibility = View.VISIBLE
            return
        }

        proba = "0";
        if(proba.length > 2)
            proba = proba.substring(0,2)

        probability.setText("${proba}%")
        summary_no_chain.visibility = View.GONE

    }
}