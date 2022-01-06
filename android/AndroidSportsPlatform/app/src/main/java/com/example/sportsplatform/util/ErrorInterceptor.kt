package com.example.sportsplatform.util

import okhttp3.Interceptor
import okhttp3.Protocol
import okhttp3.Response
import okhttp3.ResponseBody
import okhttp3.internal.http2.ConnectionShutdownException
import java.io.IOException
import java.lang.Exception
import java.net.SocketTimeoutException
import java.net.UnknownHostException

class ErrorInterceptor : Interceptor {

    @Throws(Exception::class)
    override fun intercept(chain: Interceptor.Chain): Response {
        val request = chain.request()

        try {
            val response = chain.proceed(request)
            val bodyString = response.body()!!.string()

            return response
                .newBuilder()
                .message(bodyString)
                .body(ResponseBody.create(response.body()?.contentType(), bodyString))
                .build()
        } catch (e: Exception) {
            e.printStackTrace()
            var message = ""
            when (e) {
                is SocketTimeoutException -> {
                    message = "Timeout - Please check your internet connection"
                }
                is UnknownHostException -> {
                    message = "Unable to make a connection. Please check your internet"
                }
                is ConnectionShutdownException -> {
                    message = "Connection shutdown. Please check your internet"
                }
                is IOException -> {
                    message = "Server is unreachable, please try again later."
                }
                is IllegalStateException -> {
                    message = "${e.message}"
                }
                else -> {
                    message = "${e.message}"
                }
            }

            return Response.Builder()
                .request(request)
                .protocol(Protocol.HTTP_1_1)
                .code(999)
                .message(message)
                .body(ResponseBody.create(null, "{${e}}")).build()
        }
    }
}