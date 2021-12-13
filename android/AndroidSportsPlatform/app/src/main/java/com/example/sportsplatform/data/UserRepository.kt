package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.*
import retrofit2.Response

class UserRepository(private val api: UserApi) {
    suspend fun findUser(userRequest: UserRequest) : Response<TokenResponse> {
        return api.searchUser(userRequest)
    }
    suspend fun signUser(userRegisterRequest: UserRegisterRequest) : Response<UserRegisterResponse> {
        return api.registerUser(userRegisterRequest)
    }
    suspend fun searchUserProfile(userId : Int) : Response<UserSearchResponse> {
        return api.searchProfile(userId)
    }
}