package com.example.sportsplatform

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.databinding.ActivityMainBinding
import com.example.sportsplatform.util.hide
import com.example.sportsplatform.util.show
import kotlinx.android.synthetic.main.activity_main.*
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
        viewModel.userLiveData.observe(this, Observer {
            textView.text = it
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