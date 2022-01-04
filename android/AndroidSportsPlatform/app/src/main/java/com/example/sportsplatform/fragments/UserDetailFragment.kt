package com.example.sportsplatform.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.sportsplatform.adapter.UserBadgesAdapter
import com.example.sportsplatform.adapter.UserFollowedAdapter
import com.example.sportsplatform.adapter.UserFollowingAdapter
import com.example.sportsplatform.data.models.requests.AddBadgeRequest
import com.example.sportsplatform.databinding.FragmentDetailedUserBinding
import com.example.sportsplatform.viewmodelfactories.UserDetailViewModelFactory
import com.example.sportsplatform.viewmodels.UserDetailViewModel
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class UserDetailFragment : Fragment(), KodeinAware {

    private var _binding: FragmentDetailedUserBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: UserDetailViewModel
    private val factoryDetail: UserDetailViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentDetailedUserBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factoryDetail).get(UserDetailViewModel::class.java)
        viewModel.userId.postValue(arguments?.getInt(USER_ID) ?: 0)

        initializeRecyclerview()

        viewModel.getUserInformation(arguments?.getInt(USER_ID) ?: 0)

        viewModel.fetchUsersBadgeList(arguments?.getInt(USER_ID) ?: 0)

        viewModel.fetchUsersFollowingList(arguments?.getInt(USER_ID) ?: 0)

        return binding.root
    }

    override fun onResume() {
        super.onResume()
        binding.userDetailViewModel = viewModel
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        viewModel.user.observe(
            viewLifecycleOwner,
            Observer {
                binding.userDetailViewModel = viewModel
            }
        )

        viewModel.usersBadgeList.observe(
            viewLifecycleOwner,
            Observer {
                binding.rvUserBadges.apply {
                    layoutManager =
                        LinearLayoutManager(context)
                    adapter =
                        UserBadgesAdapter(it?.additionalProperty?.get(1)?.value)
                }
            }
        )

        viewModel.addUserBadgeResponse.observe(
            viewLifecycleOwner,
            Observer {
                binding.userDetailViewModel = viewModel
            }
        )

        binding.btnFollowUser.setOnClickListener{
            viewModel.followUser(
                arguments?.getInt(USER_ID) ?: 0
            )
            Toast.makeText(this.context,"User is followed!" ,Toast.LENGTH_SHORT).show()
        }

        binding.btnAddBadge.setOnClickListener {
            viewModel.addUserBadge(
                AddBadgeRequest(
                    binding.etBadgeName.text.toString()
                ), arguments?.getInt(USER_ID) ?: 0
            )
            Toast.makeText(this.context,"Badge is added!" ,Toast.LENGTH_SHORT).show()
        }
    }

    private fun initializeRecyclerview() {
        viewModel.usersBadgeList.observe(
            viewLifecycleOwner,
            Observer {
                binding.rvUserBadges.apply {
                    layoutManager = LinearLayoutManager(context)
                    adapter = UserBadgesAdapter(
                        it?.additionalProperty?.get(1)?.value,
                    )
                }
            }
        )
        viewModel.usersFollowingList.observe(
            viewLifecycleOwner,
                    {
                binding.rvFollowingUsers.apply{
                    layoutManager = LinearLayoutManager(context)
                    adapter = UserFollowingAdapter(
                        it?.items,
                    )
                }
            }
        )
        viewModel.usersFollowedList.observe(
            viewLifecycleOwner,
            {
                binding.rvFollowedUsers.apply{
                    layoutManager = LinearLayoutManager(context)
                    adapter = UserFollowedAdapter(
                        it?.items,
                    )
                }
            }
        )
    }

    companion object {
        private const val USER_ID = "user_id"
        fun newInstance(userId: Int?) = UserDetailFragment().apply {
            arguments = Bundle().apply {
                userId?.let { putInt(USER_ID, it) }
            }
        }
    }

}