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
        val path = "https://run.mocky.io/v3/f3e20394-f10d-4501-a3e0-79f4cfc9f758"

        apiController.get(path) { response ->

            val json = response.toString()

            try{
                val municipalities = Gson().fromJson<ArrayList<Municipality>>(
                    json,
                    object : TypeToken<ArrayList<Municipality>>() {}.type
                )
                Timber.d("json ${json}")
                responseActionDelegate.didSuccessfully(municipalities)
            }catch (e: Exception){
                Timber.e(e)
                responseActionDelegate.didNotSuccessfully()
            }

        }


    }


    interface MunicipalitiesResponseActionDelegate {
        fun didSuccessfully(municipalities: ArrayList<Municipality>)
        fun didNotSuccessfully()

    }
}