package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.data.models.responses.UsersParticipatingEvents
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.util.Constants.SHARED_PREFS_USER_ID
import com.example.sportsplatform.util.Constants.SHARED_PREFS_USER_TOKEN
import com.example.sportsplatform.util.Coroutines

class HomeViewModel(
    private val userRepository: UserRepository,
    private val eventRepository: EventRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {

    val usersParticipatingEvents: MutableLiveData<UsersParticipatingEvents> = MutableLiveData()
    val eventsCreated: MutableLiveData<EventFilterResponse> = MutableLiveData()

    fun fetchUsersParticipatingEvents() {
        Coroutines.main {
            usersParticipatingEvents.postValue(
                userRepository.getUsersParticipatingEvents(
                    "Token " + sharedPreferences.getString(SHARED_PREFS_USER_TOKEN, ""),
                    sharedPreferences.getInt(SHARED_PREFS_USER_ID, 0)
                ).body()
            )
        }
    }

    fun fetchEventsCreated() {
        Coroutines.main {
            eventsCreated.postValue(eventRepository.findFilterEvents(
                EventFilterRequest(
                    creator = sharedPreferences.getInt(
                        SHARED_PREFS_USER_ID,
                        0
                    )
                )
            ).body())
        }
    }

    suspend fun userLoggingOut() = userRepository.logout(
        "Token " + sharedPreferences.getString(SHARED_PREFS_USER_TOKEN, "")
    )
}