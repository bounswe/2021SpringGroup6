package com.example.sportsplatform.util

import android.app.Activity
import android.content.Context
import android.view.View
import android.view.inputmethod.InputMethodManager
import android.widget.ProgressBar
import android.widget.Toast

fun Context.toast(message: String){
    Toast.makeText(this, message, Toast.LENGTH_LONG).show()
}

fun ProgressBar.show() {
    this.visibility = View.VISIBLE
}

fun ProgressBar.hide() {
    this.visibility = View.GONE
}

fun closeSoftKeyboard(context: Context, v: View) {
    val iMm = context.getSystemService(Activity.INPUT_METHOD_SERVICE) as InputMethodManager
    iMm.hideSoftInputFromWindow(v.windowToken, 0)
    v.clearFocus()
}