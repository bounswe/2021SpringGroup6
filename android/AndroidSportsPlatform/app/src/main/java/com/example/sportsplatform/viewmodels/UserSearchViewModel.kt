package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.UserSearchRequest
import com.example.sportsplatform.data.models.responses.UserSearchResponse
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.util.Coroutines

class UserSearchViewModel(private val userRepo: UserRepository) : ViewModel() {

    val usersSearched: MutableLiveData<UserSearchResponse?> = MutableLiveData()

    fun fillSearchUserList(userSearchKey: String?) {
        Coroutines.main {
            usersSearched.postValue(
                userRepo.userSearch(
                    UserSearchRequest(
                        identifier = userSearchKey ?: ""
                    )
                ).body()
            )
        }
    }
}