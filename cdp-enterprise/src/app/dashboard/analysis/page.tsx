"use client";

import React from 'react';
import { motion } from 'framer-motion';
import { 
  Network, Search, AlertTriangle, Lightbulb, TrendingUp, Scale
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { SectionHeader } from '@/components/ui/SectionHeader';
import { StatusBadge } from '@/components/ui/StatusBadge';

export default function LegalAnalysisPage() {
  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide">Legal Intelligence Analysis</h1>
          <p className="text-gray-400 mt-2">Deep legal reasoning, risk mapping, and precedent intelligence.</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        {/* Article Mapping */}
        <GlassCard className="lg:col-span-1 min-h-[400px] flex flex-col">
          <SectionHeader 
            title="Constitutional Mapping" 
            description="Visual dependencies between articles and statutes."
            icon={<Network className="w-5 h-5" />}
          />
          <div className="flex-1 flex items-center justify-center bg-[#051838]/50 border border-gray-800 rounded-xl relative overflow-hidden group">
             {/* Mock Node Graph */}
             <div className="absolute inset-0 opacity-20 group-hover:opacity-40 transition-opacity bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-amber-500/20 via-transparent to-transparent"></div>
             <div className="relative z-10 text-center">
                <Network className="w-12 h-12 text-amber-500/50 mx-auto mb-4" />
                <p className="text-sm font-mono text-gray-500">[Interactive D3 Node Graph Placeholder]</p>
             </div>
          </div>
        </GlassCard>

        {/* Legal Risk */}
        <GlassCard className="lg:col-span-1 min-h-[400px]">
          <SectionHeader 
            title="Legal Risk Analysis" 
            description="AI-predicted procedural vulnerabilities."
            icon={<AlertTriangle className="w-5 h-5" />}
          />
          <div className="space-y-4">
            <div className="bg-red-500/5 border border-red-500/20 rounded-lg p-4">
              <div className="flex justify-between items-start mb-2">
                <h4 className="text-red-400 font-medium flex items-center"><AlertTriangle className="w-4 h-4 mr-2" /> Admissibility Risk</h4>
                <StatusBadge status="error" label="High" />
              </div>
              <p className="text-sm text-gray-400">Digital evidence chain of custody lacks Section 65B (Evidence Act) certification.</p>
            </div>
            
            <div className="bg-amber-500/5 border border-amber-500/20 rounded-lg p-4">
              <div className="flex justify-between items-start mb-2">
                <h4 className="text-amber-500 font-medium flex items-center"><Scale className="w-4 h-4 mr-2" /> Jurisdiction Conflict</h4>
                <StatusBadge status="warning" label="Medium" />
              </div>
              <p className="text-sm text-gray-400">Potential overlap between specialized PMLA court and regular sessions court jurisdiction.</p>
            </div>
          </div>
        </GlassCard>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Precedent Engine */}
        <GlassCard className="lg:col-span-2">
          <SectionHeader 
            title="Precedent Intelligence" 
            description="Analyze landmark judgments and judicial trends."
            icon={<TrendingUp className="w-5 h-5" />}
          />
          <div className="relative mb-4">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-500" />
            <input type="text" placeholder="Search precedent similarity..." className="w-full bg-[#051838] border border-gray-800 rounded-lg pl-10 pr-4 py-2 text-sm text-gray-200 focus:border-amber-500/50 outline-none" />
          </div>
          
          <table className="w-full text-sm text-left text-gray-400">
            <thead className="text-xs text-gray-500 uppercase bg-gray-900/50">
              <tr>
                <th className="px-4 py-3 rounded-tl-lg">Case Title</th>
                <th className="px-4 py-3">Year</th>
                <th className="px-4 py-3">Similarity</th>
                <th className="px-4 py-3 rounded-tr-lg">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr className="border-b border-gray-800 hover:bg-gray-800/30">
                <td className="px-4 py-3 font-medium text-gray-200">Manish Sisodia v. DoE</td>
                <td className="px-4 py-3">2024</td>
                <td className="px-4 py-3"><span className="text-green-400">94%</span></td>
                <td className="px-4 py-3"><button className="text-amber-500 hover:underline">Analyze</button></td>
              </tr>
              <tr className="border-b border-gray-800 hover:bg-gray-800/30">
                <td className="px-4 py-3 font-medium text-gray-200">Vijay Madanlal Choudhary</td>
                <td className="px-4 py-3">2022</td>
                <td className="px-4 py-3"><span className="text-green-400">88%</span></td>
                <td className="px-4 py-3"><button className="text-amber-500 hover:underline">Analyze</button></td>
              </tr>
            </tbody>
          </table>
        </GlassCard>

        {/* Explainability */}
        <GlassCard className="lg:col-span-1">
          <SectionHeader 
            title="Explainable AI" 
            description="Reasoning path."
            icon={<Lightbulb className="w-5 h-5" />}
          />
          <div className="space-y-4 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-gray-700 before:to-transparent">
             <div className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                <div className="flex items-center justify-center w-10 h-10 rounded-full border border-amber-500 bg-amber-500/20 text-amber-500 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2">
                    1
                </div>
                <div className="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-4 rounded-lg bg-[#051838] border border-gray-800 shadow-sm">
                    <p className="text-xs text-gray-300">Identified tension between Art 21 and PMLA Sec 45.</p>
                </div>
             </div>
             <div className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                <div className="flex items-center justify-center w-10 h-10 rounded-full border border-gray-700 bg-gray-800 text-gray-400 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2">
                    2
                </div>
                <div className="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] p-4 rounded-lg bg-[#051838] border border-gray-800 shadow-sm">
                    <p className="text-xs text-gray-500">Retrieving similar bail jurisprudence where delay > 18 months.</p>
                </div>
             </div>
          </div>
        </GlassCard>
      </div>

    </div>
  );
}
