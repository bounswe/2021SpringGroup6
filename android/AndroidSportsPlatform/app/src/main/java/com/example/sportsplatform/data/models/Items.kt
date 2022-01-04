package com.example.sportsplatform.data.models

import com.google.gson.annotations.SerializedName

data class Items(
    val actor: Actor,
    @SerializedName("@context")
    val context: String?,
    @SerializedName("object")
    val objectX: Object?,
    val summary: String?,
    val type: String?
)