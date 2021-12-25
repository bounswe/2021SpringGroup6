package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.responses.UserSearchResponse
import kotlinx.android.synthetic.main.item_searched_user_layout.view.*

class UserSearchAdapter(private val itemList: List<UserSearchResponse>?) :
    RecyclerView.Adapter<UserSearchAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val userName: TextView = itemView.twUserName
        val userDescription: TextView = itemView.twUserDescription
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_searched_user_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList?.get(position)
        holder.userName.text = currentItem?.name
        holder.userDescription.text = currentItem?.name
    }

    override fun getItemCount(): Int = itemList?.size ?: 0
}