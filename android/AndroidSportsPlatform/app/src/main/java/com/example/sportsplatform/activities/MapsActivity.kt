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

class MapsActivity : AppCompatActivity(), OnMapReadyCallback, GoogleMap.OnMapLongClickListener {

    companion object {
        fun openMaps(activity: AppCompatActivity) =
            activity.apply {
                val intent = Intent(this, MapsActivity::class.java)
                startActivity(intent)
            }
    }

    private lateinit var mMap: GoogleMap
    private lateinit var binding: ActivityMapsBinding

    private lateinit var sharedPreferences: SharedPreferences

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
        mMap.addMarker(MarkerOptions().position(bogaziciCoordinates).title("Marker in Bogazici Uni"))
        mMap.moveCamera(CameraUpdateFactory.newLatLng(bogaziciCoordinates))
        mMap.setOnMapLongClickListener(this)
    }

    override fun onMapLongClick(p0: LatLng?) {
        sharedPreferences.edit().putString(Constants.EVENT_LATITUDE, p0?.latitude?.toString()).apply()
        sharedPreferences.edit().putString(Constants.EVENT_LONGITUDE, p0?.longitude?.toString()).apply()
        finish()
    }
}