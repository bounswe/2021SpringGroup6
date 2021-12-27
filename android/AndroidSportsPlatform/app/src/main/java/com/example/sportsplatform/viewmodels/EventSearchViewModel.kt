package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.activities.EventListActivity
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.closeSoftKeyboard
import com.example.sportsplatform.util.toast

class EventSearchViewModel(private val eventRepo: EventRepository) : ViewModel() {

    val eventsFiltered: MutableLiveData<EventFilterResponse?> = MutableLiveData()
    val eventSearchKey: MutableLiveData<CharSequence?> = MutableLiveData()

    fun fillSearchEventList(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            eventsFiltered.postValue(
                eventRepo.findFilterEvents(
                    EventFilterRequest(
                        nameContains = eventSearchKey.value.toString()
                    )
                ).body()
            )
        }
    }
}