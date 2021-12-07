package com.example.sportsplatform.data.models

data class UserRegisterRequest(
        val email : String,
        val password : String,
        val identifier : String,
        val name : String,
        val familyName : String,
        val birthDate : String,
        val gender : String,
        val sports : String
)
