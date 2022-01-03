package com.example.sportsplatform.data.api

import com.example.sportsplatform.data.models.requests.AddBadgeToEventRequest
import com.example.sportsplatform.data.models.responses.BadgesResponse
import com.jakewharton.retrofit2.adapter.kotlin.coroutines.CoroutineCallAdapterFactory
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*

interface BadgeApi {

    @GET("/badges")
    suspend fun getBadges(): Response<BadgesResponse?>

    @POST("/events/{event_id}/badges")
    suspend fun addBadgeToEvent(
        @Header("Authorization") token: String?,
        @Path("event_id") eventId: Int?,
        @Body request: AddBadgeToEventRequest
    ): Response<Void>

    companion object {
        operator fun invoke(): BadgeApi {
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
                .create(BadgeApi::class.java)
        }
    }
}