package com.example.sportsplatform.data.models.requests

import android.os.Parcelable
import kotlinx.android.parcel.Parcelize

@Parcelize
data class UserSearchRequest(
    // val name: String
    // val familyName: String,
    val identifier: String? = null
) : Parcelable
