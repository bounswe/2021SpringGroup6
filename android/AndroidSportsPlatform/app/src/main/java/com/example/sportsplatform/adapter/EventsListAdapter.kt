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

interface EventsClickListener {
    fun onEventsClickListener(eventResponse: EventResponse?)
}

class EventsListAdapter(
    private val itemClickListenerListener: EventsClickListener?
) :
    RecyclerView.Adapter<EventsListAdapter.MyViewHolder>() {

    var items = mutableListOf<EventResponse?>()
        set(value) {
            field.clear()
            field.addAll(value)
            notifyDataSetChanged()
        }

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
        val currentItem = items[position]
        with(holder.itemView.context) {
            holder.eventName.text = currentItem?.name
            holder.eventDescription.text = currentItem?.description
            holder.date.text = currentItem?.created_on.convertDateFormat()
            holder.maxAttendeeCap.text = this?.getString(
                R.string.eventMaxAttCapTitle,
                currentItem?.maximumAttendeeCapacity.toString()
            )
            holder.organizer.text =
                this?.getString(R.string.eventOrganizerTitle, currentItem?.organizer?.identifier)
            holder.duration.text =
                this?.getString(R.string.eventDurationTitle, currentItem?.duration.toString())
            holder.sport.text = this?.getString(R.string.eventSportTitle, currentItem?.sport)
            holder.container.setOnClickListener {
                currentItem?.let { item -> itemClickListenerListener?.onEventsClickListener(item) }
            }
        }
    }

    override fun getItemCount() = items.size
}