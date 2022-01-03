package com.example.sportsplatform.data.models.responses

import com.google.gson.annotations.SerializedName

data class GetInterestedsOfEventResponse(
    val id: Int?,
    val additionalProperty: AdditionalProperty?
)

data class AdditionalProperty(
    val name: String?,
    val value: List<Value>?
)

data class Value(
    val context: String?,
    @SerializedName("@id") val id: Int?,
    val identifier: String?
)