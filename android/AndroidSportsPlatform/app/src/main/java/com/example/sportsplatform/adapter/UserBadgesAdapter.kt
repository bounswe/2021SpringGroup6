package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.Badge
import com.example.sportsplatform.data.models.responses.GetBadgeResponse
import kotlinx.android.synthetic.main.item_badge.view.*

class UserBadgesAdapter(
    private val itemList: List<Badge>?
) :
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
        val currentItem = itemList?.get(position)
        holder.badgeName.text = currentItem?.name
    }

    override fun getItemCount() = itemList?.size ?: 0
}