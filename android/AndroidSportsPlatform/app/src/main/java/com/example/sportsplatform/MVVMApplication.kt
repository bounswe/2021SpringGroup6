package com.example.sportsplatform

import android.app.Application
import com.example.sportsplatform.data.EventApi
import com.example.sportsplatform.data.EventRepository
import com.example.sportsplatform.data.UserRepository
import com.example.sportsplatform.data.UserApi
import com.example.sportsplatform.viewmodels.AuthViewModelFactory
import com.example.sportsplatform.viewmodels.EventSearchViewModelFactory
import com.example.sportsplatform.viewmodels.ProfileViewModelFactory
import com.example.sportsplatform.viewmodels.RegisterViewModelFactory
import org.kodein.di.Kodein
import org.kodein.di.KodeinAware
import org.kodein.di.android.x.androidXModule
import org.kodein.di.generic.bind
import org.kodein.di.generic.instance
import org.kodein.di.generic.provider
import org.kodein.di.generic.singleton

class MVVMApplication : Application(), KodeinAware {

    override val kodein = Kodein.lazy {

        import(androidXModule(this@MVVMApplication))

        bind() from singleton { UserApi() }
        bind() from singleton { EventApi() }
        bind() from singleton { UserRepository(instance()) }
        bind() from singleton { EventRepository(instance()) }
        bind() from provider { AuthViewModelFactory(instance()) }
        bind() from provider { ProfileViewModelFactory(instance(), instance()) }
        bind() from provider { EventSearchViewModelFactory(instance()) }
        bind() from provider { RegisterViewModelFactory(instance()) }
    }
}