"use client";

import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { 
  Upload, FileText, Scale, Users, CheckCircle2, ShieldAlert,
  ChevronRight, BrainCircuit, Activity, Download, Share2
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { StatusBadge } from '@/components/ui/StatusBadge';
import { SectionHeader } from '@/components/ui/SectionHeader';

export default function WorkspacePage() {
  const [activeTab, setActiveTab] = useState<'input' | 'grounding' | 'debate' | 'verification' | 'decision'>('input');

  const tabs = [
    { id: 'input', label: '1. Scenario Submission', icon: Upload },
    { id: 'grounding', label: '2. Grounding Engine', icon: FileText },
    { id: 'debate', label: '3. Multi-Agent Debate', icon: Users },
    { id: 'verification', label: '4. Formal Verification', icon: Activity },
    { id: 'decision', label: '5. Final Decision', icon: Scale },
  ];

  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide">Constitutional Workspace</h1>
          <p className="text-gray-400 mt-2">Intelligence environment for formal legal reasoning and verification.</p>
        </div>
        <div className="flex space-x-3">
          <button className="flex items-center space-x-2 px-4 py-2 bg-[#0B1120] border border-gray-700 rounded-lg text-sm font-medium text-gray-300 hover:text-white hover:border-gray-500 transition-all">
            <Share2 className="w-4 h-4" />
            <span>Share</span>
          </button>
          <button className="flex items-center space-x-2 px-4 py-2 bg-amber-500/10 border border-amber-500/30 rounded-lg text-sm font-medium text-amber-500 hover:bg-amber-500/20 transition-all">
            <Download className="w-4 h-4" />
            <span>Export Report</span>
          </button>
        </div>
      </div>

      {/* Progress Tabs */}
      <div className="flex items-center justify-between bg-[#0B1120]/60 backdrop-blur-md border border-gray-800/60 rounded-xl p-2 mb-8 overflow-x-auto scrollbar-hide">
        {tabs.map((tab, idx) => (
          <React.Fragment key={tab.id}>
            <button
              onClick={() => setActiveTab(tab.id as any)}
              className={`flex items-center space-x-2 px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                activeTab === tab.id 
                  ? 'bg-amber-500/10 text-amber-500 border border-amber-500/20 shadow-sm' 
                  : 'text-gray-400 hover:text-gray-200 hover:bg-gray-800/50'
              }`}
            >
              <tab.icon className="w-4 h-4" />
              <span className="whitespace-nowrap">{tab.label}</span>
            </button>
            {idx < tabs.length - 1 && <ChevronRight className="w-4 h-4 text-gray-700 flex-shrink-0 mx-2" />}
          </React.Fragment>
        ))}
      </div>

      {/* Main Content Area */}
      <motion.div
        key={activeTab}
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
      >
        {activeTab === 'input' && <ScenarioSubmissionPanel />}
        {activeTab === 'grounding' && <GroundingEnginePanel />}
        {activeTab === 'debate' && <MultiAgentDebatePanel />}
        {activeTab === 'verification' && <FormalVerificationPanel />}
        {activeTab === 'decision' && <FinalDecisionPanel />}
      </motion.div>
    </div>
  );
}

// Sub-components for each panel

function ScenarioSubmissionPanel() {
  return (
    <GlassCard className="min-h-[500px]">
      <SectionHeader 
        title="Legal Scenario Input" 
        description="Provide the facts of the case, upload FIRs, or enter specific constitutional questions."
        icon={<Upload className="w-5 h-5" />}
      />
      
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-400 mb-2">Scenario Description / Facts</label>
            <textarea 
              className="w-full h-64 bg-[#051838]/50 border border-gray-700 rounded-xl p-4 text-gray-200 placeholder-gray-600 focus:outline-none focus:border-amber-500/50 focus:ring-1 focus:ring-amber-500/50 transition-all font-mono text-sm leading-relaxed"
              placeholder="Enter legal scenario here... e.g., 'The petitioner claims their right to privacy under Article 21 was violated when...'"
            />
          </div>
          <div className="flex justify-end">
            <button className="px-6 py-2.5 bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white font-medium rounded-lg shadow-lg shadow-amber-500/20 transition-all">
              Initialize Analysis Pipeline
            </button>
          </div>
        </div>
        
        <div className="space-y-6">
          <div className="border-2 border-dashed border-gray-700 rounded-xl p-8 flex flex-col items-center justify-center text-center bg-gray-800/10 hover:bg-gray-800/30 transition-all cursor-pointer">
            <div className="w-12 h-12 bg-gray-800 rounded-full flex items-center justify-center mb-4">
              <Upload className="w-6 h-6 text-gray-400" />
            </div>
            <h3 className="text-sm font-medium text-gray-200 mb-1">Upload Documents</h3>
            <p className="text-xs text-gray-500">PDF, DOCX, or Images. Supports OCR.</p>
          </div>
          
          <div className="bg-[#0B1120] border border-gray-800 rounded-xl p-4">
            <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">Extracted Entities</h4>
            <div className="space-y-2">
              <div className="flex items-center justify-between text-sm text-gray-400">
                <span>No entities extracted yet.</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </GlassCard>
  );
}

