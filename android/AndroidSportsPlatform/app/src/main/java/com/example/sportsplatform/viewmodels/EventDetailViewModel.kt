package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.EventRequest
import com.example.sportsplatform.data.models.responses.EventResponse
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.util.Coroutines

class EventDetailViewModel(
    private val eventRepository: EventRepository
) : ViewModel() {

    var event: MutableLiveData<EventResponse> = MutableLiveData()

    fun getEventInformation(eventId: Int) {
        Coroutines.main {
            event.postValue(eventRepository.findEvent(EventRequest(event_id = eventId)).body())
        }
    }
}