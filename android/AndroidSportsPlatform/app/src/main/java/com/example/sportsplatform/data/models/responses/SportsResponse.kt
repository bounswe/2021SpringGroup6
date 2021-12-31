package com.example.sportsplatform.data.models.responses

class SportsResponse : ArrayList<SportsResponseItem>()

data class SportsResponseItem(
    val name: String?
)