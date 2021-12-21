package com.example.sportsplatform.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.example.sportsplatform.adapter.TabBarPagerAdapter
import com.example.sportsplatform.databinding.FragmentTabBarBinding
import com.example.sportsplatform.util.Constants.TABBAR_COUNT
import com.google.android.material.tabs.TabLayout

class TabBarFragment : Fragment() {

    private var _binding: FragmentTabBarBinding? = null
    private val binding get() = _binding!!

    private val tabBarAdapter by lazy { TabBarPagerAdapter(childFragmentManager, requireContext()) }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentTabBarBinding.inflate(inflater, container, false)
        initializeTabBarPager()
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        binding.tabLayout.addOnTabSelectedListener(object : TabLayout.OnTabSelectedListener {
            override fun onTabSelected(tab: TabLayout.Tab?) {}

            override fun onTabUnselected(tab: TabLayout.Tab?) {}

            override fun onTabReselected(tab: TabLayout.Tab?) {}

        })
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    private fun initializeTabBarPager() {
        binding.viewPagerTabBar.apply {
            offscreenPageLimit = TABBAR_COUNT
            adapter = tabBarAdapter
        }
    }
}