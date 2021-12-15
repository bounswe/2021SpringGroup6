package com.example.sportsplatform.viewmodels

import android.content.Intent
import android.view.View
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.activities.ProfileActivity
import com.example.sportsplatform.data .UserRepository
import com.example.sportsplatform.data.models.Sport
import com.example.sportsplatform.data .models.UserRegisterRequest
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.toast


class RegisterViewModel(private val userRepo: UserRepository) : ViewModel() {

    var etEmail: String? = null
    var etPassword: String? = null
    var etIdentifier: String? = null
    var etName: String? = null
    var etFamilyName: String? = null
    var etBirthDate: String? = null
    var etGender: String? = null
    var etSports: List<Sport>? = null

    fun onSignUpButtonClick(view: View){

        Coroutines.main {
            val userRegisterRequest = UserRegisterRequest(
                email = etEmail!!,
                password = etPassword!!,
                identifier = etIdentifier!!,
                name = etName!!,
                familyName = etFamilyName!!,
                birthDate = etBirthDate!!,
                gender = etGender!!,
                sports = etSports!!
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