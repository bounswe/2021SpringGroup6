package com.example.sportsplatform.viewmodels

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.repository.UserRepository

class ProfileViewModelFactory(
    private val userRepository: UserRepository,
    private val eventRepository: EventRepository
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return ProfileViewModel(userRepository, eventRepository) as T
    }
}