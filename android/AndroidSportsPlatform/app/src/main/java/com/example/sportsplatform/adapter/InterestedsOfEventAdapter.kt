package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.responses.Value
import kotlinx.android.synthetic.main.item_interesteds_of_event_layout.view.*

interface InterestedsDecisionClick {
    fun onAcceptClick(user: Value?)
    fun onDeclineClick(user: Value?)
}

class InterestedsOfEventAdapter(
    private val itemClickListener: InterestedsDecisionClick?
) : RecyclerView.Adapter<InterestedsOfEventAdapter.MyViewHolder>() {

    var items = mutableListOf<Value?>()
        set(value) {
            field.clear()
            field.addAll(value)
            notifyDataSetChanged()
        }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView = LayoutInflater.from(parent.context).inflate(R.layout.item_interesteds_of_event_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = items[position]
        holder.interestedName.text = currentItem?.identifier
        holder.ivCheck.setOnClickListener {
            deleteItem(position)
            currentItem?.let { item -> itemClickListener?.onAcceptClick(item) }
        }
        holder.ivDecline.setOnClickListener {
            deleteItem(position)
            currentItem?.let { item -> itemClickListener?.onDeclineClick(item) }
        }
    }

    override fun getItemCount(): Int = items.size

    private fun deleteItem(index: Int){
        items.removeAt(index)
        notifyDataSetChanged()
    }

    inner class MyViewHolder(itemView: View): RecyclerView.ViewHolder(itemView) {
        val interestedName: TextView = itemView.twInterestedName
        val ivCheck: ImageView = itemView.ivCheck
        val ivDecline: ImageView = itemView.ivDecline
    }
}