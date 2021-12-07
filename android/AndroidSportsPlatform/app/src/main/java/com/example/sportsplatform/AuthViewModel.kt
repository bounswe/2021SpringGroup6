package com.example.sportsplatform

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.view.View
import android.view.inputmethod.InputMethodManager
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.Repository
import com.example.sportsplatform.data.models.UserRegisterRequest
import com.example.sportsplatform.data.models.UserRequest
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.toast


class AuthViewModel(private val repo: Repository) : ViewModel() {

    var authListener: AuthListener? = null
    val userLiveData = MutableLiveData<String>()

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

    fun onSearchButtonClick(view: View){
        //weatherListener?.onStarted()
        //closeSoftKeyboard(view.context, view)

        closeSoftKeyboard(view.context, view)

        if(identifier.isNullOrEmpty() || pass.isNullOrEmpty()){
            return
        }


        Coroutines.main {
            val userRequest = UserRequest(identifier!!, pass!!)
            val currResponse = repo.findUser(userRequest)
            view.context.toast(currResponse.toString())
            if (currResponse.isSuccessful) {

                val userToken = currResponse.body()?.token
                userLiveData.postValue(userToken)
                view.context.toast("Success")
                Intent(view.context, ProfilePageActivity::class.java).also{
                    view.context.startActivity(it)
                }
            } else {
                view.context.toast(identifier!!)
                view.context.toast(pass!!)
            }
        }
    }

    fun onRegisterButtonClick(view: View){

        Coroutines.main {
            Intent(view.context, RegisterActivity::class.java).also{
                view.context.startActivity(it)
            }

            val userRegisterRequest = UserRegisterRequest(
                    email = email!!,
                    password = registerPassword!!,
                    identifier = username!!,
                    name = registerName!!,
                    familyName = surname!!,
                    birthDate = age!!,
                    gender = gender!!,
                    sports = sports!!
            )

            val currResponse = repo.signUser(userRegisterRequest)
            view.context.toast(currResponse.toString())
            if (currResponse.isSuccessful) {

                Intent(view.context, ProfilePageActivity::class.java).also{
                    view.context.startActivity(it)
                }

            } else {
                view.context.toast("Fail")
            }

        }
    }

    private fun closeSoftKeyboard(context: Context, v: View) {
        val iMm = context.getSystemService(Activity.INPUT_METHOD_SERVICE) as InputMethodManager
        iMm.hideSoftInputFromWindow(v.windowToken, 0)
        v.clearFocus()
    }

}