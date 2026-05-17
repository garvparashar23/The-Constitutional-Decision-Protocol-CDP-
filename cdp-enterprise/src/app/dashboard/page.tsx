"use client";

import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Activity, FileText, CheckCircle, Clock } from 'lucide-react';
import Link from 'next/link';

export default function DashboardPage() {
  const fadeUp = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.5 } }
  };

  const stagger = {
    hidden: { opacity: 0 },
    visible: { opacity: 1, transition: { staggerChildren: 0.1 } }
  };

  return (
    <div className="p-8 md:p-12">
      {/* Welcome Section */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-12">
        <h1 className="text-3xl font-serif text-white mb-2">Welcome back, Garv.</h1>
        <p className="text-gray-400">Your enterprise constitutional intelligence environment is ready.</p>
      </motion.div>

      {/* Main Entry Point */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="mb-16">
        <Link href="/dashboard/workspace" className="block relative group overflow-hidden rounded-2xl bg-gray-900 text-white p-8 md:p-12 shadow-2xl border border-gray-800 transition-all hover:shadow-gray-900/50">
          <div className="absolute inset-0 bg-gradient-to-br from-gray-800/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          
          {/* Subtle glowing effect */}
          <div className="absolute -top-24 -right-24 w-64 h-64 bg-gray-700 blur-3xl rounded-full opacity-30 group-hover:bg-gray-600 group-hover:opacity-50 transition-all duration-700"></div>
          
          <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between">
            <div>
              <h2 className="text-3xl md:text-4xl font-serif font-medium mb-3">Launch Constitutional Decision Platform</h2>
              <p className="text-gray-400 text-lg max-w-xl">
                Initiate a new formal verification session. Access the multi-agent debate, SMT solver, and structural causal engine.
              </p>
            </div>
            <div className="mt-8 md:mt-0">
              <div className="w-14 h-14 rounded-full bg-white text-gray-900 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                <ArrowRight className="w-6 h-6" />
              </div>
            </div>
          </div>
        </Link>
      </motion.div>

      {/* Metrics / Quick Stats */}
      <motion.div initial="hidden" animate="visible" variants={stagger} className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12">
        {[
          { label: "Active Sessions", value: "3", icon: <Activity className="w-4 h-4 text-blue-500" /> },
          { label: "Verified Decisions", value: "128", icon: <CheckCircle className="w-4 h-4 text-green-500" /> },
          { label: "Constitutional Conflicts", value: "2", icon: <FileText className="w-4 h-4 text-amber-500" /> },
          { label: "Compute Hours", value: "42.5", icon: <Clock className="w-4 h-4 text-purple-500" /> }
        ].map((stat, i) => (
          <motion.div key={i} variants={fadeUp} className="bg-[#0B1120] p-6 rounded-xl border border-gray-800 shadow-sm">
            <div className="flex items-center space-x-3 mb-2">
              {stat.icon}
              <span className="text-sm font-medium text-gray-400">{stat.label}</span>
            </div>
            <div className="text-3xl font-serif text-white">{stat.value}</div>
          </motion.div>
        ))}
      </motion.div>

      {/* User History Panel & Workspace Preview Cards */}
      <motion.div initial="hidden" animate="visible" variants={fadeUp} className="bg-[#0B1120] rounded-xl border border-gray-800 shadow-sm overflow-hidden">
        <div className="px-8 py-6 border-b border-gray-800 flex items-center justify-between">
          <h3 className="text-lg font-serif font-medium text-white">Recent Constitutional Analyses</h3>
          <button className="text-sm text-gray-400 hover:text-white transition-colors">View All</button>
        </div>
        <div className="divide-y divide-gray-800">
          {[
            { id: "CDP-892", query: "Bail application under severe statutory strictures (Section 43D UAPA).", date: "Today, 10:42 AM", status: "Verified", score: "99.2%" },
            { id: "CDP-891", query: "Corporate liability in algorithmic discriminatory pricing models.", date: "Yesterday, 14:15 PM", status: "Conflict Detected", score: "64.5%" },
            { id: "CDP-890", query: "Executive overreach in environmental emergency decrees.", date: "Oct 12, 09:00 AM", status: "Verified", score: "96.8%" }
          ].map((item, i) => (
            <div key={i} className="px-8 py-5 hover:bg-gray-800/50 transition-colors cursor-pointer flex items-center justify-between group">
              <div className="flex-1 pr-8">
                <div className="flex items-center space-x-3 mb-1">
                  <span className="text-xs font-mono font-medium text-gray-400">{item.id}</span>
                  <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${item.status === 'Verified' ? 'bg-green-900/30 text-green-400' : 'bg-amber-900/30 text-amber-400'}`}>
                    {item.status}
                  </span>
                </div>
                <p className="text-sm font-medium text-gray-300 group-hover:text-amber-500 transition-colors">{item.query}</p>
              </div>
              <div className="text-right">
                <div className="text-xs text-gray-500 mb-1">{item.date}</div>
                <div className="text-sm font-medium text-white">Conf: {item.score}</div>
              </div>
            </div>
          ))}
        </div>
      </motion.div>
    </div>
  );
}
