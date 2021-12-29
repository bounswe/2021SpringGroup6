package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.responses.GetBadgeResponse
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.util.Constants
import com.example.sportsplatform.util.Coroutines

class DetailedUserViewModel(
    private val userRepo: UserRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {
    val usersBadgeList: MutableLiveData<GetBadgeResponse> = MutableLiveData()
    val searchBarHint: String = ""

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