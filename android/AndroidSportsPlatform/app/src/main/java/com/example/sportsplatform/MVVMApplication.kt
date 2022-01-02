package com.example.sportsplatform

import android.app.Application
import com.example.sportsplatform.data.api.EventApi
import com.example.sportsplatform.data.api.SportApi
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.data.api.UserApi
import com.example.sportsplatform.data.repository.SportRepository
import com.example.sportsplatform.viewmodelfactories.*
import com.example.sportsplatform.viewmodels.*
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
        bind() from singleton { SportApi() }
        bind() from singleton { UserRepository(instance()) }
        bind() from singleton { EventRepository(instance()) }
        bind() from singleton { SportRepository(instance()) }
        bind() from provider { AuthViewModelFactory(instance(), instance()) }
        bind() from provider { ProfileViewModelFactory(instance(), instance()) }
        bind() from provider { EventSearchViewModelFactory(instance()) }
        bind() from provider { UserSearchViewModelFactory(instance()) }
        bind() from provider { UserDetailViewModelFactory(instance(), instance()) }
        bind() from provider { RegisterViewModelFactory(instance()) }
        bind() from provider { SearchViewModelFactory(instance()) }
        bind() from provider { HomeViewModelFactory(instance(), instance()) }
        bind() from provider { CreateEventViewModelFactory(instance(), instance()) }
        bind() from provider { ProfileFragmentViewModelFactory(instance(), instance()) }
        bind() from provider { EventDetailViewModelFactory(instance(), instance()) }
    }
}