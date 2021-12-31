package com.example.sportsplatform.data.models.requests

data class EventFilterRequest(
    val nameContains: String? = null,
    val latitudeBetweenStart: Double? = null,
    val latitudeBetweenEnd: Double? = null,
    val longitudeBetweenStart: Double? = null,
    val longitudeBetweenEnd: Double? = null
    //val city: String,
    //val creator: String
)
