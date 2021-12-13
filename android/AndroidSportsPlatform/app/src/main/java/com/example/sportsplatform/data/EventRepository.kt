package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.EventRequest
import com.example.sportsplatform.data.models.EventResponse
import com.example.sportsplatform.data.models.TokenResponse
import com.example.sportsplatform.data.models.UserRequest
import retrofit2.Response

class EventRepository(private val api: EventApi) {
    suspend fun findEvent(eventRequest: EventRequest) : Response<EventResponse> {
        return api.searchEvent(eventRequest.event_id)
    }
}