package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.*
import com.jakewharton.retrofit2.adapter.kotlin.coroutines.CoroutineCallAdapterFactory
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface EventApi {

    @GET("events/{event_id}")
    suspend fun searchEvent(
        @Path("event_id") eventId: Int): Response<EventResponse>

    @POST("events/searches")
    suspend fun filterEvents(
        @Body eventFilterRequest: EventFilterRequest
    ): Response<EventFilterResponse>

    companion object{
        operator fun invoke() : EventApi {
            val requestInterceptor = Interceptor { chain ->
                val url = chain.request()
                    .url()
                    .newBuilder()
                    .build()
                val request = chain.request()
                    .newBuilder()
                    .url(url)
                    .build()

                return@Interceptor chain.proceed(request)
            }

            val okHttpClient = OkHttpClient.Builder()
                .addInterceptor(requestInterceptor)
                .build()

            return Retrofit.Builder()
                .client(okHttpClient)
                .baseUrl("http://3.20.232.108:8080")
                .addCallAdapterFactory(CoroutineCallAdapterFactory())
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(EventApi::class.java)
        }
    }
}