package com.example.sportsplatform.fragments

import android.content.ContentValues.TAG
import android.content.Context
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.AdapterView
import android.widget.ArrayAdapter
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.R
import com.example.sportsplatform.activities.MainActivity
import com.example.sportsplatform.activities.MapsActivity
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.requests.UserSearchRequest
import com.example.sportsplatform.databinding.FragmentSearchBinding
import com.example.sportsplatform.util.Constants
import com.example.sportsplatform.viewmodels.SearchViewModel
import com.example.sportsplatform.viewmodelfactories.SearchViewModelFactory
import kotlinx.android.synthetic.main.item_searched_user_layout.*
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

        viewModel.getSports()
        viewModel.setCustomSharedPreferences(
            requireActivity().getSharedPreferences(
                Constants.CUSTOM_SHARED_PREFERENCES,
                Context.MODE_PRIVATE
            )
        )
        viewModel.clearCoordinates()

        initializeSpinner()

        initializeSpinnersForLevels()

        binding.searchViewModel = viewModel

        return binding.root
    }

    override fun onResume() {
        super.onResume()
        viewModel.getEventSearchCoordinatesFromSharedPreferences()
        binding.twSearchEventWithMap.text = viewModel.coordinatesAsString
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding.searchBar.addTextChangedListener(object : TextWatcher {

            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {
            }

            override fun afterTextChanged(s: Editable?) {
            }

            override fun onTextChanged(s: CharSequence, start: Int, before: Int, count: Int) {
                viewModel.eventSearchKey.postValue(s)
                viewModel.userSearchKey.postValue(s)
            }
        })

        viewModel.searchOption.observe(
            viewLifecycleOwner,
            Observer {
                viewModel.setSearchOption(binding.spinnerSearchOptions, it)
            }
        )

        viewModel.searchBarHint.observe(
            viewLifecycleOwner,
            Observer {
                binding.searchViewModel = viewModel
            }
        )

        viewModel.sports.observe(
            viewLifecycleOwner,
            Observer {
                initializeSpinnerForSports(it)
            }
        )

        binding.twSearchEventWithMap.setOnClickListener {
            viewModel.clearCoordinates()
            MapsActivity.openMaps(activity as MainActivity, true)
        }

        binding.btnSearch.setOnClickListener {

            when (viewModel.searchOption.value) {
                0 -> {
                    navigateToUserSearchFragment()
                }

                1 -> {
                    navigateToEventSearchFragment()
                }

                2 -> {

                }

            }
        }
    }

    private fun initializeSpinner() {
        ArrayAdapter.createFromResource(
            requireContext(),
            R.array.searchOptions,
            R.layout.item_spinner
        ).also { adapter ->
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
            binding.spinnerSearchOptions.adapter = adapter
        }
        binding.spinnerSearchOptions.onItemSelectedListener = this
    }

    private fun initializeSpinnerForSports(sports: Array<String>) {
        val arrayAdapter =
            ArrayAdapter(requireContext(), android.R.layout.simple_spinner_dropdown_item, sports)
        binding.spinnerSport.adapter = arrayAdapter
    }

    private fun initializeSpinnersForLevels() {
        ArrayAdapter.createFromResource(
            requireContext(),
            R.array.levels,
            R.layout.item_spinner
        ).also { adapter ->
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
            binding.spinnerMinLevel.adapter = adapter
            binding.spinnerMaxLevel.adapter = adapter
        }
    }

    private fun navigateToEventSearchFragment() {
        val transaction =
            requireActivity().supportFragmentManager.beginTransaction()
        val fragmentToGo = EventSearchFragment.newInstance(
            EventFilterRequest(
                nameContains = if (viewModel.eventSearchKey.value.toString()
                        .isNotEmpty()
                ) binding.searchBar.text.toString() else null,
                sport = binding.spinnerSport.selectedItem.toString(),
                city = if (binding.etSearchCity.text.toString()
                        .isNotEmpty()
                ) binding.etSearchCity.text.toString() else null,
                country = if (binding.etSearchCountry.text.toString()
                        .isNotEmpty()
                ) binding.etSearchCountry.text.toString() else null,
                skillLevels = listOf(
                    binding.spinnerMinLevel.selectedItem.toString().toInt(),
                    binding.spinnerMaxLevel.selectedItem.toString().toInt()
                )
            ),
            viewModel.listOfEventSearchCoordinates
        )
        transaction.replace(R.id.mainContainer, fragmentToGo)
        transaction.addToBackStack(null)
        transaction.commit()
    }

    private fun navigateToUserSearchFragment() {
        val transaction =
            requireActivity().supportFragmentManager.beginTransaction()
        val fragmentToGo = UserSearchFragment.newInstance(
            UserSearchRequest(
                identifier = if (viewModel.userSearchKey.value.toString()
                        .isNotEmpty()
                ) binding.searchBar.text.toString() else null,
            )
        )
        transaction.replace(R.id.mainContainer, fragmentToGo)
        transaction.addToBackStack(null)
        transaction.commit()
    }

    override fun onItemSelected(p0: AdapterView<*>?, p1: View?, position: Int, p3: Long) {
        viewModel.searchOption.postValue(position)
    }

    override fun onNothingSelected(position: AdapterView<*>?) {}
}