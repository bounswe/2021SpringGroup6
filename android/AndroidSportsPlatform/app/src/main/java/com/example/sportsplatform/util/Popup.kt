package com.example.sportsplatform.util

import android.app.Dialog
import android.content.Context
import android.content.res.Resources
import android.graphics.Color
import android.graphics.drawable.ColorDrawable
import android.os.Bundle
import android.view.Gravity
import android.view.LayoutInflater
import android.view.Window
import android.view.WindowManager
import androidx.databinding.DataBindingUtil
import com.example.sportsplatform.R
import com.example.sportsplatform.databinding.ItemPopupLayoutBinding

interface PopupCallback {

    fun onYesButtonClick()

    fun onNoButtonClick()
}

class Popup(
    context: Context,
    val popupCallback: PopupCallback?
) : Dialog(context) {

    private lateinit var binding: ItemPopupLayoutBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        window?.requestFeature(Window.FEATURE_NO_TITLE)
        super.onCreate(savedInstanceState)

        binding = DataBindingUtil.inflate(
            LayoutInflater.from(context),
            R.layout.item_popup_layout,
            null,
            false
        )
        setContentView(binding.root)
        binding.executePendingBindings()

        setCancelable(true)

        window?.run {
            setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
            val width = (Resources.getSystem().displayMetrics.widthPixels * 0.8).toInt()
            setLayout(width, WindowManager.LayoutParams.WRAP_CONTENT)
            setGravity(Gravity.CENTER)
        }

        binding.btnNo.setOnClickListener {
            popupCallback?.onNoButtonClick()
            dismiss()
        }

        binding.btnYes.setOnClickListener {
            popupCallback?.onYesButtonClick()
            dismiss()
        }
    }
}