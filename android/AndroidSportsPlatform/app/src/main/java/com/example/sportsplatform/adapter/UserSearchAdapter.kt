package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.data.models.responses.UserResponse
import com.example.sportsplatform.util.toast
import kotlinx.android.synthetic.main.item_searched_user_layout.view.*

class UserSearchAdapter(private val itemList: List<UserResponse>?) :
    RecyclerView.Adapter<UserSearchAdapter.MyViewHolder>() {

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val userName: TextView = itemView.twUserName
        val userIdentifier: TextView = itemView.twUserIdentifier
        val userEmail: TextView = itemView.twUserEmail

        init {
            itemView.setOnClickListener{
                it.context.toast("Pressed!")
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView = LayoutInflater.from(parent.context)
            .inflate(com.example.sportsplatform.R.layout.item_searched_user_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = itemList?.get(position)
        holder.userName.text = currentItem?.name
        holder.userIdentifier.text = currentItem?.identifier
        holder.userEmail.text = currentItem?.email
    }

    override fun getItemCount(): Int = itemList?.size ?: 0
}