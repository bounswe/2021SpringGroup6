package com.example.sportsplatform.data.api

import com.example.sportsplatform.data.models.*
import com.example.sportsplatform.data.models.requests.*
import com.example.sportsplatform.data.models.responses.*
import com.example.sportsplatform.util.ErrorInterceptor
import com.jakewharton.retrofit2.adapter.kotlin.coroutines.CoroutineCallAdapterFactory
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*

interface UserApi {

    @POST("users/login")
    suspend fun loginUser(
        @Body userRequest: UserRequest
    ): Response<TokenResponse>

    @POST("users/logout")
    suspend fun logoutUser(
        @Header("Authorization") token: String
    ): Response<ResponseMessage>

    @POST("users/{user_id}/badges")
    suspend fun addUserBadge(
        @Header("Authorization") token: String,
        @Path("user_id") userId: Int,
        @Body addBadgeRequest: AddBadgeRequest
    ): Response<Void>

    @GET("users/{user_id}/badges")
    suspend fun getUsersBadges(
        @Path("user_id") userId: Int,
    ): Response<GetBadgeResponse>

    @POST("users/searches")
    suspend fun filterUsers(
        @Body userSearchRequest: UserSearchRequest
    ): Response<UserSearchResponse>

    @POST("users")
    suspend fun registerUser(
        @Body userRegisterRequest: UserRegisterRequest
    ): Response<Void>

    @GET("users/{user_id}")
    suspend fun searchUser(
        @Header("Authorization") token: String,
        @Path("user_id") userId: Int
    ): Response<UserResponse>

    @PUT("users/{user_id}")
    suspend fun updateUser(
        @Header("Authorization") token: String,
        @Path("user_id") userId: Int,
        @Body userUpdateRequest: UserUpdateRequest
    ): Response<Void>

    @GET("/users/{user_id}/following")
    suspend fun searchFollowingProfile(
        @Header("Authorization") token: String,
        @Path("user_id") userId: Int
    ): Response<GetFollowingUsersResponse>

    @POST("/users/{user_id}/following")
    suspend fun followProfile(
        @Header("Authorization") token: String,
        @Path("user_id") followedUserId: Int,
        @Body userFollowingRequest: UserFollowingRequest
    ): Response<Void>

    @GET("/users/{user_id}/participating")
    suspend fun getUsersParticipatingEvents(
        @Header("Authorization") token: String,
        @Path("user_id") userId: Int
    ): Response<UsersParticipatingEvents>

    companion object {
        operator fun invoke(): UserApi {
            val requestInterceptor = Interceptor { chain ->
                val url = chain.request()
                    .url()
                    .newBuilder()
                    .build()
                val request = chain.request()
                    .newBuilder()
                    .url(url)
                    .build()

                return@Interceptor chain.proceed(request)
            }

            val errorInterceptor = ErrorInterceptor()

            val okHttpClient = OkHttpClient.Builder()
                .addInterceptor(requestInterceptor)
                .addInterceptor(errorInterceptor)
                .build()

            return Retrofit.Builder()
                .client(okHttpClient)
                .baseUrl("http://3.20.232.108:8080")
                .addCallAdapterFactory(CoroutineCallAdapterFactory())
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(UserApi::class.java)
        }
    }

}