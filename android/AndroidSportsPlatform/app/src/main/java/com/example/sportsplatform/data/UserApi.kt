package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.TokenResponse
import com.example.sportsplatform.data.models.UserRegisterRequest
import com.example.sportsplatform.data.models.UserRegisterResponse
import com.example.sportsplatform.data.models.UserRequest
import com.jakewharton.retrofit2.adapter.kotlin.coroutines.CoroutineCallAdapterFactory
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.POST

interface UserApi {

    @POST("users/login")
    suspend fun searchUser(
        @Body userRequest: UserRequest
    ): Response<TokenResponse>

    @POST("users")
    suspend fun registerUser(
        @Body userRegisterRequest: UserRegisterRequest
    ): Response<UserRegisterResponse>

    companion object{
        operator fun invoke() : UserApi {
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
                .baseUrl("http://13.59.0.178:8080")
                .addCallAdapterFactory(CoroutineCallAdapterFactory())
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(UserApi::class.java)
        }
    }

}