package com.example.sportsplatform.data.models.responses

data class TokenResponse(
    val token: String,
    val user_id : Int
) {
    var userId: Int? = null
    fun fetchUserId() {
        userId = user_id
    }
}
