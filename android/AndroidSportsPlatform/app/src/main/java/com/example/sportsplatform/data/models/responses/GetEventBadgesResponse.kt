package com.example.sportsplatform.data.models.responses

import com.google.gson.annotations.SerializedName

data class GetEventBadgesResponse(
    @SerializedName("@context") val context: String?,
    @SerializedName("@id") val id: Int?,
    val additionalProperty: AdditionalPropertyForEventBadges?
)

data class AdditionalPropertyForEventBadges(
    @SerializedName("@type") val type: String?,
    val name: String?,
    val value: List<ValueForEventBadges>?
)

data class ValueForEventBadges(
    @SerializedName("@context") val context: String?,
    val name: String?
)