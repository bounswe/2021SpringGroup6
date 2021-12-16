package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.*
import retrofit2.Response

class EventRepository(private val api: EventApi) {
    suspend fun findEvent(eventRequest: EventRequest) : Response<EventResponse> {
        return api.searchEvent(eventRequest.event_id)
    }
    suspend fun findFilterEvents(eventFilterRequest: EventFilterRequest) : Response<EventFilterResponse> {
        return api.filterEvents(eventFilterRequest)
    }
}