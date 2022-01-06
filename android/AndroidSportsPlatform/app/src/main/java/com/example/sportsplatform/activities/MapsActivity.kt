package com.example.sportsplatform.activities

import android.content.Intent
import android.content.SharedPreferences
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.sportsplatform.R
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import com.example.sportsplatform.databinding.ActivityMapsBinding
import com.example.sportsplatform.util.Constants
import com.google.android.gms.maps.model.BitmapDescriptorFactory
import com.google.gson.Gson

class MapsActivity : AppCompatActivity(), OnMapReadyCallback, GoogleMap.OnMapLongClickListener {

    companion object {
        private const val IS_FOR_EVENT_SEARCH = "is_for_event_search"
        private const val LATITUDE = "latitude"
        private const val LONGITUDE = "longitude"
        fun openMaps(
            activity: AppCompatActivity,
            isForEventSearch: String = "",
            lat: Double? = null,
            long: Double? = null
        ) =
            activity.apply {
                val intent = Intent(this, MapsActivity::class.java)
                intent.putExtra(IS_FOR_EVENT_SEARCH, isForEventSearch)
                intent.putExtra(LATITUDE, lat)
                intent.putExtra(LONGITUDE, long)
                startActivity(intent)
            }
    }

    private lateinit var mMap: GoogleMap
    private lateinit var binding: ActivityMapsBinding

    private lateinit var sharedPreferences: SharedPreferences

    private var userAddedMarkerCount = 0
    private var listOfMarkerPositions = mutableListOf<LatLng>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMapsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        val mapFragment = supportFragmentManager
            .findFragmentById(R.id.map) as SupportMapFragment
        mapFragment.getMapAsync(this)

        sharedPreferences = getSharedPreferences(Constants.CUSTOM_SHARED_PREFERENCES, MODE_PRIVATE)
    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    override fun onMapReady(googleMap: GoogleMap) {
        mMap = googleMap

        // Add a marker in Bogazici Uni and move the camera
        val bogaziciCoordinates = LatLng(41.084, 29.055)
        mMap.addMarker(
            MarkerOptions().position(bogaziciCoordinates).title("Marker in Bogazici Uni")
        )

        if (getIsForSearchEvent() == "fromEventDetail") {
            val latLng = LatLng(
                intent.getDoubleExtra(LATITUDE, 0.0), intent.getDoubleExtra(LONGITUDE, 0.0)
            )
            addMarker(latLng)
        }

        mMap.moveCamera(CameraUpdateFactory.newLatLng(bogaziciCoordinates))
        mMap.setOnMapLongClickListener(this)
    }

    override fun onMapLongClick(p0: LatLng?) {
        when (getIsForSearchEvent()) {
            "fromSearch" -> {
                if (userAddedMarkerCount < 1) {
                    addMarker(p0)
                } else {
                    p0?.let { listOfMarkerPositions.add(it) }
                    putMarkerPositionsToSharedPreferences()
                    finish()
                }
            }

            "fromCreateEvent" -> {
                sharedPreferences.edit()
                    .putString(Constants.EVENT_LATITUDE, p0?.latitude?.toString())
                    .apply()
                sharedPreferences.edit()
                    .putString(Constants.EVENT_LONGITUDE, p0?.longitude?.toString())
                    .apply()
                finish()
            }

            else -> {
            }
        }
    }

    private fun getIsForSearchEvent(): String? = intent.getStringExtra(IS_FOR_EVENT_SEARCH)

    private fun addMarker(p0: LatLng?) {
        val markerOptions = p0?.let {
            listOfMarkerPositions.add(it)
            MarkerOptions().position(it)
        }.also {
            it?.icon(
                BitmapDescriptorFactory
                    .defaultMarker(BitmapDescriptorFactory.HUE_AZURE)
            )
            mMap.addMarker(it)
            userAddedMarkerCount += 1
        }
    }

    private fun putMarkerPositionsToSharedPreferences() {
        val gson = Gson()
        val json = gson.toJson(listOfMarkerPositions)
        sharedPreferences.edit().putString("listOfMarkerPositions", json).apply()
    }
}