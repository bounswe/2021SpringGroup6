package com.example.sportsplatform.data.repository

import com.example.sportsplatform.data.api.UserApi
import com.example.sportsplatform.data.models.requests.*
import com.example.sportsplatform.data.models.responses.*
import retrofit2.Response

class UserRepository(private val api: UserApi) {

    suspend fun login(userRequest: UserRequest) : Response<TokenResponse> {
        return api.loginUser(userRequest)
    }

    suspend fun logout(token: String) : Response<ResponseMessage> {
        return api.logoutUser(token)
    }

    suspend fun signUser(userRegisterRequest: UserRegisterRequest) : Response<Void>{
        return api.registerUser(userRegisterRequest)
    }

    suspend fun findFilterUsers(userSearchRequest: UserSearchRequest) : Response<UserSearchResponse> {
        return api.filterUsers(userSearchRequest)
    }

    suspend fun findUser(token: String, userDetailRequest : UserDetailRequest) : Response<UserResponse> {
        return api.searchUser(token, userDetailRequest.user_id)
    }

    suspend fun updateUserProfile(
        token: String,
        userId : Int,
        userUpdateRequest: UserUpdateRequest
    ) : Response<String> {
        return api.updateUser(token, userId, userUpdateRequest)
    }

    suspend fun searchFollowingUserProfile(userId : Int) : Response<UserFollowingResponse> {
        return api.searchFollowingProfile(userId)
    }

    suspend fun getUsersParticipatingEvents(token: String, userId: Int): Response<UsersParticipatingEvents> {
        return api.getUsersParticipatingEvents(token, userId)
    }

    suspend fun addBadgeToUser(token: String, userId : Int, addBadgeRequest: AddBadgeRequest): Response<String> {
        return api.addUserBadge(token, userId, addBadgeRequest)
    }

    suspend fun getUsersBadges(userId : Int): Response<GetBadgeResponse> {
        return api.getUsersBadges(userId)
    }
}