package com.example.sportsplatform.data.models.requests

data class CreateEventRequest(
    val name: String,
    val sport: String,
    val description: String?,
    val startDate: String,
    val latitude: Double,
    val longitude: Double,
    val minimumAttendeeCapacity: Int,
    val maximumAttendeeCapacity: Int,
    val maxSpectatorCapacity: Int,
    val minSkillLevel: Int,
    val maxSkillLevel: Int,
    val acceptWithoutApproval: Boolean,
    val duration: Int
)