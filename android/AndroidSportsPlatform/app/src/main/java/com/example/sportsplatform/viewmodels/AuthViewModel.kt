package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.content.SharedPreferences
import android.view.View
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.AuthListener
import com.example.sportsplatform.activities.MainActivity
import com.example.sportsplatform.activities.RegisterActivity
import com.example.sportsplatform.data.repository.UserRepository
import com.example.sportsplatform.data.models.requests.UserRequest
import com.example.sportsplatform.util.Constants.SHARED_PREFS_USER_ID
import com.example.sportsplatform.util.Constants.SHARED_PREFS_USER_TOKEN
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.closeSoftKeyboard
import com.example.sportsplatform.util.toast


class AuthViewModel(
    private val repo: UserRepository,
    private val sharedPreferences: SharedPreferences
) : ViewModel() {

    var authListener: AuthListener? = null
    val userLiveData = MutableLiveData<String>()

    var identifier: String? = null
    var pass: String? = null

    fun onLoginButtonClick(view: View) {
        closeSoftKeyboard(view.context, view)

        if (identifier.isNullOrEmpty() || pass.isNullOrEmpty()) {
            return
        }

        Coroutines.main {
            val userRequest = UserRequest(identifier!!, pass!!)
            val currResponse = repo.findUser(userRequest)
            //view.context.toast(currResponse.toString())
            if (currResponse.isSuccessful) {

                val userToken = currResponse.body()?.token
                val userId = currResponse.body()?.user_id
                userLiveData.postValue(userToken)
                userId?.let { sharedPreferences.edit()?.putInt(SHARED_PREFS_USER_ID, it)?.apply() }
                userToken?.let {
                    sharedPreferences.edit()?.putString(SHARED_PREFS_USER_TOKEN, it)?.apply()
                }
                //view.context.toast("Success")
                Intent(view.context, MainActivity::class.java).also{
                    view.context.startActivity(it)
                }
            } else {
                view.context.toast(identifier!!)
                view.context.toast(pass!!)
            }
        }
    }

    fun onRegisterButtonClick(view: View) {

        Coroutines.main {
            Intent(view.context, RegisterActivity::class.java).also {
                view.context.startActivity(it)
            }
        }
    }


}