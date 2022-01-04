package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.DecideParticipantsRequest
import com.example.sportsplatform.data.models.responses.GetInterestedsOfEventResponse
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.util.Constants
import com.example.sportsplatform.util.Coroutines

class ShowInterestedsViewModel(
    private val eventRepository: EventRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {

    var eventId: Int? = null

    var interestedsOfEvent: MutableLiveData<GetInterestedsOfEventResponse> = MutableLiveData()

    var acceptedUsersList: MutableLiveData<MutableList<Int?>> = MutableLiveData()
    var declinedUsersList: MutableLiveData<MutableList<Int?>> = MutableLiveData()
    var decideParticipantsSuccessful: MutableLiveData<Boolean> = MutableLiveData()

    fun getInterestedsOfEvent() {
        Coroutines.main {
            interestedsOfEvent.postValue(eventRepository.getInterestedsOfEvent(eventId).body())
        }
    }

    fun decideParticipants(accepted: Boolean) {
        Coroutines.main {
            val decideParticipantsResponse = eventRepository.decideParticipants(
                "Token " + sharedPreferences.getString(Constants.SHARED_PREFS_USER_TOKEN, ""),
                eventId,
                DecideParticipantsRequest(
                    accept_user_id_list = acceptedUsersList.value?.toList() ?: listOf(),
                    reject_user_id_list = declinedUsersList.value?.toList() ?: listOf()
                )
            )

            if (decideParticipantsResponse.isSuccessful) {
                decideParticipantsSuccessful.postValue(accepted)
            }
        }
    }
}