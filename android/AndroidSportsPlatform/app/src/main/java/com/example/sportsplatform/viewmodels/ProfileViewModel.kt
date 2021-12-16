package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.view.View
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.activities.ProfileActivity
import com.example.sportsplatform.activities.SearchOperationsActivity
import com.example.sportsplatform.data.repository.EventRepository
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.closeSoftKeyboard

class ProfileViewModel(
    private val userRepo: UserRepository,
    private val eventRepo: EventRepository
) : ViewModel() {

    fun onSearchImageButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, SearchOperationsActivity::class.java).also {
                view.context.startActivity(it)
            }
        }
    }


    fun onProfileButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, ProfileActivity::class.java).also {
                view.context.startActivity(it)
            }
        }
    }


    fun onMenuButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, ProfileActivity::class.java).also {
                view.context.startActivity(it)
            }
        }
    }
}