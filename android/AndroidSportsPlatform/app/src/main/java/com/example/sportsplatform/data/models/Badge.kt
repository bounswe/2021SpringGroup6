package com.example.sportsplatform.data.models

import com.google.gson.annotations.SerializedName

data class Badge(
    @SerializedName("@type") val type: String?,
    val name: String?,
    val value: List<ValueBadge>?
)
