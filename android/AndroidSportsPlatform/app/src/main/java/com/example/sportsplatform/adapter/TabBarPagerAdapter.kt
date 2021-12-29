package com.example.sportsplatform.adapter

import android.content.Context
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentStatePagerAdapter
import com.example.sportsplatform.R
import com.example.sportsplatform.fragments.HomeFragment
import com.example.sportsplatform.fragments.ProfileFragment
import com.example.sportsplatform.fragments.SearchFragment
import com.example.sportsplatform.util.Constants.TABBAR_COUNT

class TabBarPagerAdapter(
    fm: FragmentManager,
    contextParam: Context
) : FragmentStatePagerAdapter(fm, BEHAVIOR_RESUME_ONLY_CURRENT_FRAGMENT) {

    val context: Context = contextParam

    override fun getCount(): Int = TABBAR_COUNT

    override fun getItem(position: Int): Fragment {
        return when (position) {
            0 -> HomeFragment()
            1 -> SearchFragment()
            2 -> ProfileFragment()
            else -> HomeFragment()
        }
    }

    override fun getPageTitle(position: Int): CharSequence {
        return when (position) {
            0 -> context.resources.getString(R.string.tabBarHome)
            1 -> context.resources.getString(R.string.tabBarSearch)
            2 -> context.resources.getString(R.string.tabBarProfile)
            else -> ""
        }
    }
}