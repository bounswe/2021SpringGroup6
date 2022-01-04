package com.example.sportsplatform.activities

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.R
import com.example.sportsplatform.databinding.ActivityLoginBinding
import com.example.sportsplatform.viewmodels.AuthViewModel
import com.example.sportsplatform.viewmodelfactories.AuthViewModelFactory
import org.kodein.di.KodeinAware
import org.kodein.di.android.kodein
import org.kodein.di.generic.instance

class LoginActivity : AppCompatActivity(), KodeinAware {

    private lateinit var viewModel: AuthViewModel
    override val kodein by kodein()
    private val factory : AuthViewModelFactory by instance()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding: ActivityLoginBinding = DataBindingUtil.setContentView(this,
            R.layout.activity_login
        )
        viewModel = ViewModelProvider(this, factory).get(AuthViewModel::class.java)
        binding.viewmodel = viewModel

        initObservers()

    }
    private fun initObservers(){
        viewModel.userLiveData.observe(this, Observer {
            //etLoginIdentifier.text = it
        })
    }
}