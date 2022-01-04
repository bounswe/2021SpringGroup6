package com.example.sportsplatform.viewmodels

import android.content.ContentValues.TAG
import android.content.SharedPreferences
import android.util.Log
import android.view.View
import android.widget.Toast
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.AddBadgeRequest
import com.example.sportsplatform.data.models.requests.UserDetailRequest
import com.example.sportsplatform.data.models.requests.UserFollowingRequest
import com.example.sportsplatform.data.models.requests.UserUnFollowingRequest
import com.example.sportsplatform.data.models.responses.GetBadgeResponse
import com.example.sportsplatform.data.models.responses.GetFollowingUsersResponse
import com.example.sportsplatform.data.models.responses.UserResponse
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.util.Constants
import com.example.sportsplatform.util.Coroutines

class UserDetailViewModel(
    private val userRepo: UserRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {

    val user: MutableLiveData<UserResponse> = MutableLiveData()
    val addUserBadgeResponse: MutableLiveData<String> = MutableLiveData()
    var userId: MutableLiveData<Int> = MutableLiveData()
    val usersBadgeList: MutableLiveData<GetBadgeResponse> = MutableLiveData()
    val usersFollowingList: MutableLiveData<GetFollowingUsersResponse> = MutableLiveData()
    val usersFollowedList: MutableLiveData<GetFollowingUsersResponse> = MutableLiveData()
    val searchBarHint: String = ""
    val unfollowingResponse: MutableLiveData<Int> = MutableLiveData()
    val followingResponse: MutableLiveData<Int> = MutableLiveData()

    fun getUserInformation(userId: Int) {
        Coroutines.main {
            val userInformation = userRepo.findUser(
                "Token " + sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, ""),
                UserDetailRequest(user_id = userId)
            ).body()
            user.postValue(userInformation)
        }
    }

    fun followUser(
        intendedToFollowUserId: Int
    ){
        Coroutines.main{
            val token = sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, "")
            val userId = sharedPreferences.getInt(Constants.SHARED_PREFS_USER_ID, 0)
            val followUser = userRepo.followUserProfile(
                "Token $token",
                userId,
                UserFollowingRequest(intendedToFollowUserId)
            )
            if(followUser.code() == 400){
                followingResponse.postValue(0)
            }else{
                followingResponse.postValue(1)
            }
        }
    }

    fun fetchUsersFollowingList(userId: Int) {
        Coroutines.main {
            val token = sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, "")
            val following = userRepo.searchFollowingUserProfile(
                "Token $token",
                userId
            ).body()
            val followed = userRepo.searchFollowedUserProfile(
                "Token $token",
                sharedPreferences.getInt(Constants.SHARED_PREFS_USER_ID, 0)
            ).body()
            usersFollowingList.postValue(
                following
            )
            usersFollowedList.postValue(
                followed
            )
        }
    }

    fun unfollowUser(
        unfollowingUserId: Int
    ){
        Coroutines.main {
            val token = sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, "")
            val userId = sharedPreferences.getInt(Constants.SHARED_PREFS_USER_ID, 0)
            val following = userRepo.unfollowUserProfile(
                "Token $token",
                userId,
                UserUnFollowingRequest(unfollowingUserId)
            )
            if(following.code() == 400){
                unfollowingResponse.postValue(0)
            }else{
                unfollowingResponse.postValue(1)
            }
        }
    }

    fun fetchUsersBadgeList(userId: Int) {
        Coroutines.main {
            val ee = userRepo.getUsersBadges(
                        userId
                    ).body()
            usersBadgeList.postValue(
                ee
            )
        }
    }

    fun addUserBadge(
        addBadgeRequest: AddBadgeRequest,
        user_id: Int
    ) {
        Coroutines.main {
            val token = sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, "")
            val addNewBadge = userRepo.addBadgeToUser(
                "Token $token",
                user_id,
                addBadgeRequest
            ).body()
        }
    }

}