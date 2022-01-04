package com.example.sportsplatform.viewmodels

import android.content.ContentValues.TAG
import android.content.SharedPreferences
import android.util.Log
import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.AddBadgeToEventRequest
import com.example.sportsplatform.data.models.requests.UserDetailRequest
import com.example.sportsplatform.data.models.requests.UserUpdateRequest
import com.example.sportsplatform.data.models.responses.UserResponse
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.util.Constants
import com.example.sportsplatform.util.Coroutines

class ProfileFragmentViewModel(
    private val userRepo: UserRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {
    val userInformation: MutableLiveData<UserResponse> = MutableLiveData()

    fun getUser() {
        Coroutines.main {
            userInformation.postValue(
                userRepo.findUser(
                    "Token " + sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, ""),
                    UserDetailRequest(user_id = sharedPreferences.getInt(Constants.SHARED_PREFS_USER_ID, 0))
                ).body()
            )
        }
    }

    fun updUser(
        userUpdateRequest : UserUpdateRequest
    ){
        Coroutines.main {
            val response = userRepo.updateUserProfile(
                token = "Token " + sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, ""),
                userId = sharedPreferences.getInt(Constants.SHARED_PREFS_USER_ID, 0),
                userUpdateRequest = userUpdateRequest
            ).body()


            Log.d(TAG, response.toString())
        }
    }
}