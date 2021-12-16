package com.example.sportsplatform.data.models

data class EventFilterResponse(
    val context: String,
    val type: String,
    val total_items: Int,
    val items: List<EventResponse>
)
