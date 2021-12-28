package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.responses.EventResponse
import kotlinx.android.synthetic.main.item_users_participating_events_layout.view.*

class UsersParticipatingEventsAdapter(private val itemList: List<EventResponse>?) :
    RecyclerView.Adapter<UsersParticipatingEventsAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val eventTitle: TextView = itemView.twName
        val eventDescription: TextView = itemView.twDescription
        val eventStartDate: TextView = itemView.twStartDate
        val maxAttendeeCapacity: TextView = itemView.twMaxAttendeeCapacity
        val organizer: TextView = itemView.twOrganizer
        val duration: TextView = itemView.twDuration
        val sport: TextView = itemView.twSport
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_users_participating_events_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList?.get(position)
        holder.eventTitle.text = currentItem?.name
        holder.eventDescription.text = currentItem?.description
        holder.eventStartDate.text = currentItem?.startDate
        holder.maxAttendeeCapacity.text = currentItem?.maximumAttendeeCapacity?.toString()
        holder.organizer.text = currentItem?.organizer?.context
        holder.duration.text = currentItem?.duration?.toString()
        holder.sport.text = currentItem?.sport
    }

    override fun getItemCount(): Int = itemList?.size ?: 0
}