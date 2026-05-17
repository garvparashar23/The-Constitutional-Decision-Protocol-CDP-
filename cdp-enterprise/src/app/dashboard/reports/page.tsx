"use client";

import React from 'react';
import { 
  FileText, Download, Printer, Settings2, FileSignature, CheckCircle2
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { SectionHeader } from '@/components/ui/SectionHeader';

export default function ReportsPage() {
  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in flex flex-col h-[calc(100vh-4rem)]">
      <div className="flex items-center justify-between mb-8 flex-shrink-0">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide">Report Generation Engine</h1>
          <p className="text-gray-400 mt-2">Professional, publication-ready constitutional and legal memorandums.</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 flex-1 min-h-0">
        
        {/* Left: Wizard/Controls */}
        <div className="lg:col-span-1 flex flex-col space-y-6 overflow-y-auto pr-2 scrollbar-hide">
          <GlassCard>
            <SectionHeader 
              title="Report Parameters" 
              icon={<Settings2 className="w-5 h-5" />}
            />
            
            <div className="space-y-5">
              <div>
                <label className="block text-xs font-medium text-gray-400 mb-1.5 uppercase tracking-wider">Report Type</label>
                <select className="w-full bg-[#051838] border border-gray-800 rounded-lg px-3 py-2 text-sm text-white focus:border-amber-500/50 outline-none appearance-none">
                  <option>Constitutional Memorandum</option>
                  <option>Precedent Analysis Report</option>
                  <option>Legal Risk Assessment</option>
                  <option>Judicial Summary</option>
                </select>
              </div>
              
              <div>
                <label className="block text-xs font-medium text-gray-400 mb-1.5 uppercase tracking-wider">Target Session</label>
                <select className="w-full bg-[#051838] border border-gray-800 rounded-lg px-3 py-2 text-sm text-white focus:border-amber-500/50 outline-none appearance-none">
                  <option>S-8492: PMLA Bail Adjudication</option>
                  <option>S-8491: UAPA Default Bail Analysis</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-400 mb-3 uppercase tracking-wider">Include Sections</label>
                <div className="space-y-2">
                  <label className="flex items-center space-x-2 text-sm text-gray-300">
                    <input type="checkbox" defaultChecked className="rounded border-gray-700 bg-gray-900 text-amber-500 focus:ring-amber-500/50" />
                    <span>Issue Identification</span>
                  </label>
                  <label className="flex items-center space-x-2 text-sm text-gray-300">
                    <input type="checkbox" defaultChecked className="rounded border-gray-700 bg-gray-900 text-amber-500 focus:ring-amber-500/50" />
                    <span>Precedent Analysis</span>
                  </label>
                  <label className="flex items-center space-x-2 text-sm text-gray-300">
                    <input type="checkbox" defaultChecked className="rounded border-gray-700 bg-gray-900 text-amber-500 focus:ring-amber-500/50" />
                    <span>SMT Verification Proofs</span>
                  </label>
                  <label className="flex items-center space-x-2 text-sm text-gray-300">
                    <input type="checkbox" defaultChecked className="rounded border-gray-700 bg-gray-900 text-amber-500 focus:ring-amber-500/50" />
                    <span>Final Legal Opinion</span>
                  </label>
                </div>
              </div>

              <div className="pt-4 border-t border-gray-800/60">
                <button className="w-full py-2.5 bg-amber-500 hover:bg-amber-600 text-gray-900 font-medium rounded-lg transition-colors flex items-center justify-center space-x-2">
                  <FileSignature className="w-4 h-4" />
                  <span>Generate Report</span>
                </button>
              </div>
            </div>
          </GlassCard>

          <GlassCard>
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-4">Export Options</h3>
            <div className="grid grid-cols-2 gap-3">
              <button className="flex items-center justify-center space-x-2 p-3 bg-gray-800/40 hover:bg-gray-800 rounded-lg border border-gray-700 hover:border-gray-500 transition-all text-sm text-gray-300">
                <Download className="w-4 h-4" />
                <span>PDF</span>
              </button>
              <button className="flex items-center justify-center space-x-2 p-3 bg-gray-800/40 hover:bg-gray-800 rounded-lg border border-gray-700 hover:border-gray-500 transition-all text-sm text-gray-300">
                <Download className="w-4 h-4" />
                <span>DOCX</span>
              </button>
              <button className="flex items-center justify-center space-x-2 p-3 bg-gray-800/40 hover:bg-gray-800 rounded-lg border border-gray-700 hover:border-gray-500 transition-all text-sm text-gray-300 col-span-2">
                <Printer className="w-4 h-4" />
                <span>Print Document</span>
              </button>
            </div>
          </GlassCard>
        </div>

        {/* Right: Document Preview */}
        <div className="lg:col-span-2 h-full overflow-y-auto pb-4 scrollbar-hide">
          <div className="bg-white text-black p-10 md:p-16 rounded-sm shadow-2xl mx-auto max-w-3xl min-h-[1056px] font-serif relative">
            {/* Watermark */}
            <div className="absolute inset-0 flex items-center justify-center pointer-events-none opacity-5">
              <span className="text-9xl font-bold uppercase rotate-45 tracking-widest">DRAFT</span>
            </div>
            
            <div className="text-center border-b-2 border-black pb-6 mb-8 relative z-10">
              <h1 className="text-3xl font-bold uppercase tracking-wider">Constitutional Memorandum</h1>
              <p className="text-gray-600 mt-2 italic">Generated by Constitutional Decision Protocol</p>
              <p className="text-sm mt-4 font-sans">Date: {new Date().toLocaleDateString()}</p>
            </div>

            <div className="space-y-6 text-sm leading-relaxed text-justify relative z-10">
              <section>
                <h2 className="text-xl font-bold mb-3 uppercase tracking-wide">1. Issue Identification</h2>
                <p>The primary issue concerns the continued pre-trial incarceration of the petitioner exceeding 18 months, invoking the fundamental right to a speedy trial under Article 21 of the Constitution of India, juxtaposed against the restrictive twin conditions for bail stipulated under Section 45 of the Prevention of Money Laundering Act, 2002.</p>
              </section>

              <section>
                <h2 className="text-xl font-bold mb-3 uppercase tracking-wide">2. Precedent Analysis</h2>
                <p>An analysis of landmark jurisprudence reveals a consistent judicial trend prioritizing Article 21 over statutory restrictions in cases of egregious delay. Notably, in <strong>Manish Sisodia v. Directorate of Enforcement (2024)</strong>, the Hon'ble Supreme Court affirmed that the right to a speedy trial constitutes a fundamental right, the deprivation of which necessitates the granting of bail, notwithstanding the stringent provisions of PMLA.</p>
              </section>

              <section>
                <h2 className="text-xl font-bold mb-3 uppercase tracking-wide">3. Formal Verification Summary</h2>
                <p>The CDP Formal Verification Engine analyzed the logical constraints presented by both the statute and the constitutional provision. The SMT solver verified a contradiction between the absolute application of Section 45 and the temporal guarantees of Article 21. Applying the hierarchy of laws, the solver validated the primacy of the constitutional mandate.</p>
                <div className="mt-3 p-4 border border-gray-300 bg-gray-50 font-mono text-xs">
                   <div className="flex items-center text-green-700 mb-1">
                      <CheckCircle2 className="w-3 h-3 mr-1" />
                      <span>Logical Consistency Verified: True</span>
                   </div>
                   <div className="flex items-center text-green-700">
                      <CheckCircle2 className="w-3 h-3 mr-1" />
                      <span>Constitutional Primacy Applied: True</span>
                   </div>
                </div>
              </section>

              <section>
                <h2 className="text-xl font-bold mb-3 uppercase tracking-wide">4. Final Legal Opinion</h2>
                <p>Based on the synthesized constitutional reasoning and verified logical proofs, it is legally sound and constitutionally mandated to grant bail in this specific scenario, as the delayed commencement of trial renders the continued enforcement of the Section 45 twin conditions a violation of Article 21.</p>
              </section>
            </div>
            
            <div className="mt-20 pt-8 border-t border-gray-300 flex justify-between items-end relative z-10">
               <div>
                  <div className="border-b border-black w-48 mb-2"></div>
                  <p className="text-xs uppercase font-sans tracking-wider">Digital Signature</p>
               </div>
               <p className="text-xs text-gray-500 font-sans">Page 1 of 1</p>
            </div>

          </div>
        </div>
        
      </div>
    </div>
  );
}
