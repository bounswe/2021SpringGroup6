package com.example.sportsplatform.data.repository

import com.example.sportsplatform.data.api.BadgeApi
import com.example.sportsplatform.data.models.requests.AddBadgeToEventRequest
import com.example.sportsplatform.data.models.responses.BadgesResponse
import retrofit2.Response

class BadgeRepository(private val api: BadgeApi) {
    suspend fun getBadges(): Response<BadgesResponse?> {
        return api.getBadges()
    }
    suspend fun addBadgeToEvent(
        token: String?,
        eventId: Int?,
        request: AddBadgeToEventRequest
    ): Response<Void> {
        return api.addBadgeToEvent(
            token = token,
            eventId = eventId,
            request = request
        )
    }
}