package com.ampd.pidar.network



import com.google.gson.Gson
import java.util.*

/**
 *  @author Arley Duarte arleymauricio@gmail.com
 * Created by arley on 2/2/18.
 */
class APIRequest {
    var id: String = ""
    var path: String = ""
    var params: HashMap<String, String> = HashMap<String, String>()


    fun generateId(): String {
        return UUID.randomUUID().toString();
    }

    fun getParams(obj: Any): HashMap<String, String> {
        val params = HashMap<String, String>()

        print(params)

        val fields = obj.javaClass.declaredFields

        for (field in fields) {
            field.isAccessible = true

            var value = ""
            if (field.get(obj) != null) {
                try {
                    value = field.get(obj) as String
                    params.put(field.name, value.trim())
                } catch (e: Exception) {
                    // handler
                }


            }


        }

        return params
    }


    override fun toString(): String {
        return Gson().toJson(this)
    }
}