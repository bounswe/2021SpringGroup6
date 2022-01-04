package com.example.sportsplatform.data.models.responses

data class UserFilterResponse(
    val total_items: Int,
    val items: List<UserSearchResponse>
)
