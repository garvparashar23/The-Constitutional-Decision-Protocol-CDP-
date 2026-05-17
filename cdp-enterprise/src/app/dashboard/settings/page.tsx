"use client";

import React, { useState } from 'react';
import { 
  Settings, UserCircle, Sliders, Shield, Palette, Save
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { SectionHeader } from '@/components/ui/SectionHeader';

export default function SettingsPage() {
  const [activeTab, setActiveTab] = useState('ai');

  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in flex flex-col h-[calc(100vh-4rem)]">
      <div className="flex items-center justify-between mb-8 flex-shrink-0">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide">Enterprise Settings</h1>
          <p className="text-gray-400 mt-2">Manage AI configuration, security, and workspace preferences.</p>
        </div>
        <button className="flex items-center space-x-2 px-6 py-2.5 bg-amber-500 hover:bg-amber-600 text-gray-900 font-medium rounded-lg transition-colors shadow-lg shadow-amber-500/20">
          <Save className="w-4 h-4" />
          <span>Save Changes</span>
        </button>
      </div>

      <div className="flex flex-col lg:flex-row gap-8 flex-1 min-h-0">
        
        {/* Settings Navigation */}
        <div className="lg:w-64 flex-shrink-0 space-y-1">
          <button 
            onClick={() => setActiveTab('profile')}
            className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg text-sm font-medium transition-colors ${activeTab === 'profile' ? 'bg-amber-500/10 text-amber-500 border border-amber-500/20' : 'text-gray-400 hover:bg-gray-800/50 hover:text-white'}`}
          >
            <UserCircle className="w-5 h-5" />
            <span>Profile settings</span>
          </button>
          <button 
            onClick={() => setActiveTab('ai')}
            className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg text-sm font-medium transition-colors ${activeTab === 'ai' ? 'bg-amber-500/10 text-amber-500 border border-amber-500/20' : 'text-gray-400 hover:bg-gray-800/50 hover:text-white'}`}
          >
            <Sliders className="w-5 h-5" />
            <span>AI Configuration</span>
          </button>
          <button 
            onClick={() => setActiveTab('security')}
            className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg text-sm font-medium transition-colors ${activeTab === 'security' ? 'bg-amber-500/10 text-amber-500 border border-amber-500/20' : 'text-gray-400 hover:bg-gray-800/50 hover:text-white'}`}
          >
            <Shield className="w-5 h-5" />
            <span>Security & Access</span>
          </button>
          <button 
            onClick={() => setActiveTab('theme')}
            className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg text-sm font-medium transition-colors ${activeTab === 'theme' ? 'bg-amber-500/10 text-amber-500 border border-amber-500/20' : 'text-gray-400 hover:bg-gray-800/50 hover:text-white'}`}
          >
            <Palette className="w-5 h-5" />
            <span>Appearance</span>
          </button>
        </div>

        {/* Settings Content */}
        <div className="flex-1 overflow-y-auto pr-2 scrollbar-hide">
          
          {activeTab === 'ai' && (
            <GlassCard className="max-w-3xl">
              <SectionHeader 
                title="AI Intelligence Configuration" 
                description="Control how the constitutional reasoning agents operate and verify logic."
                icon={<Sliders className="w-5 h-5" />}
              />
              
              <div className="space-y-8 mt-6">
                
                <div className="space-y-4">
                  <h3 className="text-sm font-semibold text-white">Reasoning Depth</h3>
                  <p className="text-xs text-gray-400">Higher depth increases processing time but yields more exhaustive precedent searches.</p>
                  <input type="range" min="1" max="10" defaultValue="8" className="w-full h-2 bg-gray-800 rounded-lg appearance-none cursor-pointer accent-amber-500" />
                  <div className="flex justify-between text-xs text-gray-500 font-mono">
                     <span>L1 (Fast)</span>
                     <span className="text-amber-500">L8 (Deep Search)</span>
                     <span>L10 (Exhaustive)</span>
                  </div>
                </div>

                <div className="pt-6 border-t border-gray-800/60 space-y-4">
                  <h3 className="text-sm font-semibold text-white">Multi-Agent Debate Intensity</h3>
                  <div className="grid grid-cols-3 gap-4">
                     <div className="border border-gray-700 bg-[#051838] rounded-lg p-4 cursor-pointer hover:border-amber-500/50 transition-colors">
                        <div className="font-medium text-white mb-1">Standard</div>
                        <div className="text-xs text-gray-500">2 Agents (Petitioner vs Respondent)</div>
                     </div>
                     <div className="border border-amber-500/50 bg-amber-500/5 rounded-lg p-4 cursor-pointer relative overflow-hidden">
                        <div className="absolute top-0 right-0 w-8 h-8 bg-amber-500/20 rounded-bl-full"></div>
                        <div className="font-medium text-amber-500 mb-1">Advanced</div>
                        <div className="text-xs text-amber-500/70">5 Agents (Full Constitutional Bench)</div>
                     </div>
                     <div className="border border-gray-700 bg-[#051838] rounded-lg p-4 cursor-pointer hover:border-amber-500/50 transition-colors">
                        <div className="font-medium text-white mb-1">Supreme</div>
                        <div className="text-xs text-gray-500">9 Agents (Historical Bench Simulation)</div>
                     </div>
                  </div>
                </div>

                <div className="pt-6 border-t border-gray-800/60 space-y-4">
                  <div className="flex items-center justify-between">
                     <div>
                        <h3 className="text-sm font-semibold text-white mb-1">Strict Constitutional Adherence</h3>
                        <p className="text-xs text-gray-400">If enabled, SMT solvers will strictly reject any logic that slightly contradicts the literal text, limiting purposive interpretation.</p>
                     </div>
                     <label className="relative inline-flex items-center cursor-pointer">
                        <input type="checkbox" value="" className="sr-only peer" />
                        <div className="w-11 h-6 bg-gray-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-amber-500"></div>
                     </label>
                  </div>
                </div>

              </div>
            </GlassCard>
          )}

          {activeTab === 'profile' && (
            <GlassCard className="max-w-3xl">
              <SectionHeader title="Profile Settings" icon={<UserCircle className="w-5 h-5" />} />
              <div className="space-y-4 mt-6">
                 <div>
                    <label className="block text-xs font-medium text-gray-400 mb-1">Full Name</label>
                    <input type="text" defaultValue="Garv Parashar" className="w-full bg-[#051838] border border-gray-800 rounded-lg px-4 py-2 text-sm text-white focus:border-amber-500/50 outline-none" />
                 </div>
                 <div>
                    <label className="block text-xs font-medium text-gray-400 mb-1">Institution</label>
                    <input type="text" defaultValue="National Law University / AI Legal Lab" className="w-full bg-[#051838] border border-gray-800 rounded-lg px-4 py-2 text-sm text-white focus:border-amber-500/50 outline-none" />
                 </div>
                 <div>
                    <label className="block text-xs font-medium text-gray-400 mb-1">Role</label>
                    <input type="text" defaultValue="Chief Intelligence Officer" className="w-full bg-[#051838] border border-gray-800 rounded-lg px-4 py-2 text-sm text-white focus:border-amber-500/50 outline-none" />
                 </div>
              </div>
            </GlassCard>
          )}
          
          {(activeTab === 'security' || activeTab === 'theme') && (
            <div className="text-gray-500 p-8 text-center italic">
              {activeTab} settings placeholder.
            </div>
          )}

        </div>
      </div>
    </div>
  );
}
