package com.example.sportsplatform.viewmodels

import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.util.Coroutines

class SearchViewModel(
    private val repository: EventRepository
) : ViewModel() {

    val eventsFiltered: MutableLiveData<EventFilterResponse?> = MutableLiveData()
    val eventSearchKey: MutableLiveData<CharSequence?> = MutableLiveData()
    var searchBarHint: MutableLiveData<String> = MutableLiveData()
    var searchOption: MutableLiveData<Int> = MutableLiveData(0)

    fun onSearchButtonClick(view: View) {
        Coroutines.main {
            if (eventSearchKey.value.toString().isNotEmpty() ||
                eventSearchKey.value.toString().isNotBlank()
            ) {
                when (searchOption.value) {
                    0 -> {}

                    1 -> {
                        eventsFiltered.postValue(
                            repository.findFilterEvents(
                                EventFilterRequest(
                                    nameContains = eventSearchKey.value.toString()
                                )
                            ).body()
                        )
                    }

                    2 -> {}
                }
            } else {
                eventsFiltered.postValue(null)
            }
        }
    }

    fun setSearchOption(view: View?, position: Int?) {
        searchBarHint.postValue(
            when (position) {
                0 -> view?.context?.getString(R.string.searchUser)
                1 -> view?.context?.getString(R.string.searchEvent)
                2 -> view?.context?.getString(R.string.searchEquipment)
                else -> ""
            }
        )
    }
}