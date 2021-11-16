package com.example.sportsplatform.data.models

import java.util.*

data class SignUpRequest(
    val email : String,
    val password : String,
    val identifier : String,
    val name : String,
    val familyName : String,
    val birthDate : String,
    val gender : String,
    val sports : List<Dictionary<UserRequest, UserResponse>>
)
