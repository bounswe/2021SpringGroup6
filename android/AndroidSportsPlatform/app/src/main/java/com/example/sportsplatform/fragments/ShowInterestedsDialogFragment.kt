package com.example.sportsplatform.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.DialogFragment
import androidx.fragment.app.FragmentManager
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.databinding.FragmentShowInterestedsBinding
import com.example.sportsplatform.viewmodelfactories.ShowInterestedsViewModelFactory
import com.example.sportsplatform.viewmodels.ShowInterestedsViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class ShowInterestedsDialogFragment : DialogFragment(), KodeinAware {

    private var _binding: FragmentShowInterestedsBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: ShowInterestedsViewModel
    private val factory: ShowInterestedsViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentShowInterestedsBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(ShowInterestedsViewModel::class.java)

        getBundleArguments()

        viewModel.getInterestedsOfEvent()

        return binding.root
    }

    private fun getBundleArguments() {
        arguments?.let {
            viewModel.eventId = it.getInt(EVENT_ID)
        }
    }

    companion object {
        private const val EVENT_ID = "event_id"
        fun newInstance(supportFragmentManager: FragmentManager, eventId: Int) {
            ShowInterestedsDialogFragment().apply {
                arguments = Bundle().apply {
                    putInt(EVENT_ID, eventId)
                }
                this.show(
                    supportFragmentManager,
                    ShowInterestedsDialogFragment::class.java.simpleName
                )
            }
        }
    }
}