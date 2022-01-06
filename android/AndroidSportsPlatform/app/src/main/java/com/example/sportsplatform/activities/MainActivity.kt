package com.example.sportsplatform.activities

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import com.example.sportsplatform.R
import com.example.sportsplatform.databinding.ActivityMainBinding
import com.example.sportsplatform.fragments.TabBarFragment
import org.kodein.di.KodeinAware
import org.kodein.di.android.kodein

class MainActivity : AppCompatActivity(), KodeinAware {

    override val kodein by kodein()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding: ActivityMainBinding = DataBindingUtil.setContentView(
            this, R.layout.activity_main)
        val view = binding.root
        setContentView(view)

        val transaction = supportFragmentManager.beginTransaction()
        val fragmentToGo = TabBarFragment()
        if (savedInstanceState == null) {
            transaction.replace(R.id.mainContainer, fragmentToGo)
            transaction.commitAllowingStateLoss()
        }

    }
}