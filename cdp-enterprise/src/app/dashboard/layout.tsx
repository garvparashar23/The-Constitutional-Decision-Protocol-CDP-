"use client";

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { 
  LayoutDashboard, 
  Terminal, 
  Scale, 
  History, 
  Bookmark, 
  FileText, 
  ShieldCheck, 
  Settings, 
  User,
  Search,
  Bell,
  MessageSquare
} from 'lucide-react';

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();

  const navItems = [
    { name: 'Dashboard', href: '/dashboard', icon: <LayoutDashboard className="w-5 h-5" /> },
    { name: 'CDP Workspace', href: '/dashboard/workspace', icon: <Terminal className="w-5 h-5" /> },
    { name: 'Legal Analysis', href: '/dashboard/analysis', icon: <Scale className="w-5 h-5" /> },
    { name: 'History', href: '/dashboard/history', icon: <History className="w-5 h-5" /> },
    { name: 'Saved Research', href: '/dashboard/research', icon: <Bookmark className="w-5 h-5" /> },
    { name: 'Constitutional Reports', href: '/dashboard/reports', icon: <FileText className="w-5 h-5" /> },
    { name: 'AI Verification Logs', href: '/dashboard/verification-logs', icon: <ShieldCheck className="w-5 h-5" /> },
  ];

  const bottomNavItems = [
    { name: 'Settings', href: '/dashboard/settings', icon: <Settings className="w-5 h-5" /> },
    { name: 'Profile', href: '/dashboard/profile', icon: <User className="w-5 h-5" /> },
  ];

  return (
    <div className="flex h-screen bg-[#051838] font-sans text-gray-100 overflow-hidden selection:bg-amber-500/30">
      {/* Advanced Left Sidebar */}
      <aside className="w-72 bg-[#080D18] border-r border-gray-800/60 flex flex-col flex-shrink-0 relative backdrop-blur-xl">
        
        {/* Top Brand Area */}
        <div className="h-20 flex items-center px-6 border-b border-gray-800/60 bg-gradient-to-b from-[#0B1120] to-[#080D18]">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 bg-gradient-to-br from-amber-500 to-orange-600 rounded-lg flex items-center justify-center shadow-lg shadow-amber-500/20">
              <Scale className="w-4 h-4 text-white" />
            </div>
            <div>
              <Link href="/dashboard" className="text-xl font-serif font-semibold tracking-tight text-white block leading-tight">
                CDP<span className="text-amber-500">.</span>
              </Link>
              <span className="text-[10px] text-gray-500 font-mono tracking-widest uppercase">Enterprise OS</span>
            </div>
          </div>
        </div>

        {/* Main Navigation */}
        <div className="flex-1 overflow-y-auto py-6 px-4 space-y-8 scrollbar-hide">
          
          {/* Section: Core Systems */}
          <div>
            <div className="px-3 mb-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">Core Systems</div>
            <div className="space-y-1">
              {navItems.slice(0, 2).map((item) => {
                const isActive = pathname === item.href;
                return (
                  <Link 
                    key={item.name} 
                    href={item.href}
                    className={`flex items-center space-x-3 px-3 py-2.5 rounded-lg transition-all duration-200 group relative overflow-hidden ${
                      isActive 
                        ? 'bg-gray-800/50 text-white shadow-sm' 
                        : 'text-gray-400 hover:bg-gray-800/30 hover:text-gray-200'
                    }`}
                  >
                    {isActive && (
                      <div className="absolute left-0 top-0 bottom-0 w-1 bg-gradient-to-b from-amber-400 to-orange-600 rounded-r-md"></div>
                    )}
                    <div className={`${isActive ? 'text-amber-500' : 'text-gray-500 group-hover:text-gray-400'} transition-colors`}>
                      {item.icon}
                    </div>
                    <span className={`text-sm font-medium ${isActive ? 'font-semibold' : ''}`}>{item.name}</span>
                  </Link>
                );
              })}
            </div>
          </div>

          {/* Section: Intelligence */}
          <div>
            <div className="px-3 mb-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">Intelligence</div>
            <div className="space-y-1">
              {navItems.slice(2).map((item) => {
                const isActive = pathname === item.href;
                return (
                  <Link 
                    key={item.name} 
                    href={item.href}
                    className={`flex items-center space-x-3 px-3 py-2.5 rounded-lg transition-all duration-200 group relative overflow-hidden ${
                      isActive 
                        ? 'bg-gray-800/50 text-white shadow-sm' 
                        : 'text-gray-400 hover:bg-gray-800/30 hover:text-gray-200'
                    }`}
                  >
                    {isActive && (
                      <div className="absolute left-0 top-0 bottom-0 w-1 bg-gradient-to-b from-amber-400 to-orange-600 rounded-r-md"></div>
                    )}
                    <div className={`${isActive ? 'text-amber-500' : 'text-gray-500 group-hover:text-gray-400'} transition-colors`}>
                      {item.icon}
                    </div>
                    <span className={`text-sm font-medium ${isActive ? 'font-semibold' : ''}`}>{item.name}</span>
                  </Link>
                );
              })}
            </div>
          </div>
        </div>

        {/* Bottom Profile Area */}
        <div className="p-4 border-t border-gray-800/60 bg-[#0B1120]/50 backdrop-blur-md">
          <div className="space-y-1 mb-4">
            {bottomNavItems.map((item) => (
              <Link 
                key={item.name} 
                href={item.href}
                className="flex items-center space-x-3 px-3 py-2 rounded-lg text-gray-400 hover:bg-gray-800/50 hover:text-white transition-colors group"
              >
                <div className="text-gray-500 group-hover:text-gray-400 transition-colors">
                  {item.icon}
                </div>
                <span className="text-sm font-medium">{item.name}</span>
              </Link>
            ))}
          </div>
          
          <div className="flex items-center p-3 bg-gray-900/80 rounded-xl border border-gray-800 hover:border-gray-700 transition-colors cursor-pointer group">
            <div className="w-9 h-9 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white font-medium shadow-inner relative">
              GP
              <div className="absolute bottom-0 right-0 w-2.5 h-2.5 bg-green-500 border-2 border-gray-900 rounded-full"></div>
            </div>
            <div className="ml-3 flex-1 overflow-hidden">
              <p className="text-sm font-medium text-white truncate">Garv Parashar</p>
              <p className="text-xs text-gray-500 truncate group-hover:text-gray-400 transition-colors">Chief Intelligence Officer</p>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 overflow-y-auto relative bg-[#051838] shadow-inner flex flex-col">
        
        {/* Global Enterprise Top Bar */}
        <header className="h-16 border-b border-gray-800/60 bg-[#0B1120]/80 backdrop-blur-md flex items-center justify-between px-6 flex-shrink-0 z-20">
          <div className="flex-1 max-w-xl">
            <div className="relative group">
              <Search className="w-4 h-4 text-gray-500 absolute left-3 top-1/2 transform -translate-y-1/2 group-focus-within:text-amber-500 transition-colors" />
              <input 
                type="text" 
                placeholder="Search precedents, sessions, or constitutional articles..." 
                className="w-full bg-[#051838] border border-gray-800 text-sm text-gray-200 rounded-lg pl-10 pr-4 py-2 focus:outline-none focus:border-amber-500/50 focus:ring-1 focus:ring-amber-500/50 transition-all placeholder-gray-600"
              />
              <div className="absolute right-3 top-1/2 transform -translate-y-1/2 flex items-center space-x-1">
                <kbd className="hidden sm:inline-block px-1.5 py-0.5 text-[10px] font-medium text-gray-500 bg-gray-800/50 border border-gray-700 rounded-md">Ctrl</kbd>
                <kbd className="hidden sm:inline-block px-1.5 py-0.5 text-[10px] font-medium text-gray-500 bg-gray-800/50 border border-gray-700 rounded-md">K</kbd>
              </div>
            </div>
          </div>
          
          <div className="flex items-center space-x-4 ml-4">
            <button className="relative p-2 text-gray-400 hover:text-white transition-colors rounded-lg hover:bg-gray-800/50">
              <Bell className="w-5 h-5" />
              <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-red-500 rounded-full border border-[#0B1120]"></span>
            </button>
            <button className="flex items-center space-x-2 px-3 py-1.5 bg-gradient-to-r from-amber-500/10 to-orange-600/10 border border-amber-500/20 rounded-lg text-amber-500 hover:bg-amber-500/20 transition-all group">
              <MessageSquare className="w-4 h-4 group-hover:scale-110 transition-transform" />
              <span className="text-sm font-medium">Ask AI</span>
            </button>
          </div>
        </header>

        {/* Page Content */}
        <div className="flex-1 overflow-y-auto w-full relative">
          {children}
        </div>
      </main>
    </div>
  );
}
