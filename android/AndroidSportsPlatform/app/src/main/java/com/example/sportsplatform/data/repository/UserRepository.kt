package com.example.sportsplatform.data.repository

import android.content.ContentValues.TAG
import android.util.Log
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
    ) : Response<Void> {
        return api.updateUser(token, userId, userUpdateRequest)
    }

    suspend fun searchFollowingUserProfile(token: String, userId : Int) : Response<GetFollowingUsersResponse> {
        return api.searchFollowingProfile(token, userId)
    }

    suspend fun unfollowUserProfile(token: String, userId : Int, userUnFollowingRequest: UserUnFollowingRequest) : Response<Void> {
        val unfl = api.unFollowingProfile(token, userId, userUnFollowingRequest)

        Log.d(TAG, "$unfl *****************")

        return unfl
    }

    suspend fun searchFollowedUserProfile(token: String, userId : Int) : Response<GetFollowingUsersResponse> {
        return api.searchFollowedProfile(token, userId)
    }

    suspend fun getUsersParticipatingEvents(token: String, userId: Int): Response<UsersParticipatingEvents> {
        return api.getUsersParticipatingEvents(token, userId)
    }

    suspend fun addBadgeToUser(token: String, userId : Int, addBadgeRequest: AddBadgeRequest): Response<Void> {
        val rr = api.addUserBadge(token, userId, addBadgeRequest)

        Log.d(TAG, "apiRequest $addBadgeRequest")
        Log.d(TAG, "apiReturn $rr")
        Log.d(TAG, "token $token")
        Log.d(TAG, "userId $userId")

        return rr
    }

    suspend fun getUsersBadges(userId : Int): Response<GetBadgeResponse> {
        val tt = api.getUsersBadges(userId)

        Log.d(TAG, "apiReturn $tt")
        Log.d(TAG, "userId $userId")

        return tt
    }

    suspend fun followUserProfile(token: String, userId: Int, userFollowingRequest: UserFollowingRequest): Response<Void> {
        return api.followProfile(token, userId, userFollowingRequest)
    }
}