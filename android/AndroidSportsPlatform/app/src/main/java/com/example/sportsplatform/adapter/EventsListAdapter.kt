package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.responses.EventResponse
import com.example.sportsplatform.util.convertDateFormat
import kotlinx.android.synthetic.main.item_event_layout.view.*

interface UsersParticipatingEventsClick {
    fun onUsersParticipatingEventsClicked(eventResponse: EventResponse)
}

class EventsListAdapter(
    private val itemList: List<EventResponse>?,
    private val itemClickListener: UsersParticipatingEventsClick?
) :
    RecyclerView.Adapter<EventsListAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val container: ConstraintLayout = itemView.clContainer
        val eventName: TextView = itemView.twName
        val eventDescription: TextView = itemView.twDescription
        val date: TextView = itemView.twStartDate
        val maxAttendeeCap: TextView = itemView.twMaxAttendeeCapacity
        val organizer: TextView = itemView.twOrganizer
        val duration: TextView = itemView.twDuration
        val sport: TextView = itemView.twSport
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView =
            LayoutInflater.from(parent.context).inflate(R.layout.item_event_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList?.get(position)
        holder.eventName.text = currentItem?.name
        holder.eventDescription.text = currentItem?.description
        holder.date.text = currentItem?.created_on.convertDateFormat()
        holder.maxAttendeeCap.text = currentItem?.maximumAttendeeCapacity.toString()
        holder.organizer.text = currentItem?.organizer?.identifier
        holder.duration.text = currentItem?.duration.toString()
        holder.sport.text = currentItem?.sport
        holder.container.setOnClickListener {
            currentItem?.let { item -> itemClickListener?.onUsersParticipatingEventsClicked(item) }
        }
    }

    override fun getItemCount() = itemList?.size ?: 0
}