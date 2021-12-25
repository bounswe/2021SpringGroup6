package com.example.sportsplatform.util

import com.example.sportsplatform.util.Constants.DATE_FORMAT
import com.example.sportsplatform.util.Constants.SIMPLE_DATE_FORMAT
import java.text.SimpleDateFormat
import java.util.*

fun String?.convertDateFormat(): String {
    val simpleDateFormatter = SimpleDateFormat(SIMPLE_DATE_FORMAT, Locale.getDefault())
    val dateFormatter = SimpleDateFormat(DATE_FORMAT, Locale.getDefault())
    val date = this?.let {
        simpleDateFormatter.parse(it)
    }
    return date?.let { dateFormatter.format(it) } ?: ""
}