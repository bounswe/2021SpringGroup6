package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.data.models.Badge
import com.google.gson.annotations.SerializedName

data class GetBadgeResponse(
    @SerializedName("@context") val context: String?,
    @SerializedName("@id") val id: Int?,
    val additionalProperty: List<Badge>?
)
