package com.example.sportsplatform

interface AuthListener {
    fun onStarted()
    fun onSuccess()
    fun onFailure()
}