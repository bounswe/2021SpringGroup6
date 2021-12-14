package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.view.View
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.ProfileActivity
import com.example.sportsplatform.data .UserRepository
import com.example.sportsplatform.data .models.UserRegisterRequest
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.toast


class RegisterViewModel(private val userRepo: UserRepository) : ViewModel() {

    var identifier: String? = null
    var pass: String? = null
    var registerName: String? = null
    var username: String? = null
    var gender: String? = null
    var email: String? = null
    var surname: String? = null
    var location: String? = null
    var age: String? = null
    var registerPassword: String? = null
    var sports: String? = null

    fun onSignUpButtonClick(view: View){

        Coroutines.main {
            val userRegisterRequest = UserRegisterRequest(
                email = email!!,
                password = registerPassword!!,
                identifier = username!!
            )

            val currResponse = userRepo.signUser(userRegisterRequest)
            view.context.toast(currResponse.toString())
            if (currResponse.isSuccessful) {

                Intent(view.context, ProfileActivity::class.java).also{
                    view.context.startActivity(it)
                }

            } else {
                view.context.toast("Fail")
            }
        }
    }
}