"use client";

import React from 'react';
import { 
  ShieldCheck, Terminal, FileCode2, Binary, Lock, Key, Activity
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { SectionHeader } from '@/components/ui/SectionHeader';
import { StatusBadge } from '@/components/ui/StatusBadge';

export default function VerificationLogsPage() {
  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in flex flex-col h-[calc(100vh-4rem)]">
      <div className="flex items-center justify-between mb-8 flex-shrink-0">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide">Trust & Verification Center</h1>
          <p className="text-gray-400 mt-2">Immutable audit logs, AI reasoning traceability, and formal logic proofs.</p>
        </div>
        <div className="flex items-center space-x-2 px-3 py-1 bg-green-500/10 border border-green-500/30 rounded-md">
           <Lock className="w-4 h-4 text-green-500" />
           <span className="text-xs font-mono text-green-500">SYSTEM SECURE</span>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 flex-1 min-h-0">
        
        {/* Left: Raw Logs & Traceability */}
        <div className="flex flex-col space-y-6 h-full overflow-hidden">
          <GlassCard className="flex-1 flex flex-col min-h-0 overflow-hidden">
            <SectionHeader 
              title="Immutable System Logs" 
              icon={<Terminal className="w-5 h-5" />}
              action={<span className="text-xs font-mono text-gray-500">Tail: last 50 lines</span>}
            />
            
            <div className="flex-1 bg-black border border-gray-800 rounded-lg p-4 font-mono text-xs overflow-y-auto custom-scrollbar leading-relaxed">
              <div className="text-blue-400">[2026-05-17 14:30:01.002] INFO: Session S-8492 Initialized</div>
              <div className="text-gray-400">[2026-05-17 14:30:02.145] DEBUG: Extracting entities via CDP_Parser_v2</div>
              <div className="text-gray-400">[2026-05-17 14:30:03.501] DEBUG: Grounding against VectorDB_Precedents (similarity > 0.85)</div>
              <div className="text-amber-400">[2026-05-17 14:30:04.220] WARN: Statutory Conflict Detected [Art21, PMLA_Sec45]</div>
              <div className="text-blue-400">[2026-05-17 14:30:05.100] INFO: Multi-Agent Debate instantiated (Agents: P, R, B)</div>
              <div className="text-gray-400">[2026-05-17 14:30:05.150] DEBUG: Prompting Agent_P (Temperature: 0.2)</div>
              <div className="text-gray-400">[2026-05-17 14:30:06.800] DEBUG: Response received from Agent_P</div>
              <div className="text-gray-400">[2026-05-17 14:30:07.120] DEBUG: Prompting Agent_R (Temperature: 0.2)</div>
              <div className="text-gray-400">[2026-05-17 14:30:09.450] DEBUG: Response received from Agent_R</div>
              <div className="text-blue-400">[2026-05-17 14:30:10.001] INFO: Delegating to SMT Solver (Z3) for formal verification</div>
              <div className="text-green-400">[2026-05-17 14:30:11.200] SUCCESS: SMT Proof generated (SAT)</div>
              <div className="text-blue-400">[2026-05-17 14:30:12.500] INFO: Final reasoning object compiled.</div>
              <div className="text-gray-500 mt-2">_</div>
            </div>
          </GlassCard>

          <GlassCard className="h-48 flex-shrink-0">
             <SectionHeader 
              title="Audit System" 
              icon={<Key className="w-5 h-5" />}
            />
            <div className="grid grid-cols-2 gap-4">
               <div className="p-3 bg-[#051838] border border-gray-800 rounded-lg">
                  <span className="text-xs text-gray-500 uppercase tracking-wider block mb-1">Hash Verification</span>
                  <span className="text-sm font-mono text-green-400">0x8f4a...2b91 (Valid)</span>
               </div>
               <div className="p-3 bg-[#051838] border border-gray-800 rounded-lg">
                  <span className="text-xs text-gray-500 uppercase tracking-wider block mb-1">Accountability Trace</span>
                  <span className="text-sm font-mono text-blue-400">Garv Parashar (CIO)</span>
               </div>
            </div>
          </GlassCard>
        </div>

        {/* Right: Formal Proofs */}
        <div className="flex flex-col h-full overflow-hidden">
          <GlassCard className="flex-1 flex flex-col min-h-0 overflow-hidden">
            <SectionHeader 
              title="Formal Logic Proof (SMT-LIB v2)" 
              icon={<Binary className="w-5 h-5" />}
              action={<StatusBadge status="verified" label="Z3 Solver" />}
            />
            
            <div className="flex-1 bg-gray-900/80 border border-gray-800 rounded-lg p-4 font-mono text-sm overflow-y-auto custom-scrollbar">
               <pre className="text-gray-300">
{`; Define basic constraints
(declare-const delay_months Int)
(declare-const section_45_met Bool)
(declare-const bail_granted Bool)

; Article 21 constraint (Speedy trial violation threshold)
(assert (=> (> delay_months 18) (= bail_granted true)))

; PMLA Section 45 constraint
(assert (=> (= section_45_met false) (= bail_granted false)))

; Input facts for Case S-8492
(assert (= delay_months 24))
(assert (= section_45_met false))

; Check for contradiction (Are both constraints satisfiable?)
(check-sat)

; CONTRADICTION DETECTED (unsat)

; Applying Constitutional Hierarchy (Art 21 > Sec 45)
; Relaxing Sec 45 constraint
(push)
(assert (=> (> delay_months 18) (= bail_granted true)))
(assert (= delay_months 24))
(check-sat)
(get-model)

> sat
> (model 
>   (define-fun bail_granted () Bool true)
> )`}
               </pre>
            </div>
          </GlassCard>
        </div>

      </div>
    </div>
  );
}