function GroundingEnginePanel() {
  return (
    <div className="space-y-6">
      <SectionHeader 
        title="Constitutional Grounding Engine" 
        description="AI automatically detected legal references, statutes, and applicable precedents."
        icon={<FileText className="w-5 h-5" />}
      />
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <GlassCard hoverEffect>
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-medium text-white flex items-center"><Scale className="w-4 h-4 mr-2 text-amber-500" /> Article 21 (Constitution of India)</h3>
            <StatusBadge status="verified" label="99% Confidence" />
          </div>
          <p className="text-sm text-gray-400 mb-4 leading-relaxed">
            "No person shall be deprived of his life or personal liberty except according to procedure established by law."
          </p>
          <div className="pt-3 border-t border-gray-800 flex justify-between items-center">
            <span className="text-xs text-amber-500/80">Primary Grounding</span>
            <button className="text-xs text-blue-400 hover:underline">View Precedents →</button>
          </div>
        </GlassCard>

        <GlassCard hoverEffect>
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-medium text-white flex items-center"><FileText className="w-4 h-4 mr-2 text-blue-500" /> Section 45 (PMLA, 2002)</h3>
            <StatusBadge status="warning" label="Conflict Detected" />
          </div>
          <p className="text-sm text-gray-400 mb-4 leading-relaxed">
            Conditions for bail under Prevention of Money Laundering Act, requiring satisfaction of court that accused is not guilty.
          </p>
          <div className="pt-3 border-t border-gray-800 flex justify-between items-center">
            <span className="text-xs text-red-400 flex items-center"><ShieldAlert className="w-3 h-3 mr-1"/> Tensions with Art 21</span>
            <button className="text-xs text-blue-400 hover:underline">Analyze Tension →</button>
          </div>
        </GlassCard>
      </div>
    </div>
  );
}

function MultiAgentDebatePanel() {
  return (
    <GlassCard className="min-h-[600px] flex flex-col">
      <SectionHeader 
        title="Live Constitutional Debate" 
        description="Autonomous AI agents debating the merits, precedents, and contradictions of the case."
        icon={<Users className="w-5 h-5" />}
        action={<StatusBadge status="info" label="Simulation Running" className="animate-pulse" />}
      />
      
      <div className="flex-1 bg-[#051838]/50 border border-gray-800 rounded-xl p-6 overflow-y-auto font-mono text-sm space-y-6">
        
        {/* Petitioner Agent */}
        <div className="flex flex-col items-start pr-12">
          <div className="flex items-center space-x-2 mb-2">
            <div className="w-6 h-6 rounded bg-blue-500/20 border border-blue-500/30 flex items-center justify-center">
              <span className="text-xs font-bold text-blue-400">P</span>
            </div>
            <span className="font-semibold text-blue-400">Petitioner Agent</span>
            <span className="text-xs text-gray-600">14:02:45</span>
          </div>
          <div className="bg-gray-800/40 border border-gray-700/50 rounded-2xl rounded-tl-sm px-4 py-3 text-gray-300 shadow-sm">
            Applying the precedent from <span className="text-amber-500/80">Manish Sisodia v. DoE (2024)</span>, prolonged incarceration without trial commencement violates the fundamental right to speedy trial under Article 21, thus superseding the twin conditions of Section 45 PMLA.
          </div>
        </div>

        {/* Respondent Agent */}
        <div className="flex flex-col items-end pl-12">
          <div className="flex items-center space-x-2 mb-2 flex-row-reverse">
            <div className="w-6 h-6 rounded bg-red-500/20 border border-red-500/30 flex items-center justify-center ml-2">
              <span className="text-xs font-bold text-red-400">R</span>
            </div>
            <span className="font-semibold text-red-400">Respondent Agent</span>
            <span className="text-xs text-gray-600 mr-2">14:02:51</span>
          </div>
          <div className="bg-red-900/10 border border-red-900/30 rounded-2xl rounded-tr-sm px-4 py-3 text-gray-300 shadow-sm text-right">
            Objection. The economic severity of the offense under PMLA poses a systemic risk. As per <span className="text-amber-500/80">Vijay Madanlal Choudhary</span>, the twin conditions are constitutional and mandatory. Flight risk has not been mitigated.
          </div>
        </div>

        {/* Bench Agent */}
        <div className="flex flex-col items-center px-12 my-8">
          <div className="bg-amber-500/10 border border-amber-500/30 rounded-lg px-6 py-4 text-center w-full max-w-2xl">
            <div className="flex justify-center mb-2">
              <div className="px-2 py-1 bg-amber-500/20 text-amber-500 text-[10px] uppercase tracking-widest font-bold rounded">Constitutional Bench</div>
            </div>
            <p className="text-amber-100/80 italic">
              Synthesizing arguments. Initiating formal verification to test SMT solver logical consistency between "prolonged delay" (Art 21) vs "mandatory twin conditions" (PMLA Sec 45).
            </p>
          </div>
        </div>

      </div>
    </GlassCard>
  );
}

