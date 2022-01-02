package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.UserDetailRequest
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
}