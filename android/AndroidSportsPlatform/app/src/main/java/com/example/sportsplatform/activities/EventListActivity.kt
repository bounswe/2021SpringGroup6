package com.example.sportsplatform.activities

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.EventAdapter
import com.example.sportsplatform.R
import com.example.sportsplatform.databinding.ActivityEventListBinding
import com.example.sportsplatform.databinding.ActivityEventListBinding.*
import com.example.sportsplatform.databinding.ActivityMainBinding
import com.example.sportsplatform.viewmodels.EventSearchViewModel
import com.example.sportsplatform.viewmodels.EventSearchViewModelFactory
import kotlinx.android.synthetic.main.activity_event_list.*
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.android.kodein
import org.kodein.di.generic.instance

class EventListActivity : AppCompatActivity(), KodeinAware {
    private lateinit var eventSearchViewModel: EventSearchViewModel
    override val kodein by kodein()
    private val factory : EventSearchViewModelFactory by instance()


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding = inflate(layoutInflater)
        val view = binding.root
        setContentView(view)

        eventSearchViewModel = ViewModelProvider(this, factory).get(EventSearchViewModel::class.java)
        binding.eventviewmodel = eventSearchViewModel

        initObservers()
    }

    private fun initObservers(){
        eventSearchViewModel.eventLiveData.observe(this, Observer {
            event_recycler_view.apply {
                layoutManager = LinearLayoutManager(context, LinearLayoutManager.HORIZONTAL, false)
                adapter = EventAdapter(it.items)
            }
        })
    }
}