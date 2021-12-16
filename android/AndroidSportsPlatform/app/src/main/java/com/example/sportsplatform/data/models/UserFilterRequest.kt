package com.example.sportsplatform.data.models

data class UserFilterRequest(
    val nameContains: String,
    val city: String,
    val creator: String
)
