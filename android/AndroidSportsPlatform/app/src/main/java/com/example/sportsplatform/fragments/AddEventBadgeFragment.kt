package com.example.sportsplatform.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.adapter.EventBadgesAdapter
import com.example.sportsplatform.adapter.EventBadgesClickListener
import com.example.sportsplatform.data.models.responses.ValueForEventBadges
import com.example.sportsplatform.databinding.FragmentAddEventBadgeBinding
import com.example.sportsplatform.viewmodelfactories.AddEventBadgeViewModelFactory
import com.example.sportsplatform.viewmodels.AddEventBadgeViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class AddEventBadgeFragment : Fragment(), KodeinAware, EventBadgesClickListener {
    private var _binding: FragmentAddEventBadgeBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: AddEventBadgeViewModel
    private val factory: AddEventBadgeViewModelFactory by instance()

    private val badgesAdapter by lazy { EventBadgesAdapter() }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentAddEventBadgeBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(AddEventBadgeViewModel::class.java)
        initializeRecyclerview()
        viewModel.getBadges()
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.badges.observe(
            viewLifecycleOwner,
            Observer {
                badgesAdapter.items = it
            }
        )
    }

    private fun initializeRecyclerview() {
        binding.rvBadges.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = badgesAdapter
        }
    }

    override fun onEventBadgesClicked(badgeResponse: ValueForEventBadges?) {

    }
}