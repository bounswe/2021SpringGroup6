package com.example.sportsplatform.util

import java.text.SimpleDateFormat
import java.util.*

const val DATE_FORMAT = "dd.MM.yyyy HH:mm"
const val SIMPLE_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"

fun String?.convertDateFormat(): String {
    val simpleDateFormatter = SimpleDateFormat(Constants.SIMPLE_DATE_FORMAT, Locale.getDefault())
    val dateFormatter = SimpleDateFormat(Constants.DATE_FORMAT, Locale.getDefault())
    val date = this?.let {
        simpleDateFormatter.parse(it)
    }
    return date?.let { dateFormatter.format(it) } ?: ""
}

fun String?.convertDateFormatToDefault(): String {
    val simpleDateFormatter = SimpleDateFormat(SIMPLE_DATE_FORMAT, Locale.getDefault())
    val dateFormatter = SimpleDateFormat(DATE_FORMAT, Locale.getDefault())
    val date = this?.let {
        dateFormatter.parse(it)
    }
    return date?.let { simpleDateFormatter.format(it) } ?: ""
}

fun String?.initial(): String? {
    return this?.take(1)
}

fun String?.initial(): String? {
    return this?.take(1)
}

fun String?.initial(): String? {
    return this?.take(1)
}

fun String?.initial(): String? {
    return this?.take(1)
}