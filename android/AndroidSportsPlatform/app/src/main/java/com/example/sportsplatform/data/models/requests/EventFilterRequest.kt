package com.example.sportsplatform.data.models.requests

import android.os.Parcelable
import kotlinx.android.parcel.Parcelize

@Parcelize
data class EventFilterRequest(
    val nameContains: String? = null,
    val latitudeBetweenStart: Double? = null,
    val latitudeBetweenEnd: Double? = null,
    val longitudeBetweenStart: Double? = null,
    val longitudeBetweenEnd: Double? = null,
    val sport: String? = null,
    val city: String? = null,
    val country: String? = null,
    val skillLevels: List<Int>? = null
    //val city: String,
    //val creator: String
) : Parcelable
