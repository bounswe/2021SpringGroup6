package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.UserSearchRequest
import com.example.sportsplatform.data.models.responses.UserSearchResponse
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.util.Coroutines

class UserSearchViewModel(private val userRepo: UserRepository) : ViewModel() {

    var userSearch: UserSearchRequest? = null

    val usersFiltered: MutableLiveData<UserSearchResponse?> = MutableLiveData()

    fun setArguments(userToSearch: UserSearchRequest?) {
        userSearch = userToSearch
    }

    fun fillSearchUserList() {
        Coroutines.main {
            val userSearchRequest =
                UserSearchRequest(
                    identifier = userSearch?.identifier
                )
            usersFiltered.postValue(
                userRepo.findFilterUsers(
                    userSearchRequest
                ).body()
            )
        }
    }
}