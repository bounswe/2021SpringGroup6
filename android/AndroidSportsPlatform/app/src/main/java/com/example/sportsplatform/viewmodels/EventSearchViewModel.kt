package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.EventRepository
import com.example.sportsplatform.data.UserRepository
import com.example.sportsplatform.data.models.EventFilterResponse

class EventSearchViewModel(private val eventRepo: EventRepository) : ViewModel() {

    val eventLiveData = MutableLiveData<EventFilterResponse>()
}