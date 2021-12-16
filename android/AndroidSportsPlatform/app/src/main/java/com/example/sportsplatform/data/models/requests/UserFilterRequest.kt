package com.example.sportsplatform.data.models.requests

data class UserFilterRequest(
    val nameContains: String,
    val city: String,
    val creator: String
)
