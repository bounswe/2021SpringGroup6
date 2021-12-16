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

    val eventLiveData = MutableLiveData<EventFilterResponse>()
    var event: String? = null

    fun onSearchImageButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            if(!event.isNullOrEmpty()){
                val eventFilterRequest = EventFilterRequest (event!!)
                view.context.toast(eventFilterRequest.toString())
                val currResponse = eventRepo.findFilterEvents(eventFilterRequest)
                view.context.toast(currResponse.toString())
                if (currResponse.isSuccessful) {
                    view.context.toast(currResponse.toString())
                    Intent(view.context, EventListActivity::class.java).also{
                        view.context.startActivity(it)
                    }
                }
                else {
                    view.context.toast("Fail")
                }
            }
        }
    }
}