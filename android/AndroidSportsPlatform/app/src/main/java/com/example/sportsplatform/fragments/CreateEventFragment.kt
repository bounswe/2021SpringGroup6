package com.example.sportsplatform.fragments

import android.content.Context.MODE_PRIVATE
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.activities.MainActivity
import com.example.sportsplatform.activities.MapsActivity
import com.example.sportsplatform.data.models.requests.CreateEventRequest
import com.example.sportsplatform.databinding.FragmentCreateEventBinding
import com.example.sportsplatform.util.Constants.CUSTOM_SHARED_PREFERENCES
import com.example.sportsplatform.util.convertDateFormatToDefault
import com.example.sportsplatform.viewmodels.CreateEventViewModel
import com.example.sportsplatform.viewmodels.CreateEventViewModelFactory
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class CreateEventFragment : Fragment(), KodeinAware {

    private var _binding: FragmentCreateEventBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: CreateEventViewModel
    private val factory: CreateEventViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCreateEventBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(CreateEventViewModel::class.java)
        viewModel.setCustomSharedPreferences(
            requireActivity().getSharedPreferences(
                CUSTOM_SHARED_PREFERENCES,
                MODE_PRIVATE
            )
        )
        return binding.root
    }

    override fun onResume() {
        super.onResume()
        binding.createEventViewModel = viewModel
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding.twCreateEventLocationCoordinates.setOnClickListener {
            MapsActivity.openMaps(activity as MainActivity)
        }
        binding.btnCreateEvent.setOnClickListener {
            viewModel.createNewEvent(
                CreateEventRequest(
                    binding.etCreateEventName.text.toString(),
                    binding.etCreateEventSport.text.toString(),
                    binding.etCreateEventDescription.text.toString(),
                    binding.etCreateEventStartDate.text.toString().convertDateFormatToDefault(),
                    viewModel.eventLatitude.value?.take(6)?.toDouble() ?: 0.0,
                    viewModel.eventLongitude.value?.take(6)?.toDouble() ?: 0.0,
                    binding.etCreateEventMaxAttendeeCap.text.toString().toInt(),
                    binding.etCreateEventMinAttendeeCap.text.toString().toInt(),
                    binding.etCreateEventMaxSpectatorCap.text.toString().toInt(),
                    binding.etCreateEventMinSkillLevel.text.toString().toInt(),
                    binding.etCreateEventMaxSkillLevel.text.toString().toInt(),
                    binding.etCreateEventAcceptWithoutApproval.text.toString().toBoolean(),
                    binding.etCreateEventDuration.text.toString().toInt()
                )
            )
        }
    }
}