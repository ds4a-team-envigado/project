package com.ampd.pidar

import android.content.Intent
import android.os.Bundle
import android.text.TextUtils
import android.view.View
import android.widget.AdapterView
import android.widget.AdapterView.OnItemSelectedListener
import android.widget.ArrayAdapter
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.ampd.pidar.geolocation.MunicipalitiesProvider
import com.ampd.pidar.geolocation.Municipality
import kotlinx.android.synthetic.main.activity_municipality_selection.*

import org.jetbrains.annotations.NotNull
import timber.log.Timber
import java.util.*
import kotlin.collections.ArrayList


class MunicipalitySelectionActivity : AppCompatActivity(),
    @NotNull MunicipalitiesProvider.MunicipalitiesResponseActionDelegate {


    var municipalities : ArrayList<Municipality> = ArrayList<Municipality>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_municipality_selection)
        downloadMunicipalities()
    }


    private fun downloadMunicipalities(){

        if(municipalities.isEmpty()){
            val provider = MunicipalitiesProvider()
            provider.getMunicipalities(this)
        }else{
            didSuccessfully(municipalities)
        }



    }

    override fun didSuccessfully(municipalities: ArrayList<Municipality>) {
        this.municipalities = municipalities
        Timber.d("didSuccessfully ${municipalities}")
        fillSpinners(municipalities)
        hideProgress()

        next_button.setOnClickListener { view ->
            nextOnClick(view);
        }
    }


    private fun nextOnClick(view: View?) {
        var department = departments_spinner.selectedItem.toString()
        Timber.d("department ${department}")

        PidarForm.getInstance().department  = department
        val intent = Intent(this, QuestionActivity::class.java)
        startActivity(intent)
    }

    override fun didNotSuccessfully() {
        hideProgress()
        location_layout.visibility = View.GONE
        Toast.makeText(this, R.string.not_internet, Toast.LENGTH_LONG).show()
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

        departments_spinner.adapter = dataAdapter

        departments_spinner.setOnItemSelectedListener(object : OnItemSelectedListener {
            override fun onItemSelected(
                parentView: AdapterView<*>?,
                selectedItemView: View,
                position: Int,
                id: Long
            ) {
                Timber.d("setOnItemSelectedListener ${departments[position]}")
                fillMunicipality(departments[position])
            }

            override fun onNothingSelected(parentView: AdapterView<*>?) {
                // your code here
            }
        })
    }

    private fun fillMunicipality(department: String){

        var municipalitiesNames =  ArrayList<String>()

        for (municipality in municipalities)
        {
            if(municipality.department.equals(department) && !TextUtils.isEmpty(municipality.name)){
                  municipalitiesNames.add(municipality.name)
            }
        }
        val array: Array<String> = municipalitiesNames.toArray(arrayOfNulls<String>(0))
        Arrays.sort(array)

        val dataAdapter: ArrayAdapter<String> =
            ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, array)

        dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        municipalities_spinner.adapter = dataAdapter

    }
}