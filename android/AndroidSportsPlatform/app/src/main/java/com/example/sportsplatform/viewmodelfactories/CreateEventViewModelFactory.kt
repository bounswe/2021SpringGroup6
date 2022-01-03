package com.example.sportsplatform.viewmodelfactories

import android.content.SharedPreferences
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.viewmodels.CreateEventViewModel

class CreateEventViewModelFactory(
    private val eventRepository: EventRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return CreateEventViewModel(eventRepository, sharedPreferences) as T
    }
}