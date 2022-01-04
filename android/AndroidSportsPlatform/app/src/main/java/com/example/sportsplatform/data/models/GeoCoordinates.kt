package com.example.sportsplatform.data.models

data class GeoCoordinates(
    val type: String?,
    val latitude: Double?,
    val longitude: Double?
){
    fun getLatLngTogether() = "lat: $latitude  long: $longitude"
}

