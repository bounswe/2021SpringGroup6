package com.example.sportsplatform.viewmodelfactories

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.data.repository.SportRepository
import com.example.sportsplatform.viewmodels.SearchViewModel

class SearchViewModelFactory(
    private val sportRepository: SportRepository
) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return SearchViewModel(sportRepository) as T
    }
}