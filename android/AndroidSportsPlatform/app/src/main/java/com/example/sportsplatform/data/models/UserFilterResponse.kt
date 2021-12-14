package com.example.sportsplatform.data.models

data class UserFilterResponse(
    val total_items: Int,
    val items: List<UserSearchResponse>
)
