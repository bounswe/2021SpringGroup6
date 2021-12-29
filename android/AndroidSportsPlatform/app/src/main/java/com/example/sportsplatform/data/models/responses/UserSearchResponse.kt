package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.util.initial

data class UserSearchResponse(
    val context: String,
    val type : String,
    val total_items : Int,
    val items: List<UserResponse>
) {
    fun fetchUserInitials() = name.initial() + familyName.initial()
}
