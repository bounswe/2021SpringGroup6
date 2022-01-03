package com.example.sportsplatform.viewmodels

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.models.responses.ValueForEventBadges
import com.example.sportsplatform.data.repository.BadgeRepository
import com.example.sportsplatform.util.Coroutines

class AddEventBadgeViewModel(
    private val badgeRepository: BadgeRepository
) : ViewModel() {

    var badges: MutableLiveData<MutableList<ValueForEventBadges?>> = MutableLiveData()

    fun getBadges() {
        Coroutines.main {
            val allBadges = badgeRepository.getBadges().body()?.badges
            badges.postValue(allBadges?.map { it.toValueBadge() }?.toMutableList())
        }
    }
}