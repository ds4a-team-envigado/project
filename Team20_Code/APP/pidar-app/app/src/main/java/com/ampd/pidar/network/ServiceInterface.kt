package com.ampd.pidar.network

/**
 *  * @author Arley Duarte arleymauricio@gmail.com
 * Created by arley on 1/16/18.
 */
interface ServiceInterface {

    fun postSimple(path: String, params: HashMap<String, String>,  completionHandler: (response: String?) -> Unit)
    fun get(path: String, completionHandler: (response: String?) -> Unit)
}
