"use client";

import React from 'react';
import { 
  History, Search, PlayCircle, GitCompare, Calendar, ChevronRight
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { SectionHeader } from '@/components/ui/SectionHeader';
import { StatusBadge } from '@/components/ui/StatusBadge';

export default function HistoryPage() {
  const sessions = [
    {
      id: 'S-8492',
      date: 'Today, 14:30',
      title: 'PMLA Bail Adjudication: Sisodia Precedent',
      status: 'verified',
      articles: ['Art 21', 'Sec 45 PMLA'],
    },
    {
      id: 'S-8491',
      date: 'Yesterday, 09:15',
      title: 'UAPA Default Bail Analysis',
      status: 'warning',
      articles: ['Art 22', 'Sec 43D(5) UAPA'],
    },
    {
      id: 'S-8490',
      date: 'Oct 24, 16:00',
      title: 'Digital Evidence Admissibility',
      status: 'success',
      articles: ['Sec 65B IEA'],
    }
  ];

  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide">Enterprise Intelligence Memory</h1>
          <p className="text-gray-400 mt-2">Chronological timeline of past constitutional analyses and reasoning replays.</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Timeline & Search */}
        <div className="lg:col-span-2 space-y-6">
          <GlassCard>
            <div className="flex flex-col md:flex-row md:items-center justify-between mb-6 gap-4">
              <SectionHeader 
                title="Session Timeline" 
                icon={<History className="w-5 h-5" />}
              />
              <div className="relative w-full md:w-64">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-500" />
                <input type="text" placeholder="Semantic search..." className="w-full bg-[#051838] border border-gray-800 rounded-lg pl-10 pr-4 py-2 text-sm text-gray-200 focus:border-amber-500/50 outline-none" />
              </div>
            </div>

            <div className="space-y-4">
              {sessions.map((session) => (
                <div key={session.id} className="flex items-center justify-between p-4 bg-[#0B1120]/50 border border-gray-800 rounded-xl hover:border-amber-500/30 transition-all group cursor-pointer">
                  <div className="flex items-center space-x-4">
                    <div className="w-10 h-10 rounded-lg bg-gray-800 flex items-center justify-center text-gray-400 group-hover:text-amber-500 group-hover:bg-amber-500/10 transition-colors">
                      <Calendar className="w-5 h-5" />
                    </div>
                    <div>
                      <h4 className="text-white font-medium">{session.title}</h4>
                      <div className="flex items-center space-x-3 mt-1 text-xs text-gray-500">
                        <span>{session.id}</span>
                        <span>•</span>
                        <span>{session.date}</span>
                        <span>•</span>
                        <div className="flex space-x-1">
                          {session.articles.map((art) => (
                            <span key={art} className="px-1.5 py-0.5 bg-gray-800 rounded text-gray-400">{art}</span>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center space-x-4">
                    <StatusBadge status={session.status as any} label={session.status === 'verified' ? 'Verified' : session.status === 'warning' ? 'Conflict' : 'Complete'} />
                    <ChevronRight className="w-5 h-5 text-gray-600 group-hover:text-amber-500 transition-colors" />
                  </div>
                </div>
              ))}
            </div>
          </GlassCard>
        </div>

        {/* Actions */}
        <div className="lg:col-span-1 space-y-6">
          <GlassCard hoverEffect className="cursor-pointer group">
            <div className="flex items-center space-x-4">
              <div className="w-12 h-12 rounded-full bg-blue-500/10 flex items-center justify-center group-hover:bg-blue-500/20 transition-colors border border-blue-500/20">
                <PlayCircle className="w-6 h-6 text-blue-400" />
              </div>
              <div>
                <h3 className="text-lg font-medium text-white group-hover:text-blue-400 transition-colors">Session Replay</h3>
                <p className="text-sm text-gray-400 mt-1">Reopen past AI debates and logic trees.</p>
              </div>
            </div>
          </GlassCard>

          <GlassCard hoverEffect className="cursor-pointer group">
            <div className="flex items-center space-x-4">
              <div className="w-12 h-12 rounded-full bg-purple-500/10 flex items-center justify-center group-hover:bg-purple-500/20 transition-colors border border-purple-500/20">
                <GitCompare className="w-6 h-6 text-purple-400" />
              </div>
              <div>
                <h3 className="text-lg font-medium text-white group-hover:text-purple-400 transition-colors">Comparative Analysis</h3>
                <p className="text-sm text-gray-400 mt-1">Compare multiple reasoning outputs.</p>
              </div>
            </div>
          </GlassCard>
          
          <GlassCard>
             <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-4">Memory Stats</h3>
             <div className="space-y-3">
                <div className="flex justify-between items-center text-sm">
                   <span className="text-gray-400">Total Sessions</span>
                   <span className="text-white font-mono">1,204</span>
                </div>
                <div className="flex justify-between items-center text-sm">
                   <span className="text-gray-400">Precedents Indexed</span>
                   <span className="text-white font-mono">8,492</span>
                </div>
                <div className="flex justify-between items-center text-sm">
                   <span className="text-gray-400">Storage Used</span>
                   <span className="text-white font-mono">4.2 GB</span>
                </div>
             </div>
          </GlassCard>
        </div>

      </div>
    </div>
  );
}
