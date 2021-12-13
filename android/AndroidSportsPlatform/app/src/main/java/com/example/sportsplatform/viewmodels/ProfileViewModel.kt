package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.view.View
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.ProfileActivity
import com.example.sportsplatform.RegisterActivity
import com.example.sportsplatform.activities.SearchOperationsActivity
import com.example.sportsplatform.data.UserRepository
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.closeSoftKeyboard
import com.example.sportsplatform.util.toast

class ProfileViewModel(
        private val userRepo: UserRepository,
        private val eventRepo: EventRepository) : ViewModel() {

    var userId: String? = null
    var event: String? = null

    fun onSearchImageButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, SearchOperationsActivity::class.java).also {
                view.context.startActivity(it)
            }
        }
    }

    fun onSearchButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            if(!userId.isNullOrEmpty() || !event.isNullOrEmpty()) {
                if (!userId.isNullOrEmpty()) {
                    val currResponse = userRepo.searchUserProfile(Integer.parseInt(userId!!))
                    view.context.toast(currResponse.toString())
                    if (currResponse.isSuccessful) {
                        val userName = currResponse.body()?.name
                        if (userName != null) {
                            view.context.toast(userName)
                        }
                    } else {
                        view.context.toast("Fail")
                    }
                } else {
                    val currResponse = eventRepo.findEvent(Integer.parseInt(event!!))
                    view.context.toast(currResponse.toString())
                    if (currResponse.isSuccessful) {
                        val eventName = currResponse.body()?.event
                        if (eventName != null) {
                            view.context.toast(eventName)
                        }
                    } else {
                        view.context.toast("Fail")
                    }
                }
            }
        }
    }

    fun onProfileButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, RegisterActivity::class.java).also {
                view.context.startActivity(it)
            }
        }

    }


    fun onMenuButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, RegisterActivity::class.java).also {
                view.context.startActivity(it)
            }
        }

    }
}