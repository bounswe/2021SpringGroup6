package com.example.sportsplatform

import android.app.Application
import com.example.sportsplatform.data.Repository
import com.example.sportsplatform.data.UserApi
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
        bind() from singleton { Repository(instance()) }
        bind() from provider { PlatformViewModelFactory(instance()) }
    }
}