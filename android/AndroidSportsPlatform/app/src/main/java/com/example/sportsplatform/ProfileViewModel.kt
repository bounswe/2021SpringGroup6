package com.example.sportsplatform

import android.content.Intent
import android.view.View
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.Repository
import com.example.sportsplatform.data.models.UserRequest
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.closeSoftKeyboard
import com.example.sportsplatform.util.toast

class ProfileViewModel(private val repo: Repository) : ViewModel() {

    fun onSearchImageButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        Coroutines.main {
            Intent(view.context, RegisterActivity::class.java).also {
                view.context.startActivity(it)
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