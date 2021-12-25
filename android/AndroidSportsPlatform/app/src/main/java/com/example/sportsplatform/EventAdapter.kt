package com.example.sportsplatform

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.data.models.responses.EventResponse
import kotlinx.android.synthetic.main.item_layout.view.*
import com.example.sportsplatform.util.convertDateFormat

class EventAdapter(private val itemList: List<EventResponse>) :
    RecyclerView.Adapter<EventAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val eventName: TextView = itemView.event_name
        val eventImageView: ImageView = itemView.image_view
        val eventTextView: TextView = itemView.event_desc
        val date: TextView = itemView.days
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView =
            LayoutInflater.from(parent.context).inflate(R.layout.item_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList[position]
        //holder.eventImageView.setImageResource(R.drawable.football)
        holder.eventTextView.text = currentItem.description
        holder.eventName.text = currentItem.name
        holder.date.text = currentItem.created_on.convertDateFormat()
    }

    override fun getItemCount() = itemList.size
}