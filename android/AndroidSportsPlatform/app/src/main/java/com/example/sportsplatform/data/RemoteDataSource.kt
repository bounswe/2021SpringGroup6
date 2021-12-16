package com.example.sportsplatform.data

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class RemoteDataSource {

    companion object{
        private const val BASE_URL = "http://3.20.232.108:8080"
    }

    fun<Api> buildApi(
        api: Class<Api>
    ) : Api {
        return Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(api)
    }

}