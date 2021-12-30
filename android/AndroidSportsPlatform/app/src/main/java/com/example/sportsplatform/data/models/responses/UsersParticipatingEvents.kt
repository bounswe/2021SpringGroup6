package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.data.models.AdditionalProperty

data class UsersParticipatingEvents(
    val context: String?,
    val id: Int?,
    val additionalProperty: AdditionalProperty?,
    val identifier: String?
)