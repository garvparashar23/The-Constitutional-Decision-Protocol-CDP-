"use client";

import React from 'react';
import { 
  User, Award, Target, Activity, FileText, CheckCircle2, Shield
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { SectionHeader } from '@/components/ui/SectionHeader';

export default function ProfilePage() {
  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide">Professional Identity</h1>
          <p className="text-gray-400 mt-2">Constitutional specialization, research metrics, and achievements.</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Left: Identity Card */}
        <div className="lg:col-span-1 space-y-6">
          <GlassCard className="text-center relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-24 bg-gradient-to-r from-amber-500/20 to-orange-600/20"></div>
            
            <div className="relative z-10">
               <div className="w-24 h-24 mx-auto bg-gradient-to-br from-indigo-500 to-purple-600 rounded-full flex items-center justify-center text-3xl text-white font-serif shadow-xl shadow-purple-500/20 border-4 border-[#051838] mt-6">
                 GP
               </div>
               <h2 className="text-xl font-bold text-white mt-4">Garv Parashar</h2>
               <p className="text-sm text-amber-500 font-medium">Chief Intelligence Officer</p>
               <p className="text-xs text-gray-400 mt-1 mb-6">National Law University / AI Legal Lab</p>
               
               <div className="grid grid-cols-2 gap-4 border-t border-gray-800 pt-6">
                 <div>
                    <p className="text-xs text-gray-500 uppercase tracking-wider mb-1">Rank</p>
                    <p className="text-sm text-gray-200 font-medium flex items-center justify-center">
                       <Shield className="w-4 h-4 text-blue-400 mr-1" /> Tier 1 Validator
                    </p>
                 </div>
                 <div>
                    <p className="text-xs text-gray-500 uppercase tracking-wider mb-1">Specialty</p>
                    <p className="text-sm text-gray-200 font-medium">Constitutional Law</p>
                 </div>
               </div>
            </div>
          </GlassCard>

          <GlassCard>
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-4">Constitutional Domains</h3>
            <div className="space-y-3">
               <div>
                  <div className="flex justify-between text-xs mb-1">
                     <span className="text-gray-300">Article 21 (Life & Liberty)</span>
                     <span className="text-amber-500">92%</span>
                  </div>
                  <div className="w-full bg-gray-800 rounded-full h-1.5">
                     <div className="bg-amber-500 h-1.5 rounded-full" style={{ width: '92%' }}></div>
                  </div>
               </div>
               <div>
                  <div className="flex justify-between text-xs mb-1">
                     <span className="text-gray-300">PMLA (Economic Offenses)</span>
                     <span className="text-amber-500">85%</span>
                  </div>
                  <div className="w-full bg-gray-800 rounded-full h-1.5">
                     <div className="bg-amber-500 h-1.5 rounded-full" style={{ width: '85%' }}></div>
                  </div>
               </div>
               <div>
                  <div className="flex justify-between text-xs mb-1">
                     <span className="text-gray-300">UAPA (Anti-Terror Laws)</span>
                     <span className="text-amber-500">78%</span>
                  </div>
                  <div className="w-full bg-gray-800 rounded-full h-1.5">
                     <div className="bg-amber-500 h-1.5 rounded-full" style={{ width: '78%' }}></div>
                  </div>
               </div>
            </div>
          </GlassCard>
        </div>

        {/* Right: Metrics & Achievements */}
        <div className="lg:col-span-2 space-y-6">
          
          {/* Key Metrics */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
             <GlassCard className="text-center p-4">
                <Activity className="w-6 h-6 text-blue-400 mx-auto mb-2" />
                <div className="text-2xl font-mono text-white mb-1">1,204</div>
                <div className="text-[10px] uppercase tracking-wider text-gray-500">Analyses</div>
             </GlassCard>
             <GlassCard className="text-center p-4">
                <FileText className="w-6 h-6 text-green-400 mx-auto mb-2" />
                <div className="text-2xl font-mono text-white mb-1">342</div>
                <div className="text-[10px] uppercase tracking-wider text-gray-500">Reports</div>
             </GlassCard>
             <GlassCard className="text-center p-4">
                <CheckCircle2 className="w-6 h-6 text-amber-500 mx-auto mb-2" />
                <div className="text-2xl font-mono text-white mb-1">98.4%</div>
                <div className="text-[10px] uppercase tracking-wider text-gray-500">Verif. Accuracy</div>
             </GlassCard>
             <GlassCard className="text-center p-4">
                <Target className="w-6 h-6 text-purple-400 mx-auto mb-2" />
                <div className="text-2xl font-mono text-white mb-1">89</div>
                <div className="text-[10px] uppercase tracking-wider text-gray-500">Conflicts Found</div>
             </GlassCard>
          </div>

          {/* Achievement System */}
          <GlassCard>
            <SectionHeader 
              title="Expert Achievements" 
              icon={<Award className="w-5 h-5" />}
            />
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
               <div className="flex items-center space-x-4 p-4 border border-gray-800 bg-[#051838]/50 rounded-lg">
                  <div className="w-12 h-12 rounded-full bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-500">
                     <Award className="w-6 h-6" />
                  </div>
                  <div>
                     <h4 className="text-sm font-medium text-white">Constitutional Oracle</h4>
                     <p className="text-xs text-gray-400 mt-0.5">Resolved 50+ complex Art 21 vs Statutory conflicts.</p>
                  </div>
               </div>

               <div className="flex items-center space-x-4 p-4 border border-gray-800 bg-[#051838]/50 rounded-lg opacity-75 grayscale hover:grayscale-0 transition-all cursor-pointer">
                  <div className="w-12 h-12 rounded-full bg-gray-800 border border-gray-700 flex items-center justify-center text-gray-400">
                     <Shield className="w-6 h-6" />
                  </div>
                  <div>
                     <h4 className="text-sm font-medium text-gray-300">Verification Master</h4>
                     <p className="text-xs text-gray-500 mt-0.5">Achieve 99.5% accuracy across 1000 SMT validations.</p>
                     <div className="w-full bg-gray-800 rounded-full h-1 mt-2">
                        <div className="bg-gray-500 h-1 rounded-full" style={{ width: '80%' }}></div>
                     </div>
                  </div>
               </div>
            </div>
          </GlassCard>
          
        </div>
      </div>
    </div>
  );
}
