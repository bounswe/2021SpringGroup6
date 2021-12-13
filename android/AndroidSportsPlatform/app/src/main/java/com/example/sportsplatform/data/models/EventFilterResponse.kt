package com.example.sportsplatform.data.models

data class EventFilterResponse(
    val total_items: Int,
    val items: List<EventResponse>
)
