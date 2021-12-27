package com.example.sportsplatform.viewmodelfactories

import android.content.SharedPreferences
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.viewmodels.AuthViewModel

class AuthViewModelFactory(
    private val repository: UserRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return AuthViewModel(repository, sharedPreferences) as T
    }
}