package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.R
import com.google.android.gms.maps.model.LatLng
import com.example.sportsplatform.data.models.responses.UserSearchResponse

class SearchViewModel : ViewModel() {

    val eventSearchKey: MutableLiveData<CharSequence?> = MutableLiveData()

    val usersFiltered: MutableLiveData<UserSearchResponse?> = MutableLiveData()
    val userSearchKey: MutableLiveData<CharSequence?> = MutableLiveData()

    var searchBarHint: MutableLiveData<String> = MutableLiveData()
    var searchOption: MutableLiveData<Int> = MutableLiveData(0)
    var searchEventWithMapVisibility: MutableLiveData<Int> = MutableLiveData()
    var custSharedPreferences: SharedPreferences? = null
    var listOfEventSearchCoordinates: Array<LatLng>? = null

    fun setSearchOption(view: View?, position: Int?) {
        searchBarHint.postValue(
            when (position) {
                0 -> view?.context?.getString(R.string.searchUser)
                1 -> view?.context?.getString(R.string.searchEvent)
                2 -> view?.context?.getString(R.string.searchEquipment)
                else -> ""
            }
        )
        searchEventWithMapVisibility.postValue(if (position == 1) View.VISIBLE else View.GONE)
    }

    fun setCustomSharedPreferences(customSharedPrefers: SharedPreferences) {
        custSharedPreferences = customSharedPrefers
    }
}