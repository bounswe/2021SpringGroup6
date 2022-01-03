package com.example.sportsplatform.viewmodelfactories

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.BadgeRepository
import com.example.sportsplatform.viewmodels.AddEventBadgeViewModel

class AddEventBadgeViewModelFactory(
    private val badgeRepository: BadgeRepository
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return AddEventBadgeViewModel(badgeRepository) as T
    }
}