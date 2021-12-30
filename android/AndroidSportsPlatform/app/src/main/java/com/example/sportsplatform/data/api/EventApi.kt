package com.example.sportsplatform.data.api

import com.example.sportsplatform.data.models.*
import com.example.sportsplatform.data.models.requests.CreateEventRequest
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.responses.CreateEventResponse
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.data.models.responses.EventResponse
import com.jakewharton.retrofit2.adapter.kotlin.coroutines.CoroutineCallAdapterFactory
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*

interface EventApi {

    @GET("events/{event_id}")
    suspend fun searchEvent(
        @Path("event_id") eventId: Int): Response<EventResponse>

    @POST("events/searches")
    suspend fun filterEvents(
        @Body eventFilterRequest: EventFilterRequest
    ): Response<EventFilterResponse>

    @POST("/events")
    suspend fun createEvent(
        @Header("Authorization") token: String,
        @Body createEventRequest: CreateEventRequest
    ): Response<CreateEventResponse>

    @POST("/events/{event_id}/interesteds")
    suspend fun sendInterestToEvent(
        @Header("Authorization") token: String,
        @Path("event_id") eventId: Int?
    ): Response<Unit>

    @POST("/events/{event_id}/spectators")
    suspend fun participateAsSpectatorToEvent(
        @Header("Authorization") token: String,
        @Path("event_id") eventId: Int?
    ): Response<Unit>

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