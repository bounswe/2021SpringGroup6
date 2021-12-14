package com.example.sportsplatform.activities

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.R
import com.example.sportsplatform.databinding.ActivityProfileBinding
import com.example.sportsplatform.databinding.ActivityRegisterBinding
import com.example.sportsplatform.viewmodels.ProfileViewModel
import com.example.sportsplatform.viewmodels.ProfileViewModelFactory
import com.example.sportsplatform.viewmodels.RegisterViewModel
import com.example.sportsplatform.viewmodels.RegisterViewModelFactory
import org.kodein.di.KodeinAware
import org.kodein.di.android.kodein
import org.kodein.di.generic.instance

class ProfileActivity : AppCompatActivity(), KodeinAware {

    private lateinit var profileViewModel: ProfileViewModel
    override val kodein by kodein()
    private val factory : ProfileViewModelFactory by instance()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding: ActivityProfileBinding = DataBindingUtil.setContentView(
                this, R.layout.activity_profile)
        val view = binding.root
        setContentView(view)

        profileViewModel = ViewModelProvider(this, factory).get(ProfileViewModel::class.java)
        binding.profileviewmodel = profileViewModel
    }
}