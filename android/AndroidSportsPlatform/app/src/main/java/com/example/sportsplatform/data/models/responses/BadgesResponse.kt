package com.example.sportsplatform.data.models.responses

import com.google.gson.annotations.SerializedName

data class BadgesResponse(
    val badges: List<Badge>?
)

data class Badge(
    @SerializedName("@context") val context: String?,
    val name: String?
) {
    fun toValueBadge() = ValueForEventBadges(
        name = name,
        context = null
    )
}