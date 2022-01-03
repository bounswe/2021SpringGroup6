package com.example.sportsplatform.data.models

import com.google.gson.annotations.SerializedName

data class ValueBadge(
    @SerializedName("@context") val context: String?,
    val name: String?,
    val additionalProperty: AdditionalPropertyBadge?,
)
