package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.data.models.AdditionalProperty

data class UserResponse(
    val user_id: Int,
    val email: String,
    val email_visibility: Boolean,
    val identifier: String,
    val name: String,
    val name_visibility: Boolean,
    val familyName: String,
    val familyName_visibility: Boolean,
    val birthDate: String,
    val birthDate_visibility: Boolean,
    val latitude: Float,
    val longitude: Float,
    val location_visibility: Boolean,
    val context: String,
    val id: Int,
    val type: String,
    val knowsAbout: List<AdditionalProperty>
)
