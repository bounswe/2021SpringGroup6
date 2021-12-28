package com.example.sportsplatform.fragments

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.activities.LoginActivity
import com.example.sportsplatform.adapter.UsersParticipatingEventsAdapter
import com.example.sportsplatform.databinding.FragmentHomeBinding
import com.example.sportsplatform.util.toast
import com.example.sportsplatform.viewmodels.HomeViewModel
import com.example.sportsplatform.viewmodelfactories.HomeViewModelFactory
import kotlinx.coroutines.launch
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance
import com.example.sportsplatform.R

class HomeFragment : Fragment(), KodeinAware {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: HomeViewModel
    private val factory: HomeViewModelFactory by instance()

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

        binding.btnLogout.setOnClickListener {
            view?.context?.toast("Logout Button Pressed!")
            logOut()
            startActivity(Intent(activity, LoginActivity::class.java))
        }

        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.btnCreateNewEvent.setOnClickListener {
            val fragmentToGo = CreateEventFragment()
            val transaction = requireActivity().supportFragmentManager.beginTransaction()
            transaction.replace(R.id.mainContainer, fragmentToGo)
            transaction.addToBackStack(null)
            transaction.commit()
        }
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

    private fun logOut() = lifecycleScope.launch {
        viewModel.userLoggingOut()
    }
}