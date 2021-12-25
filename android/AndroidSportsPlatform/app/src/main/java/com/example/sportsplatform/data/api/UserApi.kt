package com.example.sportsplatform.data.api

import com.example.sportsplatform.data.models.*
import com.example.sportsplatform.data.models.requests.UserRegisterRequest
import com.example.sportsplatform.data.models.requests.UserRequest
import com.example.sportsplatform.data.models.responses.*
import com.jakewharton.retrofit2.adapter.kotlin.coroutines.CoroutineCallAdapterFactory
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*

interface UserApi {

    @POST("users/login")
    suspend fun searchUser(
        @Body userRequest: UserRequest
    ): Response<TokenResponse>

    @POST("users")
    suspend fun registerUser(
        @Body userRegisterRequest: UserRegisterRequest
    ): Response<Void>

    @GET("users/{user_id}")
    suspend fun searchProfile(
        @Path("user_id") userId: Int
    ): Response<UserSearchResponse>

    @GET("/users/{user_id}/following")
    suspend fun searchFollowingProfile(
        @Path("user_id") userId: Int
    ): Response<UserFollowingResponse>

    @GET("/users/{user_id}/participating")
    suspend fun getUsersParticipatingEvents(
        @Header("Authorization") token: String,
        @Path("user_id") userId: Int
    ): Response<UsersParticipatingEvents>

    companion object {
        operator fun invoke(): UserApi {
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
                .create(UserApi::class.java)
        }
    }

}