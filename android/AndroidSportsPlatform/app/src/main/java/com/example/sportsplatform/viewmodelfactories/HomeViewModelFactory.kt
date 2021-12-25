package com.example.sportsplatform.viewmodelfactories

import android.content.SharedPreferences
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.viewmodels.HomeViewModel

class HomeViewModelFactory(
    private val userRepository: UserRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return HomeViewModel(userRepository, sharedPreferences) as T
    }
}