package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.SignUpRequest
import com.example.sportsplatform.data.models.TokenResponse
import com.example.sportsplatform.data.models.UserRequest
import retrofit2.Response

class Repository(private val api: UserApi) {
    suspend fun findUser(userRequest: UserRequest) : Response<TokenResponse> {
        return api.searchUser(userRequest)
    }
    suspend fun signUpUser(signUpRequest: SignUpRequest) : Response<SignUpRequest> {
        return api.registerUser(signUpRequest)
    }
}