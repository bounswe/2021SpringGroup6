package com.example.sportsplatform.data.models.requests

data class DecideParticipantsRequest(
    val accept_user_id_list: List<Int?>,
    val reject_user_id_list: List<Int?>
)