package com.example.sportsplatform.viewmodels

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.EventRepository
import com.example.sportsplatform.data.UserRepository

class EventSearchViewModelFactory(
    private val repository: EventRepository
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return EventSearchViewModel(repository) as T
    }
}