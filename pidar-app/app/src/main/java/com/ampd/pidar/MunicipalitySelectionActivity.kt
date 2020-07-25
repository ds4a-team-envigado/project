package com.ampd.pidar

import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import androidx.appcompat.app.AppCompatActivity
import com.ampd.pidar.geolocation.MunicipalitiesProvider
import com.ampd.pidar.geolocation.Municipality
import kotlinx.android.synthetic.main.activity_municipality_selection.*
import kotlinx.android.synthetic.main.content_question.options_spinner
import org.jetbrains.annotations.NotNull
import timber.log.Timber
import java.util.*
import kotlin.collections.ArrayList

class MunicipalitySelectionActivity : AppCompatActivity(),
    @NotNull MunicipalitiesProvider.MunicipalitiesResponseActionDelegate {



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_municipality_selection)
        downloadMunicipalities()
    }


    private fun downloadMunicipalities(){
        val provider = MunicipalitiesProvider()
        provider.getMunicipalities(this)
    }

    override fun didSuccessfully(municipalities: List<Municipality>) {
       Timber.d("didSuccessfully ${municipalities}")
        fillSpinners(municipalities)
        hideProgress()
    }

    private fun hideProgress(){
        progess.visibility = View.GONE
        location_layout.visibility = View.VISIBLE
    }

    private fun fillSpinners(municipalities: List<Municipality>){
        var departments =  ArrayList<String>()
        for (municipality in municipalities)
        {
            if(!departments.contains(municipality.department)){
                departments.add(municipality.department)
            }
        }
        val array: Array<String> = departments.toArray(arrayOfNulls<String>(0))
        Arrays.sort(array)

        fillDepartments(array)
    }

    private fun fillDepartments(departments: Array<String>){
        val dataAdapter: ArrayAdapter<String> =
            ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, departments)

        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        options_spinner.adapter = dataAdapter
    }
}