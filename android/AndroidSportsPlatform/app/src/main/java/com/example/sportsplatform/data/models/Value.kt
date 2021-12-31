package com.example.sportsplatform.data.models

import com.google.gson.annotations.SerializedName

data class Value(
    @SerializedName("@id") val id: Int?,
    val location: Location?,
    val maximumAttendeeCapacity: Int?,
    val name: String?,
    val sport: String?,
    val startDate: String?,
    val type: String?
)