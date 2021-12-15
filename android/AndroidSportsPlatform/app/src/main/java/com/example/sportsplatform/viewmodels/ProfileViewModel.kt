package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.view.View
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.activities.ProfileActivity
import com.example.sportsplatform.activities.RegisterActivity
import com.example.sportsplatform.activities.SearchOperationsActivity
import com.example.sportsplatform.data.EventRepository
import com.example.sportsplatform.data.UserRepository
import com.example.sportsplatform.data.models.EventFilterRequest
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.closeSoftKeyboard
import com.example.sportsplatform.util.toast

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