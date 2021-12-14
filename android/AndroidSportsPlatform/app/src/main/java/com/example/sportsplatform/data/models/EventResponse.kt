package com.example.sportsplatform.data.models

data class EventResponse(
        val event_id: Int,
        val name: String,
        val description: String,
        val startDate: String,
        val maximumAttendeeCapacity: Int,
        val minSkillLevel: String,
        val maxSkillLevel: Int,
        val duration: Int,
        val created_on: Int,
        val sport: String,
        val context: String,
        val type: Int,
        val location: Location,
        val address: String,
        val organizer: User,
        val attendee: List<User>,
        val audience: List<User>,
        val additionalProperty: List<AdditionalProperty>

)
