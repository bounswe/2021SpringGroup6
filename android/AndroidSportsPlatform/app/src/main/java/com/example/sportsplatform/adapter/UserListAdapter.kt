package com.example.sportsplatform.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.recyclerview.widget.RecyclerView
import com.example.sportsplatform.data.models.responses.EventResponse
import com.example.sportsplatform.data.models.responses.UserResponse
import com.example.sportsplatform.util.toast
import kotlinx.android.synthetic.main.item_event_layout.view.*
import kotlinx.android.synthetic.main.item_searched_user_layout.view.*

interface UsersClickListener {
    fun onUsersClickListener(userResponse: UserResponse?)
}

class UserListAdapter(
    private val itemClickListenerListener: UsersClickListener?
) :
    RecyclerView.Adapter<UserListAdapter.MyViewHolder>() {

    var items = mutableListOf<UserResponse?>()
        set(value) {
            field.clear()
            field.addAll(value)
            notifyDataSetChanged()
        }

    class MyViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val container: ConstraintLayout = itemView.clUserContainer
        val userName: TextView = itemView.twUserName
        val userIdentifier: TextView = itemView.twUserIdentifier
        val userEmail: TextView = itemView.twUserEmail
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val itemView = LayoutInflater.from(parent.context)
            .inflate(com.example.sportsplatform.R.layout.item_searched_user_layout, parent, false)
        return MyViewHolder(itemView)
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val currentItem = items.get(position)
        holder.userName.text = currentItem?.name
        holder.userIdentifier.text = currentItem?.identifier
        holder.userEmail.text = currentItem?.email
        holder.container.setOnClickListener {
            currentItem?.let { item -> itemClickListenerListener?.onUsersClickListener(item) }
        }
    }

    override fun getItemCount() = items.size
}