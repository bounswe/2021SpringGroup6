package com.example.sportsplatform.viewmodels

import android.content.SharedPreferences
import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.R
import com.example.sportsplatform.data.repository.SportRepository
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.fromJson
import com.google.android.gms.maps.model.LatLng
import com.example.sportsplatform.data.models.responses.UserSearchResponse
import com.google.gson.Gson

class SearchViewModel(
    private val sportRepository: SportRepository
) : ViewModel() {

    val eventSearchKey: MutableLiveData<CharSequence?> = MutableLiveData("")

    val usersFiltered: MutableLiveData<UserSearchResponse?> = MutableLiveData()
    val userSearchKey: MutableLiveData<CharSequence?> = MutableLiveData("")

    var searchBarHint: MutableLiveData<String> = MutableLiveData()
    var searchOption: MutableLiveData<Int> = MutableLiveData(0)
    var searchEventWithMapVisibility: MutableLiveData<Int> = MutableLiveData()
    var custSharedPreferences: SharedPreferences? = null
    var listOfEventSearchCoordinates: Array<LatLng>? = null
    var coordinatesAsString: String = ""
    var sports: MutableLiveData<Array<String>> = MutableLiveData()

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

    fun getSports() {
        Coroutines.main {
            val sportsNames = sportRepository.getSports().body()
            var sportsNamesList = arrayOf<String>()
            sportsNames?.map { it.name?.let { name -> sportsNamesList += name } }
            sports.postValue(sportsNamesList)
        }
    }

    fun setCustomSharedPreferences(customSharedPrefers: SharedPreferences) {
        custSharedPreferences = customSharedPrefers
    }

    fun getEventSearchCoordinatesFromSharedPreferences() {
        val serializedObject =
            custSharedPreferences?.getString("listOfMarkerPositions", null)
        listOfEventSearchCoordinates = serializedObject?.let {
            Gson().fromJson<Array<LatLng>>(it)
        }

        getCoorinatesAsString()
    }

    private fun getCoorinatesAsString() {
        listOfEventSearchCoordinates?.toMutableList()?.map {
            coordinatesAsString += " ${it.latitude.toString().take(9)} / ${
                it.longitude.toString().take(9)
            } "
        }
    }

    fun clearCoordinates() {
        custSharedPreferences?.edit()?.putString("listOfMarkerPositions", null)?.apply()
        coordinatesAsString = ""
    }
}