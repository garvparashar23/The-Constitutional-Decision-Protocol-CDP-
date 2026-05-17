import React from 'react';

interface SectionHeaderProps {
  title: string;
  description?: string;
  icon?: React.ReactNode;
  action?: React.ReactNode;
}

export function SectionHeader({ title, description, icon, action }: SectionHeaderProps) {
  return (
    <div className="flex items-start justify-between mb-6">
      <div className="flex items-start space-x-3">
        {icon && (
          <div className="mt-1 p-2 bg-gray-800/50 border border-gray-700/50 rounded-lg text-amber-500">
            {icon}
          </div>
        )}
        <div>
          <h2 className="text-xl font-serif font-medium text-white tracking-wide">{title}</h2>
          {description && <p className="text-sm text-gray-400 mt-1 max-w-2xl">{description}</p>}
        </div>
      </div>
      {action && <div>{action}</div>}
    </div>
  );
}
