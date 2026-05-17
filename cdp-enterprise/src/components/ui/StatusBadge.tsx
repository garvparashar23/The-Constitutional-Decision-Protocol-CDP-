import React from 'react';
import { AlertCircle, CheckCircle2, AlertTriangle, ShieldCheck, Info } from 'lucide-react';

export type BadgeStatus = 'success' | 'warning' | 'error' | 'info' | 'verified';

interface StatusBadgeProps {
  status: BadgeStatus;
  label: string;
  className?: string;
}

export function StatusBadge({ status, label, className = '' }: StatusBadgeProps) {
  const config = {
    success: { colors: 'bg-green-500/10 text-green-400 border-green-500/20', icon: CheckCircle2 },
    warning: { colors: 'bg-amber-500/10 text-amber-500 border-amber-500/20', icon: AlertTriangle },
    error: { colors: 'bg-red-500/10 text-red-400 border-red-500/20', icon: AlertCircle },
    info: { colors: 'bg-blue-500/10 text-blue-400 border-blue-500/20', icon: Info },
    verified: { colors: 'bg-indigo-500/10 text-indigo-400 border-indigo-500/20', icon: ShieldCheck },
  };

  const { colors, icon: Icon } = config[status];

  return (
    <span className={`inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-md border text-xs font-medium ${colors} ${className}`}>
      <Icon className="w-3.5 h-3.5" />
      <span>{label}</span>
    </span>
  );
}
