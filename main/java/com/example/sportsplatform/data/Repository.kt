package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.UserResponse
import retrofit2.Response

class Repository(private val api: UserApi) {
    suspend fun findUser(city: String) : Response<UserResponse> {
        return api.searchUser(city)
    }
}