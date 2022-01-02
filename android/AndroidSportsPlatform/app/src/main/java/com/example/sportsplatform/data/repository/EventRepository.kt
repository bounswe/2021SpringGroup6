package com.example.sportsplatform.data.repository

import com.example.sportsplatform.data.api.EventApi
import com.example.sportsplatform.data.models.requests.CreateEventRequest
import com.example.sportsplatform.data.models.requests.EventFilterRequest
import com.example.sportsplatform.data.models.requests.EventRequest
import com.example.sportsplatform.data.models.responses.CreateEventResponse
import com.example.sportsplatform.data.models.responses.EventFilterResponse
import com.example.sportsplatform.data.models.responses.EventResponse
import com.example.sportsplatform.data.models.responses.GetInterestedsOfEventResponse
import retrofit2.Response

class EventRepository(private val api: EventApi) {
    suspend fun findEvent(eventRequest: EventRequest) : Response<EventResponse> {
        return api.searchEvent(eventRequest.event_id)
    }
    suspend fun findFilterEvents(eventFilterRequest: EventFilterRequest) : Response<EventFilterResponse> {
        return api.filterEvents(eventFilterRequest)
    }
    suspend fun createNewEvent(token: String, createEventRequest: CreateEventRequest) : Response<CreateEventResponse> {
        return api.createEvent(token, createEventRequest)
    }
    suspend fun sendInterestToEvent(token: String, eventId: Int?): Response<Unit> {
        return api.sendInterestToEvent(token, eventId)
    }
    suspend fun participateAsSpectatorToEvent(token: String, eventId: Int?): Response<Unit> {
        return api.participateAsSpectatorToEvent(token, eventId)
    }
    suspend fun deleteSpectatorRequest(token: String, eventId: Int?): Response<Unit> {
        return api.deleteSpectatorRequest(token, eventId)
    }
    suspend fun getInterestedsOfEvent(eventId: Int?): Response<GetInterestedsOfEventResponse> {
        return api.getInterestedsOfEvent(eventId)
    }
}