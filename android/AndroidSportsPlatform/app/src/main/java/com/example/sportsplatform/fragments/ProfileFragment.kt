package com.example.sportsplatform.fragments

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.activities.LoginActivity
import com.example.sportsplatform.data.models.requests.UserUpdateRequest
import com.example.sportsplatform.databinding.FragmentProfileBinding
import com.example.sportsplatform.util.toast
import com.example.sportsplatform.viewmodels.ProfileFragmentViewModel
import com.example.sportsplatform.viewmodelfactories.ProfileFragmentViewModelFactory
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.generic.instance

class ProfileFragment : Fragment(), KodeinAware {

    private var _binding: FragmentProfileBinding? = null
    private val binding get() = _binding!!

    override lateinit var kodein: Kodein

    private lateinit var viewModel: ProfileFragmentViewModel
    private val factory : ProfileFragmentViewModelFactory by instance()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentProfileBinding.inflate(inflater, container, false)
        kodein = (requireActivity().applicationContext as KodeinAware).kodein
        viewModel = ViewModelProvider(this, factory).get(ProfileFragmentViewModel::class.java)
        viewModel.getUser()
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        viewModel.userInformation.observe(
            viewLifecycleOwner,
            Observer {
                binding.profileViewModel = viewModel
            }
        )

        binding.btnUpdateProfile.setOnClickListener {

            view?.context?.toast("User is Updated!")

            viewModel.updUser(
                UserUpdateRequest(
                    email = binding.etEmail.text.toString(),
                    name = binding.etUserName.text.toString(),
                    familyName = binding.etUserFamilyName.text.toString(),
                    birthDate = binding.etBirthDate.text.toString(),
                    gender = binding.etGender.text.toString(),
                    sports = null
                )
            )
        }

        binding.btnDeleteProfile.setOnClickListener {
            view?.context?.toast("User is Deleted!")
            viewModel.dltUser()
            Intent(view.context, LoginActivity::class.java).also{
                view.context.startActivity(it)
            }
        }
    }
}