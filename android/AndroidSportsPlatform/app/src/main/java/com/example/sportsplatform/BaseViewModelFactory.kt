package com.example.sportsplatform

import android.content.SharedPreferences
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.BaseRepository
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.viewmodels.AuthViewModel
import com.example.sportsplatform.viewmodels.EventSearchViewModel
import com.example.sportsplatform.viewmodels.HomeViewModel
import java.lang.IllegalArgumentException

@Suppress("Unchecked_Cast")
class BaseViewModelFactory(
    private val repo: BaseRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return when{
            modelClass.isAssignableFrom(AuthViewModel::class.java) -> AuthViewModel(repo as UserRepository, sharedPreferences) as T
            modelClass.isAssignableFrom(HomeViewModel::class.java) -> HomeViewModel(repo as UserRepository, sharedPreferences) as T
            modelClass.isAssignableFrom(EventSearchViewModel::class.java) -> EventSearchViewModel(repo as EventRepository) as T
            else -> throw IllegalArgumentException("ViewModel Not Found")
        }
    }

}