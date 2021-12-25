package com.example.sportsplatform

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.data.models.responses.EventResponse
import kotlinx.android.synthetic.main.item_layout.view.*
import java.time.Instant
import java.time.ZoneId

class EventAdapter(private val itemList: List<EventResponse>) : RecyclerView.Adapter<EventAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val eventName: TextView = itemView.twName
        //val eventImageView: ImageView = itemView.image_view
        val eventTextView: TextView = itemView.twDescription
        val date: TextView = itemView.twStartDate
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) : MyViewHolder {
        val itemView = LayoutInflater.from(parent.context).inflate(R.layout.item_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList[position]
        //holder.eventImageView.setImageResource(R.drawable.football)
        holder.eventTextView.text = currentItem.description
        holder.eventName.text = currentItem.name
        holder.date.text = getDateTime(currentItem.created_on)
    }

    override fun getItemCount() = itemList.size

    private fun getDateTime(s: String): String {
        val datetime = Instant.ofEpochSecond(s.toLong())
            .atZone(ZoneId.systemDefault())
            .toLocalDateTime()

        val str: String = datetime.toString()

        return str.substring(0, 10)
    }
}