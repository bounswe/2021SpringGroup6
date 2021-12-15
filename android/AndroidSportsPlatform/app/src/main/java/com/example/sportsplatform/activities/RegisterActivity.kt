package com.example.sportsplatform.activities

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProvider
import com.example.sportsplatform.R
import com.example.sportsplatform.databinding.ActivityRegisterBinding
import com.example.sportsplatform.viewmodels.RegisterViewModel
import com.example.sportsplatform.viewmodels.RegisterViewModelFactory
import org.kodein.di.KodeinAware
import org.kodein.di.android.kodein
import org.kodein.di.generic.instance

class RegisterActivity : AppCompatActivity(), KodeinAware {
    private lateinit var registerViewModel: RegisterViewModel
    override val kodein by kodein()
    private val factory : RegisterViewModelFactory by instance()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding: ActivityRegisterBinding = DataBindingUtil.setContentView(
            this, R.layout.activity_register)

        val view = binding.root
        setContentView(view)

        registerViewModel = ViewModelProvider(this, factory).get(RegisterViewModel::class.java)
        binding.registerviewmodel = registerViewModel

    }
}