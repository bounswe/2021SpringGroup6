package com.example.sportsplatform.viewmodelfactories

import android.content.SharedPreferences
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.BadgeRepository
import com.example.sportsplatform.viewmodels.AddEventBadgeViewModel

class AddEventBadgeViewModelFactory(
    private val badgeRepository: BadgeRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return AddEventBadgeViewModel(badgeRepository, sharedPreferences) as T
    }
}