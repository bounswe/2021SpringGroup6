package com.example.sportsplatform.data.repository

import com.example.sportsplatform.data.api.EventApi
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.requests.EventRequest
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.data.models.responses.EventResponse
import retrofit2.Response

class EventRepository(private val api: EventApi) {
    suspend fun findEvent(eventRequest: EventRequest) : Response<EventResponse> {
        return api.searchEvent(eventRequest.event_id)
    }
    suspend fun findFilterEvents(eventFilterRequest: EventFilterRequest) : Response<EventFilterResponse> {
        return api.filterEvents(eventFilterRequest)
    }
}