package com.example.sportsplatform.activities

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.asLiveData
import androidx.lifecycle.lifecycleScope
import com.example.sportsplatform.AuthListener
import com.example.sportsplatform.R
import com.example.sportsplatform.data.UserPreferences
import com.example.sportsplatform.databinding.ActivityMainBinding
import com.example.sportsplatform.util.hide
import com.example.sportsplatform.util.show
import com.example.sportsplatform.viewmodels.AuthViewModel
import com.example.sportsplatform.viewmodels.AuthViewModelFactory
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.coroutines.launch
import org.kodein.di.KodeinAware
import org.kodein.di.android.kodein
import org.kodein.di.generic.instance

class MainActivity : AppCompatActivity(), AuthListener, KodeinAware {

    private lateinit var viewModel: AuthViewModel
    override val kodein by kodein()
    private val factory : AuthViewModelFactory by instance()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        viewModel = ViewModelProvider(this, factory).get(AuthViewModel::class.java)
        binding.viewmodel = viewModel
        viewModel.authListener = this

        initObservers()

    }
    private fun initObservers(){
        val userPreferences = UserPreferences(this)

        viewModel.userLiveData.observe(this, Observer {
            lifecycleScope.launch {
                userPreferences.saveAuthToken(it)
            }
        })

        userPreferences.authToken.asLiveData().observe(this, Observer {
            Toast.makeText(this, it ?: "Token null", Toast.LENGTH_SHORT).show()
            startActivity(Intent(this, MainActivity::class.java))
        })

    }

    override fun onStarted(){
        progressBar.show()
    }

    override fun onSuccess() {
        progressBar.hide()
    }

    override fun onFailure() {
        progressBar.hide()
    }
}