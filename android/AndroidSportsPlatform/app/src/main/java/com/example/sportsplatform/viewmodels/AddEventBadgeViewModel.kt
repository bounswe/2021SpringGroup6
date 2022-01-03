package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.content.SharedPreferences
import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.activities.MainActivity
import com.example.sportsplatform.data.models.requests.AddBadgeToEventRequest
import com.example.sportsplatform.data.models.responses.ValueForEventBadges
import com.example.sportsplatform.data.repository.BadgeRepository
import com.example.sportsplatform.util.Constants.SHARED_PREFS_USER_TOKEN
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.closeSoftKeyboard

class AddEventBadgeViewModel(
    private val badgeRepository: BadgeRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {

    var badges: MutableLiveData<MutableList<ValueForEventBadges?>> = MutableLiveData()
    var eventId: MutableLiveData<Int?> = MutableLiveData()
    var eventSport: MutableLiveData<String?> = MutableLiveData()
    var addBadgeMessage: MutableLiveData<String> = MutableLiveData()

    fun getBadges() {
        Coroutines.main {
            val allBadges =
                if (eventSport.value == "basketball" || eventSport.value == "soccer") badgeRepository.getSportBadges(
                    eventSport.value
                ).body()?.badges else badgeRepository.getBadges().body()?.badges
            badges.postValue(allBadges?.map { it.toValueBadge() }?.toMutableList())
        }
    }

    fun addBadgeToEvent(
        eventId: Int?,
        badgeName: String?
    ) {
        Coroutines.main {
            val response = badgeRepository.addBadgeToEvent(
                "Token " + sharedPreferences.getString(SHARED_PREFS_USER_TOKEN, ""),
                eventId,
                AddBadgeToEventRequest(
                    badgeName
                )
            )

            addBadgeMessage.postValue(response.message())
        }
    }

    fun onDoneButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, MainActivity::class.java).also {
                view.context.startActivity(it)
            }
        }
    }
}