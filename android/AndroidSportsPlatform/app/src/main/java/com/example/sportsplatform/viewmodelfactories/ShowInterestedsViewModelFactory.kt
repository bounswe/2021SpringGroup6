package com.example.sportsplatform.viewmodelfactories

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.viewmodels.ShowInterestedsViewModel

class ShowInterestedsViewModelFactory : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return ShowInterestedsViewModel() as T
    }
}