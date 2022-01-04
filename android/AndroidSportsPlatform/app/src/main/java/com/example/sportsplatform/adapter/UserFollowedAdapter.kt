package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.R
import com.example.sportsplatform.data.models.Items
import kotlinx.android.synthetic.main.item_following_users.view.*

class UserFollowedAdapter(
    private val itemList: List<Items>?
) :
    RecyclerView.Adapter<UserFollowedAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val userName: TextView = itemView.twFollowingUser
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView =
            LayoutInflater.from(parent.context).inflate(R.layout.item_following_users, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList?.get(position)
        holder.userName.text = currentItem?.objectX?.identifier ?: ""
    }

    override fun getItemCount() = itemList?.size ?: 0
}