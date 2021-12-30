package com.example.sportsplatform.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.R
import com.example.sportsplatform.adapter.EventsListAdapter
import com.example.sportsplatform.adapter.EventsClickListener
import com.example.sportsplatform.data.models.responses.EventResponse
import com.example.sportsplatform.databinding.FragmentSearchEventBinding
import com.example.sportsplatform.viewmodelfactories.EventSearchViewModelFactory
import com.example.sportsplatform.viewmodels.EventSearchViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class EventSearchFragment : Fragment(), KodeinAware, EventsClickListener {
    private var _binding: FragmentSearchEventBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: EventSearchViewModel
    private val factory: EventSearchViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSearchEventBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(EventSearchViewModel::class.java)
        viewModel.fillSearchEventList(arguments?.getString("event_search_filter"))
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.eventsFiltered.observe(
            viewLifecycleOwner,
            Observer {
                binding.rvEventsFiltered.apply {
                    layoutManager =
                        LinearLayoutManager(context)
                    adapter =
                        it?.items?.let { filteredEventItems ->
                            EventsListAdapter(
                                filteredEventItems,
                                this@EventSearchFragment
                            )
                        }
                }
            }
        )
    }

    override fun onEventsClickListener(eventResponse: EventResponse?) {
        val transaction = requireActivity().supportFragmentManager.beginTransaction()
        val fragmentToGo = EventDetailFragment.newInstance(eventId = eventResponse?.event_id)
        transaction.replace(R.id.mainContainer, fragmentToGo)
        transaction.addToBackStack(null)
        transaction.commit()
    }
}