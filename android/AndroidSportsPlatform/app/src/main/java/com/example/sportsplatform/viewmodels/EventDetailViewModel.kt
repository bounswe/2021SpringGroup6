package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.EventRequest
import com.example.sportsplatform.data.models.responses.EventResponse
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.util.Constants.SHARED_PREFS_USER_TOKEN
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.toast

class EventDetailViewModel(
    private val eventRepository: EventRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {

    var event: MutableLiveData<EventResponse> = MutableLiveData()
    var eventId: MutableLiveData<Int> = MutableLiveData()

    fun getEventInformation(eventId: Int) {
        Coroutines.main {
            event.postValue(eventRepository.findEvent(EventRequest(event_id = eventId)).body())
        }
    }

    fun sendInterestToEvent(
        view: View
    ) {
        Coroutines.main {
            val token = sharedPreferences.getString(SHARED_PREFS_USER_TOKEN, "")

            val deleteSpectatorRequest = eventRepository.deleteSpectatorRequest(
                "Token $token",
                eventId.value
            )

            view.context.toast(
                if (deleteSpectatorRequest.isSuccessful) "Delete spectator request is sent!"
                else deleteSpectatorRequest.message()
            )

            val sendInterestToEvent = eventRepository.sendInterestToEvent(
                "Token $token",
                eventId.value
            )

            view.context.toast(
                if (sendInterestToEvent.isSuccessful) "Interest sent!" else sendInterestToEvent.message()
            )
        }
    }

    fun participateAsSpectatorToEvent(
        view: View
    ) {
        Coroutines.main {
            val token = sharedPreferences.getString(SHARED_PREFS_USER_TOKEN, "")
            val participateAsSpectatorToEvent = eventRepository.participateAsSpectatorToEvent(
                "Token $token",
                eventId.value
            )

            view.context.toast(
                if (participateAsSpectatorToEvent.isSuccessful) "Participate as spectator sent!"
                else participateAsSpectatorToEvent.message()
            )
        }
    }
}