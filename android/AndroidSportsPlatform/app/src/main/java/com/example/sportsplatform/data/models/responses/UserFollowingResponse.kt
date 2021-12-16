package com.example.sportsplatform.data.models.responses

import com.example.sportsplatform.data.models.responses.UserSearchResponse

data class UserFollowingResponse(
    val list_of_users : List<UserSearchResponse>
)
