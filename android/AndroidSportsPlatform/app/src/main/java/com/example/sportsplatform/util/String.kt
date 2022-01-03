package com.example.sportsplatform.util

import java.text.SimpleDateFormat
import java.time.Instant
import java.util.*

const val DATE_FORMAT = "dd.MM.yyyy HH:mm"
const val SIMPLE_DATE_FORMAT = "yyyy-MM-dd'T'HH:mm:ss'Z'"
const val SIMPLE_DATE_FORMAT_WITHOUT_SECONDS = "yyyy-MM-dd'T'HH:mm"

fun String?.convertDateFormat(): String {
    val simpleDateFormatter = SimpleDateFormat(Constants.SIMPLE_DATE_FORMAT, Locale.getDefault())
    val dateFormatter = SimpleDateFormat(Constants.DATE_FORMAT, Locale.getDefault())
    return try {
        val date = this?.let {
            simpleDateFormatter.parse(it)
        }
        date?.let { dateFormatter.format(it) } ?: ""
    } catch (e: Exception) {
        "01.01.2022 00:00"
    }
}

fun String?.convertDateFormatToDefault(): String {
    val simpleDateFormatter = SimpleDateFormat(SIMPLE_DATE_FORMAT, Locale.getDefault())
    val dateFormatter = SimpleDateFormat(DATE_FORMAT, Locale.getDefault())
    return try {
        val date = this?.let {
            dateFormatter.parse(it)
        }
        date?.let { simpleDateFormatter.format(it) } ?: ""
    } catch (e: Exception) {
        "01.01.2022 00:00"
    }
}

fun String?.convertDateWithoutSecondsToDefault(): String {
    val instant: Instant = Instant.parse(this)
    val simpleDateFormatter =
        SimpleDateFormat(SIMPLE_DATE_FORMAT_WITHOUT_SECONDS, Locale.getDefault())
    val dateFormatter = SimpleDateFormat(DATE_FORMAT, Locale.getDefault())
    return try {
        val date = simpleDateFormatter.parse(instant.toString())
        date?.let { dateFormatter.format(it) } ?: ""
    } catch (e: Exception) {
        "01.01.2022 00:00"
    }
}

fun String?.initial(): String? {
    return this?.take(1)
}
