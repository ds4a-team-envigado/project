package com.ampd.pidar.network


import android.util.Log
import com.android.volley.*
import com.android.volley.toolbox.StringRequest
import org.json.JSONException
import timber.log.Timber
import java.nio.charset.Charset


/**
 * @author Arley Duarte arleymauricio@gmail.com
 * Created by arley on 1/16/18.
 */
class ServiceVolley : ServiceInterface {
    val TAG = ServiceVolley::class.java.simpleName
    val basePath = ""

    override fun get(path: String, completionHandler: (response: String?) -> Unit) {

        Timber.d("/Request GET: $path")

        val stringRequest = object : StringRequest(Method.GET, basePath + path,
            Response.Listener<String> { response ->
                try {
                    //val obj = JSONObject(response)
                    Timber.d( "/get request OK! Response: $response")



                    completionHandler(response)
                } catch (e: JSONException) {
                    e.printStackTrace()
                }
            },
            object : Response.ErrorListener {
                override fun onErrorResponse(volleyError: VolleyError) {

                    completionHandler("VolleyError")


                }
            }) {


        }

        BackendVolley.instance?.addToRequestQueue(stringRequest)
    }

    override fun postSimple(path: String, params: HashMap<String, String>, completionHandler: (response: String?) -> Unit) {


        val stringRequest = object : StringRequest(Method.POST, basePath + path,
            Response.Listener<String> { response ->
                try {

                    Timber.i("/POST request OK! Response: $response")

                    completionHandler(response)
                } catch (e: JSONException) {
                    e.printStackTrace()

                }
            },
            object : Response.ErrorListener {
                override fun onErrorResponse(volleyError: VolleyError) {


                    var errorMessage = "";
                    if(volleyError.networkResponse!= null){
                        val errorR = volleyError.networkResponse.data?.toString(Charset.defaultCharset())
                        errorMessage = errorR.toString()
                    }

                    completionHandler("XERROR"+errorMessage)
                    Timber.i("Error : $volleyError")



                }
            }) {



            override fun getParams(): MutableMap<String, String> {


                Log.i(TAG, "getParams: " + params.toString())
                return params;
            }
        }



        BackendVolley.instance?.addToRequestQueue(stringRequest)


    }



    private fun isSuccessful(statusCode: Int): Boolean {
        var success = false;

        if (statusCode >= 200 && statusCode > 300) {
            success = true
        }

        return success
    }
}
