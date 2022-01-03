package com.example.sportsplatform.data.models.responses

import com.google.gson.annotations.SerializedName

data class CreateEventResponse(
    val context: String,
    @SerializedName("@id") val id: Int
)