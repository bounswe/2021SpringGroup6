package com.example.sportsplatform.viewmodels

import android.content.ContentValues.TAG
import android.content.SharedPreferences
import android.nfc.Tag
import android.util.Log
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.AddBadgeRequest
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

    val user: MutableLiveData<UserResponse> = MutableLiveData()

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

    fun fetchUsersBadgeList(userId: Int) {
        Coroutines.main {
            usersBadgeList.postValue(
                userRepo.getUsersBadges(
                    userId
                ).body()
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
            )
            Log.d(TAG, addNewBadge.toString())
        }
    }

}