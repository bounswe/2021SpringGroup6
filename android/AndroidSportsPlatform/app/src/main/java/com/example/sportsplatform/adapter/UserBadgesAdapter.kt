package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.AdditionalProperty
import kotlinx.android.synthetic.main.item_badge.view.*

class UserBadgesAdapter(private val itemList: List<AdditionalProperty>) :
    RecyclerView.Adapter<UserBadgesAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val badgeName: TextView = itemView.twBadgeName
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView =
            LayoutInflater.from(parent.context).inflate(R.layout.item_badge, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList[position]
        holder.badgeName.text = currentItem.value.toString()
    }

    override fun getItemCount() = itemList.size
}