package com.example.sportsplatform.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.databinding.FragmentEventDetailBinding
import com.example.sportsplatform.viewmodelfactories.EventDetailViewModelFactory
import com.example.sportsplatform.viewmodels.EventDetailViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class EventDetailFragment : Fragment(), KodeinAware {

    private var _binding: FragmentEventDetailBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: EventDetailViewModel
    private val factory: EventDetailViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentEventDetailBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(EventDetailViewModel::class.java)
        viewModel.getEventInformation(arguments?.getInt(EVENT_ID) ?: 0)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.event.observe(
            viewLifecycleOwner,
            Observer {
                val event = it
            }
        )
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