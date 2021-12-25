package com.example.sportsplatform.viewmodelfactories

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.viewmodels.RegisterViewModel


class RegisterViewModelFactory(
    private val userRepo: UserRepository
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return RegisterViewModel(userRepo) as T
    }
}