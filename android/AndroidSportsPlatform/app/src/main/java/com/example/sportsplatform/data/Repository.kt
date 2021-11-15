package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.TokenResponse
import retrofit2.Response

class Repository(private val api: UserApi) {
    suspend fun findUser(identifier: String, password: String) : Response<TokenResponse> {
        return api.searchUser(identifier, password)
    }
}