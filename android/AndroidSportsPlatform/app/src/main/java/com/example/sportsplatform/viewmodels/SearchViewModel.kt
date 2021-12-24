package com.example.sportsplatform.viewmodels

import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.util.Coroutines

class SearchViewModel(
    private val repository: EventRepository
) : ViewModel() {

    val eventsFiltered: MutableLiveData<EventFilterResponse?> = MutableLiveData()
    val eventSearchKey: MutableLiveData<CharSequence?> = MutableLiveData()

    fun onSearchButtonClick(view: View) {
        Coroutines.main {
            if (eventSearchKey.value.toString().isNotEmpty() ||
                eventSearchKey.value.toString().isNotBlank()
            ) {
                eventsFiltered.postValue(
                    repository.findFilterEvents(
                        EventFilterRequest(
                            nameContains = eventSearchKey.value.toString()
                        )
                    ).body()
                )
            } else {
                eventsFiltered.postValue(null)
            }
        }
    }
}