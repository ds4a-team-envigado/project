package com.ampd.pidar.network

import android.util.Log

import java.util.*

/**
 *  @author Arley Duarte arleymauricio@gmail.com
 * Created by arley on 2/2/18.
 */

class APIController constructor(serviceInjection: ServiceInterface): ServiceInterface {

    companion object {
        val API_ERROR = "XERROR"
    }




    private val service: ServiceInterface = serviceInjection


    override fun postSimple(path: String, params: HashMap<String, String>, completionHandler: (response: String?) -> Unit) {
        service.postSimple(path, params,  completionHandler)
    }



    override fun get(path: String, completionHandler: (response: String?) -> Unit) {
        service.get(path, completionHandler)
    }





}
