package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.UserDetailRequest
import com.example.sportsplatform.data.models.responses.GetBadgeResponse
import com.example.sportsplatform.data.models.responses.UserResponse
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.util.Constants
import com.example.sportsplatform.util.Coroutines

class UserDetailViewModel(
    private val userRepo: UserRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {

    var user: MutableLiveData<UserResponse> = MutableLiveData()
    var userId: MutableLiveData<Int> = MutableLiveData()
    val usersBadgeList: MutableLiveData<GetBadgeResponse> = MutableLiveData()
    val searchBarHint: String = ""

    fun getUserInformation(userId: Int) {
        Coroutines.main {
            val userInformation = userRepo.findUser(
                "Token " + sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, ""),
                UserDetailRequest(user_id = userId)
            ).body()
            user.postValue(userInformation)
        }
    }
    fun fetchUsersBadgeList() {
        Coroutines.main {
            usersBadgeList.postValue(
                userRepo.getUsersBadges(
                    sharedPreferences.getInt(Constants.SHARED_PREFS_USER_ID, 0)
                ).body()
            )
        }
    }
}