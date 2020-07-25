package com.ampd.pidar.geolocation

import com.ampd.pidar.network.APIController
import com.ampd.pidar.network.ServiceVolley
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import org.jetbrains.annotations.NotNull
import timber.log.Timber

class MunicipalitiesProvider {

    fun getMunicipalities(
        responseActionDelegate: @NotNull MunicipalitiesResponseActionDelegate
    ) {

        val service = ServiceVolley()
        val apiController = APIController(service)
        val path = "https://run.mocky.io/v3/908a4156-dac4-4a84-81c2-a1fbdcb78138"

        apiController.get(path) { response ->

            val json = response.toString()

            val municipalities = Gson().fromJson<List<Municipality>>(
                json,
                object : TypeToken<List<Municipality>>() {}.type
            )
            Timber.d("json ${json}")
            responseActionDelegate.didSuccessfully(municipalities)
        }


    }


    interface MunicipalitiesResponseActionDelegate {
        fun didSuccessfully(municipalities: List<Municipality>)
    }
}