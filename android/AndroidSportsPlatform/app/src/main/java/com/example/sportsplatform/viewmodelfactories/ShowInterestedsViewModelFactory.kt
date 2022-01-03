package com.example.sportsplatform.viewmodelfactories

import android.content.SharedPreferences
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.viewmodels.ShowInterestedsViewModel

class ShowInterestedsViewModelFactory(
    private val eventRepository: EventRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return ShowInterestedsViewModel(eventRepository, sharedPreferences) as T
    }
}