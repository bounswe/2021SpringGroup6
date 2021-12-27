package com.example.sportsplatform.viewmodels

import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.responses.EventFilterResponse

class SearchViewModel : ViewModel() {

    val eventsFiltered: MutableLiveData<EventFilterResponse?> = MutableLiveData()
    val eventSearchKey: MutableLiveData<CharSequence?> = MutableLiveData()
    var searchBarHint: MutableLiveData<String> = MutableLiveData()
    var searchOption: MutableLiveData<Int> = MutableLiveData(0)

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