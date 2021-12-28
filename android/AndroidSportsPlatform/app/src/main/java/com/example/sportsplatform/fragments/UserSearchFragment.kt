package com.example.sportsplatform.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.adapter.UserSearchAdapter
import com.example.sportsplatform.databinding.FragmentSearchUserBinding
import com.example.sportsplatform.viewmodelfactories.UserSearchViewModelFactory
import com.example.sportsplatform.viewmodels.UserSearchViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class UserSearchFragment : Fragment(), KodeinAware {
    private var _binding: FragmentSearchUserBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: UserSearchViewModel
    private val factory: UserSearchViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSearchUserBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(UserSearchViewModel::class.java)
        viewModel.fillSearchUserList(arguments?.getString("user_search_filter"))
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.usersSearched.observe(
            viewLifecycleOwner,
            Observer {
                binding.rvUsersSearched.apply {
                    layoutManager =
                        LinearLayoutManager(context)
                    adapter =
                        it?.items?.let { foundUserItems -> UserSearchAdapter(foundUserItems) }
                }
            }
        )
    }
}