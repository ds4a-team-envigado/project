package com.ampd.pidar

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.ampd.pidar.geolocation.Municipality

class MunicipalityActivity : AppCompatActivity() {

    lateinit var municipalities: List<Municipality>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_municipality)


    }

    fun downloadMunicipalities(){

    }
}