package com.example.sportsplatform.data.repository

import com.example.sportsplatform.data.api.SportApi
import com.example.sportsplatform.data.models.responses.SportsResponse
import retrofit2.Response

class SportRepository(private val api: SportApi) {
    suspend fun getSports() : Response<SportsResponse> {
        return api.getSports()
    }
}