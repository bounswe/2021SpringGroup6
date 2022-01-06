package com.example.sportsplatform.data.models.responses

import com.google.gson.annotations.SerializedName

data class GetBadgeResponse(
    @SerializedName("@context") val context: String?,
    @SerializedName("@id") val id: Int?,
    val additionalProperty: List<Badges>?
)
data class Badges(
    @SerializedName("@type") val type: String?,
    val name: String?,
    val value: List<ValueBadge>?
)
data class ValueBadge(
    @SerializedName("@context") val context: String?,
    val name: String?,
    val additionalProperty: AdditionalPropertyBadge?,
    val sport: String?
)
data class AdditionalPropertyBadge(
    @SerializedName("@type") val type: String?,
    val name: String?,
    val value: AdditionalPropertyBadgeGivenBy?
)
data class AdditionalPropertyBadgeGivenBy(
    @SerializedName("@context") val context: String?,
    @SerializedName("@id") val id: Int?
)