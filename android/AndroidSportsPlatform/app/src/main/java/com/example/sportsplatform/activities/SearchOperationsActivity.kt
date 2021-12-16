package com.example.sportsplatform.activities

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.R
import com.example.sportsplatform.databinding.ActivitySearchOperationsBinding
import com.example.sportsplatform.viewmodels.EventSearchViewModel
import com.example.sportsplatform.viewmodels.EventSearchViewModelFactory
import com.example.sportsplatform.viewmodels.ProfileViewModel
import com.example.sportsplatform.viewmodels.ProfileViewModelFactory
import org.kodein.di.KodeinAware
import org.kodein.di.android.kodein
import org.kodein.di.generic.instance

class SearchOperationsActivity : AppCompatActivity(), KodeinAware {

    private lateinit var searchOperationsViewModel: EventSearchViewModel
    override val kodein by kodein()
    private val factory : EventSearchViewModelFactory by instance()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding: ActivitySearchOperationsBinding = DataBindingUtil.setContentView(
                this, R.layout.activity_search_operations)
        val view = binding.root
        setContentView(view)

        searchOperationsViewModel = ViewModelProvider(this, factory).get(EventSearchViewModel::class.java)
        binding.searchoperation = searchOperationsViewModel

    }
}