package com.example.sportsplatform

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider

class PlatformViewModelFactory : ViewModelProvider.NewInstanceFactory() {
    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return PlatformViewModel() as T
    }
}