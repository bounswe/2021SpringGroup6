package com.example.sportsplatform.viewmodelfactories

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.viewmodels.SearchViewModel

class SearchViewModelFactory(
    private val repository: EventRepository
): ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return SearchViewModel(repository) as T
    }
}