package com.example.sportsplatform

import android.app.Activity
import android.content.Context
import android.view.View
import android.view.inputmethod.InputMethodManager
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.Repository
import com.example.sportsplatform.data.models.UserRequest
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.toast


class PlatformViewModel(private val repo: Repository) : ViewModel() {

    var platformListener: PlatformListener? = null
    val userLiveData = MutableLiveData<String>()

    var identifier: String? = null
    var pass: String? = null

    fun onSearchButtonClick(view: View){

        closeSoftKeyboard(view.context, view)

        if(identifier.isNullOrEmpty() || pass.isNullOrEmpty()){
            return
        }

        Coroutines.main {
            val userRequest = UserRequest(identifier!!, pass!!)
            val currResponse = repo.findUser(userRequest)
            if (currResponse.isSuccessful) {
                //weatherListener?.onSuccess()
                val userToken = currResponse.body()?.user_id
                userLiveData.postValue(userToken.toString())
                view.context.toast("Success")
                view.context.toast(userToken.toString())
            } else {
                view.context.toast(identifier!!)
                view.context.toast(pass!!)
                view.context.toast("Fail")
                //weatherListener?.onFailure()
            }
        }
    }

    fun onRegisterButtonClick(view: View){

        closeSoftKeyboard(view.context, view)

    }

    private fun closeSoftKeyboard(context: Context, v: View) {
        val iMm = context.getSystemService(Activity.INPUT_METHOD_SERVICE) as InputMethodManager
        iMm.hideSoftInputFromWindow(v.windowToken, 0)
        v.clearFocus()
    }

}