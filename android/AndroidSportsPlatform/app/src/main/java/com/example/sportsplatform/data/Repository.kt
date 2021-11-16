package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.UserRequest
import retrofit2.Response

class Repository(private val api: UserApi) {
    suspend fun findUser(userRequest: UserRequest) : Response<UserRequest> {
        return api.searchUser(userRequest)
    }
}