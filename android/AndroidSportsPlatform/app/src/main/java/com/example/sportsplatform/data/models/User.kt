package com.example.sportsplatform.data.models

import com.google.gson.annotations.SerializedName

data class User(
    val context: String,
    val type: String,
    @SerializedName("@id") val id: Int,
    val identifier: String
)
