"use client";

import React from 'react';
import { 
  Folder, FileText, Search, Plus, MessageSquare, Network, MoreHorizontal, Users
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { SectionHeader } from '@/components/ui/SectionHeader';

export default function SavedResearchPage() {
  const folders = [
    { id: 1, name: 'Constitutional Bench Cases', count: 12, updated: '2 hrs ago' },
    { id: 2, name: 'PMLA Jurisprudence', count: 45, updated: 'Yesterday' },
    { id: 3, name: 'UAPA Amendments Analysis', count: 8, updated: 'Oct 20' },
    { id: 4, name: 'Digital Privacy Doctrine', count: 24, updated: 'Oct 15' },
  ];

  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in flex flex-col h-[calc(100vh-4rem)]">
      <div className="flex items-center justify-between mb-8 flex-shrink-0">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide">Research Repository</h1>
          <p className="text-gray-400 mt-2">Enterprise knowledge system for constitutional projects and case studies.</p>
        </div>
        <button className="flex items-center space-x-2 px-4 py-2 bg-amber-500 hover:bg-amber-600 text-gray-900 font-medium rounded-lg transition-colors">
          <Plus className="w-4 h-4" />
          <span>New Collection</span>
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 flex-1 min-h-0">
        
        {/* Left Sidebar: Collections */}
        <div className="lg:col-span-1 flex flex-col space-y-4 overflow-y-auto pr-2 scrollbar-hide">
          <div className="relative mb-2">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-500" />
            <input type="text" placeholder="Filter collections..." className="w-full bg-[#0B1120] border border-gray-800 rounded-lg pl-10 pr-4 py-2 text-sm text-gray-200 focus:border-amber-500/50 outline-none" />
          </div>

          <div className="space-y-2">
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3 px-1">My Folders</h3>
            {folders.map(folder => (
              <div key={folder.id} className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-800/50 cursor-pointer group transition-colors">
                <div className="flex items-center space-x-3 overflow-hidden">
                  <Folder className="w-4 h-4 text-amber-500/70 group-hover:text-amber-500 flex-shrink-0" />
                  <span className="text-sm text-gray-300 group-hover:text-white truncate">{folder.name}</span>
                </div>
                <span className="text-xs text-gray-600 group-hover:text-gray-400">{folder.count}</span>
              </div>
            ))}
          </div>
          
          <div className="mt-8 space-y-2">
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3 px-1">Shared with me</h3>
            <div className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-800/50 cursor-pointer group transition-colors">
                <div className="flex items-center space-x-3 overflow-hidden">
                  <Users className="w-4 h-4 text-blue-500/70 group-hover:text-blue-500 flex-shrink-0" />
                  <span className="text-sm text-gray-300 group-hover:text-white truncate">Team Legal Research</span>
                </div>
            </div>
          </div>
        </div>

        {/* Main Content Area */}
        <div className="lg:col-span-3 flex flex-col gap-6 h-full min-h-0 overflow-y-auto pb-4 scrollbar-hide">
          
          {/* AI Research Assistant Chat */}
          <GlassCard className="flex flex-col h-[400px]">
            <SectionHeader 
              title="Collection Assistant" 
              description="Ask questions specifically grounded in the selected research folder."
              icon={<MessageSquare className="w-5 h-5" />}
            />
            
            <div className="flex-1 overflow-y-auto mb-4 pr-2 space-y-4">
              <div className="flex items-start space-x-3">
                <div className="w-8 h-8 rounded bg-gray-800 flex items-center justify-center flex-shrink-0">
                  <span className="text-xs font-bold text-gray-400">You</span>
                </div>
                <div className="bg-gray-800/40 rounded-2xl rounded-tl-sm px-4 py-3 text-sm text-gray-300">
                  Summarize the evolution of the "twin conditions" in PMLA based on the cases in this folder.
                </div>
              </div>
              
              <div className="flex items-start space-x-3">
                <div className="w-8 h-8 rounded bg-amber-500/20 border border-amber-500/30 flex items-center justify-center flex-shrink-0 text-amber-500">
                  AI
                </div>
                <div className="bg-amber-900/10 border border-amber-500/20 rounded-2xl rounded-tl-sm px-4 py-3 text-sm text-gray-300">
                  <p className="mb-2">Based on the 45 cases in your "PMLA Jurisprudence" folder, the evolution is as follows:</p>
                  <ol className="list-decimal pl-4 space-y-1 text-gray-400">
                     <li><strong>Nikesh Tarachand Shah (2017)</strong>: Struck down Section 45(1) as unconstitutional for being manifestly arbitrary.</li>
                     <li><strong>2018 Amendment</strong>: Reintroduced the twin conditions, altering the threshold.</li>
                     <li><strong>Vijay Madanlal Choudhary (2022)</strong>: Upheld the constitutional validity of the amended Section 45, citing compelling state interest.</li>
                  </ol>
                  <p className="mt-2 text-xs text-amber-500/80 cursor-pointer hover:underline">View 12 cited documents →</p>
                </div>
              </div>
            </div>

            <div className="relative mt-auto">
              <input 
                type="text" 
                placeholder="Ask your research assistant..." 
                className="w-full bg-[#051838] border border-gray-800 rounded-lg pl-4 pr-12 py-3 text-sm text-gray-200 focus:border-amber-500/50 outline-none"
              />
              <button className="absolute right-2 top-1/2 transform -translate-y-1/2 p-1.5 bg-amber-500/10 text-amber-500 rounded-md hover:bg-amber-500/20 transition-colors">
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </GlassCard>

          {/* Document Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <GlassCard hoverEffect className="cursor-pointer">
              <div className="flex items-start justify-between mb-3">
                <div className="p-2 bg-gray-800 rounded">
                  <FileText className="w-4 h-4 text-blue-400" />
                </div>
                <MoreHorizontal className="w-4 h-4 text-gray-600" />
              </div>
              <h4 className="text-white font-medium mb-1">Sisodia vs DoE Final Judgment</h4>
              <p className="text-xs text-gray-500 mb-3">PDF • Added 2 hrs ago</p>
              <div className="flex -space-x-2">
                 <div className="w-6 h-6 rounded-full bg-gray-700 border-2 border-[#0B1120]"></div>
                 <div className="w-6 h-6 rounded-full bg-indigo-600 border-2 border-[#0B1120]"></div>
              </div>
            </GlassCard>

            <GlassCard hoverEffect className="cursor-pointer">
              <div className="flex items-start justify-between mb-3">
                <div className="p-2 bg-gray-800 rounded">
                  <Network className="w-4 h-4 text-purple-400" />
                </div>
                <MoreHorizontal className="w-4 h-4 text-gray-600" />
              </div>
              <h4 className="text-white font-medium mb-1">Knowledge Graph: PMLA Sec 45</h4>
              <p className="text-xs text-gray-500 mb-3">Visualization • Added Yesterday</p>
            </GlassCard>
          </div>
          
        </div>
      </div>
    </div>
  );
}

// Dummy ChevronRight since it wasn't imported from lucide-react in the file
function ChevronRight(props: any) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m9 18 6-6-6-6" />
    </svg>
  );
}
