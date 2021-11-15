package com.example.sportsplatform.data

import com.example.sportsplatform.data.models.TokenResponse
import org.json.JSONObject
import retrofit2.Response

class Repository(private val api: UserApi) {
    suspend fun findUser(identifier: String, password: String) : Response<TokenResponse> {
        val jsonObject = JSONObject()
        jsonObject.put("identifier", identifier)
        jsonObject.put("password", password)
        return api.searchUser(jsonObject.toString())
    }
}