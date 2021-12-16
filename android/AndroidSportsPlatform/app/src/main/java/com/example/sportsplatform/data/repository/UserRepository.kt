package com.example.sportsplatform.data.repository

import com.example.sportsplatform.data.api.UserApi
import com.example.sportsplatform.data.models.requests.UserRegisterRequest
import com.example.sportsplatform.data.models.requests.UserRequest
import com.example.sportsplatform.data.models.responses.TokenResponse
import com.example.sportsplatform.data.models.responses.UserFollowingResponse
import com.example.sportsplatform.data.models.responses.UserSearchResponse
import retrofit2.Response

class UserRepository(
    private val api: UserApi
) : BaseRepository() {

    suspend fun findUser(
        userRequest: UserRequest
    ) = safeApiCall {
        api.searchUser(userRequest)
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
}