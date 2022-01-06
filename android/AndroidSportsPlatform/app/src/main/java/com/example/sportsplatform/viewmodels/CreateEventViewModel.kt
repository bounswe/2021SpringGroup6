package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.requests.CreateEventRequest
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.repository.SportRepository
import com.example.sportsplatform.util.Constants.EVENT_LATITUDE
import com.example.sportsplatform.util.Constants.EVENT_LONGITUDE
import com.example.sportsplatform.util.Constants.SHARED_PREFS_USER_TOKEN
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.toast

class CreateEventViewModel(
    private val eventRepository: EventRepository,
    private val sportRepository: SportRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {

    private var customSharedPreferences: SharedPreferences? = null
    var eventLatitude: MutableLiveData<String> = MutableLiveData()
    var eventLongitude: MutableLiveData<String> = MutableLiveData()
    var sports: MutableLiveData<Array<String>> = MutableLiveData()
    var eventCreatedSuccessful: MutableLiveData<Pair<Int, String>> = MutableLiveData()

    fun setCustomSharedPreferences(customSharedPrefers: SharedPreferences) {
        customSharedPreferences = customSharedPrefers
    }

    fun getEventCoordinates(): String? {
        eventLatitude.postValue(customSharedPreferences?.getString(EVENT_LATITUDE, ""))
        eventLongitude.postValue(customSharedPreferences?.getString(EVENT_LONGITUDE, ""))
        val latitude = eventLatitude.value?.take(5) ?: ""
        val longitude = eventLongitude.value?.take(5) ?: ""
        var coordinates: String? = null
        if (latitude.isNotEmpty() || longitude.isNotEmpty()) {
            coordinates = "$latitude $longitude"
        }
        return coordinates
    }

    fun getSports() {
        Coroutines.main {
            val sportsNames = sportRepository.getSports().body()
            var sportsNamesList = arrayOf<String>()
            sportsNames?.map { it.name?.let { name -> sportsNamesList += name } }
            sports.postValue(sportsNamesList)
        }
    }

    fun createNewEvent(
        view: View,
        createEventRequest: CreateEventRequest
    ) {
        Coroutines.main {
            val token = sharedPreferences.getString(SHARED_PREFS_USER_TOKEN, "")
            val createEventResponse = eventRepository.createNewEvent(
                "Token $token",
                createEventRequest
            )
            if (createEventResponse.isSuccessful) {
                view.context.toast("Event created!")
                eventCreatedSuccessful.postValue(
                    Pair(
                        createEventResponse.body()?.id ?: 0,
                        createEventRequest.sport
                    )
                )
            } else {
                view.context.toast(createEventResponse.raw().message())
            }


        }
    }
}