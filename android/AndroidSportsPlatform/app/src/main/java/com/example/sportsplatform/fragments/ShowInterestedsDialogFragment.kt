package com.example.sportsplatform.fragments

import android.content.DialogInterface
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.DialogFragment
import androidx.fragment.app.FragmentManager
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.adapter.InterestedsDecisionClick
import com.example.sportsplatform.adapter.InterestedsOfEventAdapter
import com.example.sportsplatform.data.models.responses.Value
import com.example.sportsplatform.databinding.FragmentShowInterestedsBinding
import com.example.sportsplatform.util.DialogDismissListener
import com.example.sportsplatform.util.toast
import com.example.sportsplatform.viewmodelfactories.ShowInterestedsViewModelFactory
import com.example.sportsplatform.viewmodels.ShowInterestedsViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class ShowInterestedsDialogFragment(
    private val dialogDismissListener: DialogDismissListener?
) : DialogFragment(), KodeinAware, InterestedsDecisionClick {

    private var _binding: FragmentShowInterestedsBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: ShowInterestedsViewModel
    private val factory: ShowInterestedsViewModelFactory by instance()

    private val interestedsAdapter by lazy { InterestedsOfEventAdapter(this) }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentShowInterestedsBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(ShowInterestedsViewModel::class.java)

        initializeRecyclerview()
        getBundleArguments()

        viewModel.getInterestedsOfEvent()

        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.interestedsOfEvent.observe(
            viewLifecycleOwner,
            Observer {
                interestedsAdapter.items =
                    it?.additionalProperty?.value?.toMutableList() ?: mutableListOf()
            }
        )

        viewModel.decideParticipantsSuccessful.observe(
            viewLifecycleOwner,
            Observer {
                requireContext().toast(if (it) "User Accepted!" else "User Declined!")
            }
        )

        viewModel.acceptedUsersList.observe(
            viewLifecycleOwner,
            Observer {
                viewModel.decideParticipants(true)
            }
        )

        viewModel.declinedUsersList.observe(
            viewLifecycleOwner,
            Observer {
                viewModel.decideParticipants(false)
            }
        )

        binding.btnDone.setOnClickListener {
            dismiss()
        }
    }

    override fun onDismiss(dialog: DialogInterface) {
        super.onDismiss(dialog)
        dialogDismissListener?.onDismiss(dialog)
    }

    private fun getBundleArguments() {
        arguments?.let {
            viewModel.eventId = it.getInt(EVENT_ID)
        }
    }

    private fun initializeRecyclerview() {
        binding.rvInteresteds.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = interestedsAdapter
        }
    }

    override fun onAcceptClick(user: Value?) {
        viewModel.acceptedUsersList.postValue(mutableListOf(user?.id))
    }

    override fun onDeclineClick(user: Value?) {
        viewModel.declinedUsersList.postValue(mutableListOf(user?.id))
    }

    companion object {
        private const val EVENT_ID = "event_id"
        fun newInstance(
            supportFragmentManager: FragmentManager,
            dismissListener: DialogDismissListener,
            eventId: Int
        ) {
            ShowInterestedsDialogFragment(dismissListener).apply {
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