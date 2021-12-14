package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.view.View
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.activities.RegisterActivity
import com.example.sportsplatform.activities.SearchOperationsActivity
import com.example.sportsplatform.data.UserRepository
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.closeSoftKeyboard
import com.example.sportsplatform.util.toast

class ProfileViewModel(private val repo: UserRepository) : ViewModel() {

    var userId: String? = null
    var event: String? = null

    fun onSearchImageButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, SearchOperationsActivity::class.java).also {
                view.context.startActivity(it)
            }

            if(!userId.isNullOrEmpty() || !event.isNullOrEmpty()){
                if(!userId.isNullOrEmpty()){
                    val currResponse = repo.searchUserProfile(Integer.parseInt(userId!!))
                    view.context.toast(currResponse.toString())
                    if (currResponse.isSuccessful) {
                        val userName = currResponse.body()?.name
                        if (userName != null) {
                            view.context.toast(userName)
                        }
                    } else {
                        view.context.toast("Fail")
                    }
                }
                else{
                    val currResponse = repo.searchUserProfile(Integer.parseInt(userId!!))
                    view.context.toast(currResponse.toString())
                    if (currResponse.isSuccessful) {
                        val userName = currResponse.body()?.name
                        if (userName != null) {
                            view.context.toast(userName)
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