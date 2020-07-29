package com.ampd.pidar.geolocation

import com.ampd.pidar.network.APIController
import com.ampd.pidar.network.ServiceVolley
import com.google.gson.Gson
import org.jetbrains.annotations.NotNull
import timber.log.Timber

class GeolocatorService {

    public fun sendRequest(
        responseActionDelegate: @NotNull ResponseActionDelegate,
        latitude: Double,
        longitude: Double
    ) {

        val service = ServiceVolley()
        val apiController = APIController(service)
        //TODO: Poner latitud
       // val path = "https://run.mocky.io/v3/a65dba6b-c9bb-4739-812a-f402f7468240"

        val path = "http://54.217.47.179:5000/getmunicipality?latitude=${latitude}&longitude=${longitude}"




        apiController.get(path) { response ->

            val json = response.toString()


            try{
                var municipality = Gson().fromJson(json, Municipality::class.java)

                Timber.d("path: ${path} json ${json}")

                responseActionDelegate.didSuccessfully(municipality)
            }catch (e: Exception){
                responseActionDelegate.didNotSuccessfully("");
            }



        }


    }


    interface ResponseActionDelegate {
        fun didSuccessfully(municipality: Municipality)
        fun didNotSuccessfully(error: String)
    }
}