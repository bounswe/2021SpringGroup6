package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.data.models.Location
import com.example.sportsplatform.data.models.User

data class UserResponse(
    val user_id: Int,
    val email: String,
    val email_visibility: String,
    val identifier: String,
    val name: Int,
    val name_visibility: String,
    val familyName: Int,
    val familyName_visibility: Int,
    val birthDate: String,
    val birthDate_visibility: String,
    val latitude: String,
    val longitude: String,
    val location_visibility: Location,
    val context: User,
    val id: List<User>,
    val type: List<User>,
    val knowsAbout: List<String>
)
