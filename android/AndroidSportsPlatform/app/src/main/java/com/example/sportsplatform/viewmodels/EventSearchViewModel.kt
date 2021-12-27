package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.util.Coroutines

class EventSearchViewModel(private val eventRepo: EventRepository) : ViewModel() {

    val eventsFiltered: MutableLiveData<EventFilterResponse?> = MutableLiveData()

    fun fillSearchEventList(eventSearchKey: String?) {
        Coroutines.main {
            eventsFiltered.postValue(
                eventRepo.findFilterEvents(
                    EventFilterRequest(
                        nameContains = eventSearchKey ?: ""
                    )
                ).body()
            )
        }
    }
}