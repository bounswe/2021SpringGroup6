package com.example.sportsplatform.fragments

import android.content.DialogInterface
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.adapter.EventBadgesAdapter
import com.example.sportsplatform.adapter.UsersAdapter
import com.example.sportsplatform.databinding.FragmentEventDetailBinding
import com.example.sportsplatform.util.DialogDismissListener
import com.example.sportsplatform.viewmodelfactories.EventDetailViewModelFactory
import com.example.sportsplatform.viewmodels.EventDetailViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class EventDetailFragment : Fragment(), KodeinAware, DialogDismissListener {

    private var _binding: FragmentEventDetailBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: EventDetailViewModel
    private val factory: EventDetailViewModelFactory by instance()

    private val attendeeAdapter by lazy { UsersAdapter() }
    private val audienceAdapter by lazy { UsersAdapter() }
    private val badgesAdapter by lazy { EventBadgesAdapter() }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentEventDetailBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(EventDetailViewModel::class.java)
        viewModel.eventId.postValue(arguments?.getInt(EVENT_ID) ?: 0)

        initializeRecyclerviews()

        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.eventId.observe(
            viewLifecycleOwner,
            Observer {
                viewModel.getEventInformation(it)
                viewModel.getEventBadges()
            }
        )

        viewModel.event.observe(
            viewLifecycleOwner,
            Observer {
                attendeeAdapter.items = it?.attendee?.toMutableList() ?: mutableListOf()
                audienceAdapter.items = it?.audience?.toMutableList() ?: mutableListOf()
                binding.eventDetailViewModel = viewModel
            }
        )

        viewModel.interestSent.observe(
            viewLifecycleOwner,
            Observer {
                viewModel.eventId.value?.let { id -> viewModel.getEventInformation(id) }
            }
        )

        viewModel.eventBadges.observe(
            viewLifecycleOwner,
            Observer {
                badgesAdapter.items =
                    it?.additionalProperty?.value?.toMutableList() ?: mutableListOf()
            }
        )

        binding.showInteresteds.setOnClickListener {
            ShowInterestedsDialogFragment.newInstance(
                requireActivity().supportFragmentManager,
                this,
                arguments?.getInt(EVENT_ID) ?: 0
            )
        }
    }

    private fun initializeRecyclerviews() {
        binding.rvAttendee.apply {
            layoutManager = LinearLayoutManager(context, LinearLayoutManager.HORIZONTAL, false)
            adapter = attendeeAdapter
        }

        binding.rvAudience.apply {
            layoutManager = LinearLayoutManager(context, LinearLayoutManager.HORIZONTAL, false)
            adapter = audienceAdapter
        }

        binding.rvBadges.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = badgesAdapter
        }
    }

    override fun onDismiss(dialog: DialogInterface) {
        viewModel.eventId.postValue(arguments?.getInt(EVENT_ID) ?: 0)
    }

    companion object {
        private const val EVENT_ID = "event_id"
        fun newInstance(eventId: Int?) = EventDetailFragment().apply {
            arguments = Bundle().apply {
                eventId?.let { putInt(EVENT_ID, it) }
            }
        }
    }
}