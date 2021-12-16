package com.example.sportsplatform.data.models.responses

data class UserSearchResponse(
    val name: String,
    val familyName : String,
    val birthDate : String,
    val gender : String,
    val created_on: Int
)
