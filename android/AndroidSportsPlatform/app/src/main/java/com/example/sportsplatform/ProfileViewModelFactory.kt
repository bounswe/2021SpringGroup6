package com.example.sportsplatform

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.Repository

class ProfileViewModelFactory(
        private val repository: Repository
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return ProfileViewModel(repository) as T
    }
}