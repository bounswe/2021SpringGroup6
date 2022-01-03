package com.example.sportsplatform.data.models


import com.google.gson.annotations.SerializedName

data class Actor(
    @SerializedName("@id")
    val id: Int?,
    val identifier: String?,
    val type: String?
)