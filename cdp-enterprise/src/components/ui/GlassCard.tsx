import React from 'react';

interface GlassCardProps {
  children: React.ReactNode;
  className?: string;
  hoverEffect?: boolean;
}

export function GlassCard({ children, className = '', hoverEffect = false }: GlassCardProps) {
  return (
    <div 
      className={`
        bg-[#0B1120]/60 backdrop-blur-xl border border-gray-800/60 rounded-xl p-5 shadow-lg
        ${hoverEffect ? 'hover:border-amber-500/30 hover:shadow-amber-500/5 transition-all duration-300' : ''}
        ${className}
      `}
    >
      {children}
    </div>
  );
}
