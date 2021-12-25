package com.example.sportsplatform.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.adapter.UsersParticipatingEventsAdapter
import com.example.sportsplatform.databinding.FragmentHomeBinding
import com.example.sportsplatform.viewmodels.HomeViewModel
import com.example.sportsplatform.viewmodels.HomeViewModelFactory
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class HomeFragment : Fragment(), KodeinAware {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: HomeViewModel
    private val factory : HomeViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(HomeViewModel::class.java)
        viewModel.fetchUsersParticipatingEvents()

        initializeRecyclerview()

        return binding.root
    }

    private fun initializeRecyclerview() {
        viewModel.usersParticipatingEvents.observe(
            viewLifecycleOwner,
            Observer {
                binding.rvEventsAttending.apply {
                    layoutManager = LinearLayoutManager(context)
                    adapter = UsersParticipatingEventsAdapter(it.items)
                }
            }
        )
    }
}