package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.TokenResponse
import com.example.sportsplatform.data.models.UserRegisterRequest
import com.example.sportsplatform.data.models.UserRegisterResponse
import com.example.sportsplatform.data.models.UserRequest
import retrofit2.Response

class Repository(private val api: UserApi) {
    suspend fun findUser(userRequest: UserRequest) : Response<TokenResponse> {
        return api.searchUser(userRequest)
    }
    suspend fun signUser(userRegisterRequest: UserRegisterRequest) : Response<UserRegisterResponse> {
        return api.registerUser(userRegisterRequest)
    }
}