package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.responses.Badge
import com.example.sportsplatform.data.repository.BadgeRepository
import com.example.sportsplatform.util.Coroutines

class AddEventBadgeViewModel(
    private val badgeRepository: BadgeRepository
) : ViewModel() {

    var badges: MutableLiveData<List<Badge?>> = MutableLiveData()

    fun getBadges() {
        Coroutines.main {
            badges.postValue(badgeRepository.getBadges().body()?.badges)
        }
    }
}