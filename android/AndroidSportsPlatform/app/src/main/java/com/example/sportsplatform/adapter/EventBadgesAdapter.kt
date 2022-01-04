package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.responses.ValueForEventBadges
import kotlinx.android.synthetic.main.item_event_badges_layout.view.*

interface EventBadgesClickListener {
    fun onEventBadgesClicked(badgeResponse: ValueForEventBadges?)
}

class EventBadgesAdapter(
    private val itemClickListener: EventBadgesClickListener? = null
) : RecyclerView.Adapter<EventBadgesAdapter.MyViewHolder>() {

    var items = mutableListOf<ValueForEventBadges?>()
        set(value) {
            field.clear()
            field.addAll(value)
            notifyDataSetChanged()
        }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_event_badges_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = items[position]
        holder.badgeName.text = currentItem?.name
        holder.container.setOnClickListener {
            itemClickListener?.let {
                currentItem?.let { item -> it.onEventBadgesClicked(item) }
                holder.ivCheck.visibility = View.VISIBLE
            }
        }
    }

    override fun getItemCount(): Int = items.size

    inner class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val container: ConstraintLayout = itemView.clContainer
        val badgeName: TextView = itemView.twBadgeName
        val ivCheck: ImageView = itemView.ivCheck
    }
}