package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.fromJson
import com.google.android.gms.maps.model.LatLng
import com.google.gson.Gson

class EventSearchViewModel(private val eventRepo: EventRepository) : ViewModel() {

    var eventSearchKey: String? = null
    var eventSearchCoordinates: Array<LatLng>? = null

    val eventsFiltered: MutableLiveData<EventFilterResponse?> = MutableLiveData()

    fun setArguments(searchKey: String?, coordinates: String?) {
        eventSearchKey = searchKey
        eventSearchCoordinates = coordinates?.let { Gson().fromJson<Array<LatLng>>(it) }
    }

    fun fillSearchEventList() {
        Coroutines.main {
            eventSearchKey?.let {
                val eventFilterRequest = if (it.isNotEmpty()) {
                    EventFilterRequest(nameContains = it)
                } else {
                    EventFilterRequest(
                        latitudeBetweenEnd = eventSearchCoordinates?.get(0)?.latitude?.toString()
                            ?.take(9)?.toDouble(),
                        latitudeBetweenStart = eventSearchCoordinates?.get(1)?.latitude?.toString()
                            ?.take(9)?.toDouble(),
                        longitudeBetweenEnd = eventSearchCoordinates?.get(0)?.longitude?.toString()
                            ?.take(9)?.toDouble(),
                        longitudeBetweenStart = eventSearchCoordinates?.get(1)?.longitude?.toString()
                            ?.take(9)?.toDouble()
                    )
                }
                eventsFiltered.postValue(
                    eventRepo.findFilterEvents(
                        eventFilterRequest
                    ).body()
                )
            }
        }
    }
}