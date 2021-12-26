package com.example.sportsplatform.fragments

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ArrayAdapter
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.EventAdapter
import com.example.sportsplatform.R
import com.example.sportsplatform.databinding.FragmentSearchBinding
import com.example.sportsplatform.viewmodels.SearchViewModel
import com.example.sportsplatform.viewmodels.SearchViewModelFactory
import kotlinx.android.synthetic.main.fragment_search.view.*
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class SearchFragment : Fragment(), KodeinAware, AdapterView.OnItemSelectedListener {

    private var _binding: FragmentSearchBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: SearchViewModel
    private val factory: SearchViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSearchBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(SearchViewModel::class.java)
        initializeSpinner()
        binding.searchViewModel = viewModel
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        view.searchBar?.addTextChangedListener(object : TextWatcher {

            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
            }

            override fun afterTextChanged(s: Editable?) {
            }

            override fun onTextChanged(s: CharSequence, start: Int, before: Int, count: Int) {
                viewModel.eventSearchKey.postValue(s)
            }
        })

        viewModel.eventsFiltered.observe(
            viewLifecycleOwner,
            Observer {
                binding.rvEventsFiltered.apply {
                    layoutManager =
                        LinearLayoutManager(context)
                    adapter =
                        it?.items?.let { filteredEventItems -> EventAdapter(filteredEventItems) }
                }
            }
        )

        viewModel.searchOption.observe(
            viewLifecycleOwner,
            Observer {
                viewModel.setSearchOption(binding.spinner, it)
            }
        )

        viewModel.searchBarHint.observe(
            viewLifecycleOwner,
            Observer {
                binding.searchViewModel = viewModel
            }
        )
    }

    private fun initializeSpinner() {
        ArrayAdapter.createFromResource(
            requireContext(),
            R.array.searchOptions,
            R.layout.item_spinner
        ).also { adapter ->
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
            binding.spinner.adapter = adapter
        }
        binding.spinner.onItemSelectedListener = this
    }

    override fun onItemSelected(p0: AdapterView<*>?, p1: View?, position: Int, p3: Long) {
        viewModel.searchOption.postValue(position)
    }

    override fun onNothingSelected(position: AdapterView<*>?) {}
}