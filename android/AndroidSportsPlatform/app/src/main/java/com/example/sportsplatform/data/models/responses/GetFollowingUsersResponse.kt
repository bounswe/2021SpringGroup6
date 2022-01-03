package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.data.models.Items
import com.google.gson.annotations.SerializedName

data class GetFollowingUsersResponse(
    @SerializedName("@context")
    val context: String?,
    val items: List<Items>?,
    val summary: String?,
    @SerializedName("total_items")
    val totalItems: Int?,
    val type: String?
)