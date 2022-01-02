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
import com.example.sportsplatform.adapter.UserListAdapter
import com.example.sportsplatform.adapter.UsersClickListener
import com.example.sportsplatform.data.models.requests.UserSearchRequest
import com.example.sportsplatform.data.models.responses.UserResponse
import com.example.sportsplatform.databinding.FragmentSearchUserBinding
import com.example.sportsplatform.viewmodelfactories.UserSearchViewModelFactory
import com.example.sportsplatform.viewmodels.UserSearchViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class UserSearchFragment : Fragment(), KodeinAware, UsersClickListener {
    private var _binding: FragmentSearchUserBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: UserSearchViewModel
    private val factory: UserSearchViewModelFactory by instance()

    private val usersAdapter by lazy { UserListAdapter(this) }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentSearchUserBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(UserSearchViewModel::class.java)

        getBundleArguments()

        initializeRecyclerview()

        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.usersFiltered.observe(
            viewLifecycleOwner,
            Observer {
                usersAdapter.items = it?.items?.toMutableList() ?: mutableListOf()
            }
        )
    }

    private fun getBundleArguments() {
        arguments?.let {
            viewModel.setArguments(
                it.getParcelable(USER_SEARCH)
            )
        }
    }

    private fun initializeRecyclerview() {
        binding.rvUsersSearched.apply {
            layoutManager = LinearLayoutManager(context)
            adapter = usersAdapter
        }
    }

    companion object {
        private const val USER_SEARCH = "user_search"
        fun newInstance(
            userSearch: UserSearchRequest?
        ) = UserSearchFragment().apply {
            arguments = Bundle().apply {
                putParcelable(USER_SEARCH, userSearch)
            }
        }
    }

    override fun onUsersClickListener(userResponse: UserResponse?) {
        val transaction = requireActivity().supportFragmentManager.beginTransaction()
        val fragmentToGo = UserDetailFragment.newInstance(userId = userResponse?.user_id)
        transaction.replace(R.id.mainContainer, fragmentToGo)
        transaction.addToBackStack(null)
        transaction.commit()
    }

}