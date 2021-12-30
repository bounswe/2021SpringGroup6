package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.Value
import com.example.sportsplatform.util.convertDateWithoutSecondsToDefault
import kotlinx.android.synthetic.main.item_users_participating_events.view.*

interface UsersParticipatingEventsClick {
    fun onUsersParticipatingEventsClicked(eventResponse: Value?)
}

class UsersParticipatingEventsAdapter(
    private val itemList: List<Value>?,
    private val itemClickListenerListener: UsersParticipatingEventsClick?
) :
    RecyclerView.Adapter<UsersParticipatingEventsAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val container: ConstraintLayout = itemView.clContainer
        val eventName: TextView = itemView.twName
        val eventAddress: TextView = itemView.twAddress
        val date: TextView = itemView.twStartDate
        val maxAttendeeCap: TextView = itemView.twMaxAttendeeCapacity
        val sport: TextView = itemView.twSport
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView =
            LayoutInflater.from(parent.context).inflate(R.layout.item_users_participating_events, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList?.get(position)
        holder.eventName.text = currentItem?.name
        holder.eventAddress.text = currentItem?.location?.address
        holder.date.text = currentItem?.startDate?.convertDateWithoutSecondsToDefault()
        holder.maxAttendeeCap.text = currentItem?.maximumAttendeeCapacity.toString()
        holder.sport.text = currentItem?.sport
        holder.container.setOnClickListener {
            currentItem?.let { item -> itemClickListenerListener?.onUsersParticipatingEventsClicked(item) }
        }
    }

    override fun getItemCount() = itemList?.size ?: 0
}