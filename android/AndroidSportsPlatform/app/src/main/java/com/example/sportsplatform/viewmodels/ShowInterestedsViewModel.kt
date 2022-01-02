package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.responses.GetInterestedsOfEventResponse
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.util.Coroutines

class ShowInterestedsViewModel(
    private val eventRepository: EventRepository
) : ViewModel() {

    var eventId: Int? = null

    var interestedsOfEvent: MutableLiveData<GetInterestedsOfEventResponse> = MutableLiveData()

    fun getInterestedsOfEvent() {
        Coroutines.main {
            interestedsOfEvent.postValue(eventRepository.getInterestedsOfEvent(eventId).body())
        }
    }
}