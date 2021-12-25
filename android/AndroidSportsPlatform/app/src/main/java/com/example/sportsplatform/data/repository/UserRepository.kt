package com.example.sportsplatform.data.repository

import com.example.sportsplatform.data.api.UserApi
import com.example.sportsplatform.data.models.requests.UserRegisterRequest
import com.example.sportsplatform.data.models.requests.UserRequest
import com.example.sportsplatform.data.models.responses.*
import retrofit2.Response

class UserRepository(private val api: UserApi) {

    suspend fun findUser(userRequest: UserRequest) : Response<TokenResponse> {
        return api.searchUser(userRequest)
    }
    suspend fun signUser(userRegisterRequest: UserRegisterRequest) : Response<Void>{
        return api.registerUser(userRegisterRequest)
    }

    suspend fun searchUserProfile(userId : Int) : Response<UserSearchResponse> {
        return api.searchProfile(userId)
    }

    suspend fun searchFollowingUserProfile(userId : Int) : Response<UserFollowingResponse> {
        return api.searchFollowingProfile(userId)
    }

    suspend fun getUsersParticipatingEvents(token: String, userId: Int): Response<UsersParticipatingEvents> {
        return api.getUsersParticipatingEvents(token, userId)
    }
}