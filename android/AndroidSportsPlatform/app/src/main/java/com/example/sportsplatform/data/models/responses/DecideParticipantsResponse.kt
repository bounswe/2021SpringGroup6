package com.example.sportsplatform.data.models.responses

data class DecideParticipantsResponse(
    val summary: String?,
    val type: String?,
    val items: List<Item>?
)

data class Item(
    val context: String?,
    val actor: Actor?,
    val `object`: Object?,
    val summary: String?,
    val type: String?
)

data class Actor(
    val id: Int?,
    val identifier: String?,
    val type: String?
)

data class Object(
    val id: Int?,
    val identifier: String?,
    val type: String?
)