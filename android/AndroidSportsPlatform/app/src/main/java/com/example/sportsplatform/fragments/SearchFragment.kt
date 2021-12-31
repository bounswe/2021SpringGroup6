package com.example.sportsplatform.fragments

import android.content.Context
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
import com.example.sportsplatform.R
import com.example.sportsplatform.activities.MainActivity
import com.example.sportsplatform.activities.MapsActivity
import com.example.sportsplatform.databinding.FragmentSearchBinding
import com.example.sportsplatform.util.Constants
import com.example.sportsplatform.viewmodels.SearchViewModel
import com.example.sportsplatform.viewmodelfactories.SearchViewModelFactory
import com.google.android.gms.maps.model.LatLng
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance
import com.google.gson.Gson

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
        viewModel.setCustomSharedPreferences(
            requireActivity().getSharedPreferences(
                Constants.CUSTOM_SHARED_PREFERENCES,
                Context.MODE_PRIVATE
            )
        )
        viewModel.custSharedPreferences?.edit()?.putString("listOfMarkerPositions", null)?.apply()
        initializeSpinner()
        binding.searchViewModel = viewModel
        return binding.root
    }

    override fun onResume() {
        super.onResume()
        val listOfEventSearchCoordinates = getEventSearchCoordinatesFromSharedPreferences()
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
                viewModel.setSearchOption(binding.spinner, it)
            }
        )

        viewModel.searchBarHint.observe(
            viewLifecycleOwner,
            Observer {
                binding.searchViewModel = viewModel
            }
        )

        binding.twSearchEventWithMap.setOnClickListener {
            MapsActivity.openMaps(activity as MainActivity, true)
        }

        binding.btnSearch.setOnClickListener {
            if (viewModel.eventSearchKey.value.toString().isNotEmpty() ||
                viewModel.eventSearchKey.value.toString().isNotBlank() ||
                viewModel.userSearchKey.value.toString().isNotEmpty() ||
                viewModel.userSearchKey.value.toString().isNotBlank()
            ) {
                when (viewModel.searchOption.value) {
                    0 -> {
                        val transaction = requireActivity().supportFragmentManager.beginTransaction()
                        val arguments = Bundle()
                        arguments.putString("user_search_filter", viewModel.userSearchKey.value.toString())
                        val fragmentToGo = UserSearchFragment()
                        fragmentToGo.arguments = arguments
                        if (savedInstanceState == null) {
                            transaction.replace(R.id.mainContainer, fragmentToGo)
                            transaction.addToBackStack(null)
                            transaction.commitAllowingStateLoss()
                        }
                    }

                    1 -> {
                        navigateToEventSearchFragment()
                    }

                    2 -> {
                    }
                }
            } else {
                viewModel.eventsFiltered.postValue(null)
                viewModel.usersFiltered.postValue(null)
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
            binding.spinner.adapter = adapter
        }
        binding.spinner.onItemSelectedListener = this
    }

    private fun navigateToEventSearchFragment() {
        val transaction =
            requireActivity().supportFragmentManager.beginTransaction()
        val arguments = Bundle()
        arguments.putString(
            "event_search_filter",
            viewModel.eventSearchKey.value.toString()
        )
        val fragmentToGo = EventSearchFragment()
        fragmentToGo.arguments = arguments
        transaction.replace(R.id.mainContainer, fragmentToGo)
        transaction.addToBackStack(null)
        transaction.commitAllowingStateLoss()
    }

    private fun getEventSearchCoordinatesFromSharedPreferences(): Array<LatLng>? {
        val serializedObject =
            viewModel.custSharedPreferences?.getString("listOfMarkerPositions", null)
        return serializedObject?.let {
            val gson = Gson()
            gson.fromJson(it, Array<LatLng>::class.java)
        }
    }

    override fun onItemSelected(p0: AdapterView<*>?, p1: View?, position: Int, p3: Long) {
        viewModel.searchOption.postValue(position)
    }

    override fun onNothingSelected(position: AdapterView<*>?) {}
}