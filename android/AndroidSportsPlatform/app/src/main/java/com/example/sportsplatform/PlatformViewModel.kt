package com.example.sportsplatform

import android.app.Activity
import android.content.Context
import android.view.View
import android.view.inputmethod.InputMethodManager
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.sportsplatform.data.Repository
import com.example.sportsplatform.util.Coroutines
import com.example.sportsplatform.util.toast


class PlatformViewModel(private val repo: Repository) : ViewModel() {

    var platformListener: PlatformListener? = null
    val userLiveData = MutableLiveData<String>()

    var identifier: String? = null
    var pass: String? = null

    fun onSearchButtonClick(view: View){
        //weatherListener?.onStarted()
        //closeSoftKeyboard(view.context, view)

        closeSoftKeyboard(view.context, view)

        if(identifier.isNullOrEmpty()){
            return
        }


        Coroutines.main {
            val currResponse = repo.findUser(identifier!!, pass!!)
            if (currResponse.isSuccessful) {
                //weatherListener?.onSuccess()
                val userToken = currResponse.body()?.token
                userLiveData.postValue(userToken)
                view.context.toast("Success")
            } else {
                view.context.toast(identifier!!)
                view.context.toast(pass!!)
                //weatherListener?.onFailure()
            }
        }
    }

    private fun closeSoftKeyboard(context: Context, v: View) {
        val iMm = context.getSystemService(Activity.INPUT_METHOD_SERVICE) as InputMethodManager
        iMm.hideSoftInputFromWindow(v.windowToken, 0)
        v.clearFocus()
    }

}