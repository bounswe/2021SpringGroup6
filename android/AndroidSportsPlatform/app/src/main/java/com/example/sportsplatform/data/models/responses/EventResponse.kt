package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.data.models.Location
import com.example.sportsplatform.data.models.User
import com.example.sportsplatform.util.convertDateWithoutSecondsToDefault

data class EventResponse(
    val event_id: Int,
    val name: String,
    val description: String,
    val startDate: String,
    val maximumAttendeeCapacity: Int,
    val minSkillLevel: String,
    val maxSkillLevel: Int,
    val duration: Int,
    val created_on: String,
    val sport: String,
    val context: String,
    val type: String,
    val location: Location,
    val organizer: User,
    val attendee: List<User>,
    val audience: List<User>

) {
    var convertedDate: String? = null
    fun getFormattedDate() {
        convertedDate = startDate.convertDateWithoutSecondsToDefault()
    }
}
