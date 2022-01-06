package com.example.sportsplatform.data.models.requests

data class UserUpdateRequest(
    val email: String?,
    val name: String?,
    val familyName: String?,
    val birthDate: String?,
    val gender: String?,
    val sports: List<String>?
)
