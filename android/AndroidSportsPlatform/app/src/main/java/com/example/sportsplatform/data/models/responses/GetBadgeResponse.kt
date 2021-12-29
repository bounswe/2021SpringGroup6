package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.data.models.AdditionalProperty

data class GetBadgeResponse(
    val context: String,
    val id: Int,
    val additionalProperty: List<AdditionalProperty>
)