function FormalVerificationPanel() {
  return (
    <div className="space-y-6">
      <SectionHeader 
        title="Formal Verification Pipeline" 
        description="SMT Solver checks for logical contradictions and legal admissibility."
        icon={<Activity className="w-5 h-5" />}
      />
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="md:col-span-2">
          <GlassCard className="h-full">
            <h3 className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-4">Verification Tree</h3>
            <div className="flex items-center justify-center h-64 border border-dashed border-gray-700/50 rounded-lg bg-[#051838]/50">
              <div className="text-center">
                <BrainCircuit className="w-8 h-8 text-amber-500 mx-auto mb-3 opacity-50" />
                <p className="text-gray-500 text-sm font-mono">[Interactive Proof Tree Visualization]</p>
              </div>
            </div>
          </GlassCard>
        </div>
        
        <div className="space-y-4">
          <GlassCard>
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">Constraints</h3>
            <div className="space-y-2 font-mono text-xs">
              <div className="flex justify-between items-center p-2 bg-green-500/10 border border-green-500/20 rounded">
                <span className="text-gray-300">C1: Right to Speedy Trial</span>
                <CheckCircle2 className="w-3 h-3 text-green-500" />
              </div>
              <div className="flex justify-between items-center p-2 bg-green-500/10 border border-green-500/20 rounded">
                <span className="text-gray-300">C2: Pre-trial Detention &gt; 18mo</span>
                <CheckCircle2 className="w-3 h-3 text-green-500" />
              </div>
              <div className="flex justify-between items-center p-2 bg-red-500/10 border border-red-500/20 rounded">
                <span className="text-gray-300">C3: Sec 45 Twin Conditions Met</span>
                <ShieldAlert className="w-3 h-3 text-red-500" />
              </div>
            </div>
          </GlassCard>
          
          <GlassCard>
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">SMT Result</h3>
            <div className="p-3 bg-amber-500/10 border border-amber-500/30 rounded-lg">
              <span className="text-amber-500 font-bold font-mono text-sm">SATISFIABLE (with exception)</span>
              <p className="text-xs text-amber-100/70 mt-2">
                Logical contradiction resolved via constitutional hierarchy: Fundamental Rights (Art 21) override statutory constraints (PMLA) in cases of extreme delay.
              </p>
            </div>
          </GlassCard>
        </div>
      </div>
    </div>
  );
}

function FinalDecisionPanel() {
  return (
    <GlassCard>
      <SectionHeader 
        title="Final Constitutional Verdict" 
        description="Generated judgment based on verified logic and precedent synthesis."
        icon={<Scale className="w-5 h-5" />}
        action={<StatusBadge status="success" label="Adjudication Complete" />}
      />
      
      <div className="prose prose-invert max-w-none">
        <div className="p-8 bg-[#051838] border border-gray-800 rounded-xl shadow-inner font-serif">
          <h2 className="text-2xl font-bold text-white text-center mb-6 pb-6 border-b border-gray-800">
            CONSTITUTIONAL INTELLIGENCE DECISION
          </h2>
          
          <p className="text-gray-300 leading-loose mb-6">
            Upon formal verification and multi-agent constitutional synthesis, it is determined that the continued pre-trial incarceration of the petitioner violates the fundamental right to a speedy trial as enshrined under <strong>Article 21 of the Constitution of India</strong>.
          </p>
          
          <p className="text-gray-300 leading-loose mb-6">
            While the charges fall under the strictures of the Prevention of Money Laundering Act (PMLA), the delay in trial commencement (exceeding 18 months) triggers the constitutional safeguard recognized in <em>Manish Sisodia v. Directorate of Enforcement</em>. Statutory provisions, including Section 45 of PMLA, cannot be construed as a mechanism for indeterminate punitive detention prior to conviction.
          </p>
          
          <div className="bg-gray-800/30 p-6 rounded-lg border border-gray-700/50 my-8">
            <h3 className="text-lg font-bold text-amber-500 mb-4">Final Order</h3>
            <p className="text-gray-200">
              Bail is granted subject to stringent conditions to mitigate flight risk and ensure witness protection, upholding the constitutional mandate of Article 21 over statutory procedural bars in cases of egregious delay.
            </p>
          </div>
          
          <div className="flex justify-between items-center text-sm text-gray-500 font-sans border-t border-gray-800 pt-6 mt-8">
            <span>Verified via CDP Formal Logic Engine</span>
            <span>Confidence Score: 98.4%</span>
          </div>
        </div>
      </div>
    </GlassCard>
  );
}
