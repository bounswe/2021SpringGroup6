package com.example.sportsplatform.data.models.responses

data class UserSearchResponse(
    val context: String,
    val type : String,
    val total_items : Int,
    val items: List<UserResponse>
)
