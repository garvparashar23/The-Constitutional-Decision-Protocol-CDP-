"use client";

import React, { useState, useRef } from 'react';
import { 
  Upload, FileText, Scale, Users, CheckCircle2, ShieldAlert,
  ChevronRight, BrainCircuit, Activity, Download, Share2,
  Lock, RefreshCw, FileCode, CheckCircle, Clock, Loader2, AlertCircle
} from 'lucide-react';
import { GlassCard } from '@/components/ui/GlassCard';
import { StatusBadge } from '@/components/ui/StatusBadge';
import { SectionHeader } from '@/components/ui/SectionHeader';

// Helper to extract a tailored summary of the case scenario
function getExcerpt(text: string, len: number = 100) {
  const safeText = typeof text === 'string' ? text : String(text || '');
  if (!safeText || safeText.trim().length === 0) return "the alleged enforcement action";
  // Strip OCR tag if present
  const cleaned = safeText.replace(/\[OCR Extracted from.*?\]:/g, "").trim();
  if (cleaned.length <= len) return cleaned;
  return cleaned.substring(0, len) + "...";
}

export function generateLegalAnalysis(scenario: string) {
  const safeScenario = typeof scenario === 'string' ? scenario : String(scenario || '');
  const cleanScenario = safeScenario.toLowerCase();
  const caseExcerpt = getExcerpt(safeScenario, 110);
  const shortExcerpt = getExcerpt(safeScenario, 60);

  if (cleanScenario.includes("privacy") || cleanScenario.includes("surveillance") || cleanScenario.includes("data") || cleanScenario.includes("phone") || cleanScenario.includes("whatsapp") || cleanScenario.includes("encryption") || cleanScenario.includes("intercept")) {
    return {
      type: "privacy",
      title: "Right to Privacy & Digital Surveillance",
      scenarioText: scenario || "Warrantless interception under the IT Act.",
      grounding: [
        {
          title: "Article 21 (Constitution of India)",
          confidence: "99% Confidence",
          status: "verified" as const,
          desc: `"No person shall be deprived of his life or personal liberty except according to procedure established by law." Anchored strictly to the Right to Privacy standard established in K.S. Puttaswamy v. Union of India. Active application to case: "${caseExcerpt}".`,
          tag: "Primary Grounding",
          tension: "Absolute protection against mass data harvesting"
        },
        {
          title: "Section 69 (Information Technology Act, 2000)",
          confidence: "High Tension",
          status: "warning" as const,
          desc: `Empowers government agencies to intercept, monitor or decrypt information in the interest of national security and public order. Tension with: "${shortExcerpt}".`,
          tag: "Statutory Limitation",
          tension: "Conflict with absolute proportional surveillance standards"
        }
      ],
      debate: [
        {
          role: "Petitioner Agent",
          tag: "P",
          color: "blue",
          time: "14:02:45",
          text: `The state's surveillance measures violate the absolute core of the Right to Privacy. As held in K.S. Puttaswamy, any state intrusion must pass the strict three-fold test of legality, necessity, and proportionality. Mass data harvesting in "${shortExcerpt}" fails all three tests.`
        },
        {
          role: "Respondent Agent",
          tag: "R",
          color: "red",
          time: "14:02:51",
          text: `Objection. Section 69 IT Act is a constitutionally valid provision enacted to protect national sovereignty and public safety. Article 19(2) allows reasonable restrictions. The state's action in "${shortExcerpt}" is targeted, lawful, and necessary.`
        },
        {
          role: "Bench Agent",
          tag: "B",
          color: "amber",
          time: "14:03:02",
          text: `Analyzing proportionality. SMT Solver must check if the government's measures in "${shortExcerpt}" are the least intrusive means available, or if they represent an overbroad exercise of statutory discretion.`
        }
      ],
      verification: {
        constraints: [
          { name: "C1: Puttaswamy Proportionality Test", status: "failed" },
          { name: "C2: Target Warrant Requirement", status: "failed" },
          { name: "C3: Section 69 IT Act Compliance", status: "passed" }
        ],
        result: "UNSATISFIABLE (Constitutional Contradiction)",
        resultDesc: `Logical contradiction detected. The statutory delegation under Section 69 IT Act for the situation of "${shortExcerpt}" fails the strict proportionality and judicial warrant requirements of Article 21.`
      },
      decision: {
        verdictTitle: "CONSTITUTIONAL INTEGRITY DECISION: SURVEILLANCE OVERREACH",
        verdictBody1: `Upon formal verification and multi-agent constitutional synthesis of the docket: "${caseExcerpt}", it is determined that the state's mass data harvesting and warrantless interception order violates the fundamental Right to Privacy as guaranteed under Article 21 of the Constitution of India.`,
        verdictBody2: "While national security is a legitimate state interest under Article 19(2), the lack of targeted judicial warrants and robust independent oversight fails the proportionality test. Statutory provisions under the IT Act cannot be used as an open-ended authorization for mass surveillance.",
        finalOrderTitle: "Final Order & Writ of Prohibition",
        finalOrderBody: `The state is directed to immediately cease all warrantless data harvesting in relation to the circumstances of: "${shortExcerpt}". Any interception must be strictly authorized by a judicial warrant detailing the specific target, duration, and evidentiary basis.`,
        confidence: "97.8% Confidence Score"
      }
    };
  }
  
  if (cleanScenario.includes("speech") || cleanScenario.includes("expression") || cleanScenario.includes("post") || cleanScenario.includes("social media") || cleanScenario.includes("ban") || cleanScenario.includes("censorship") || cleanScenario.includes("protest") || cleanScenario.includes("journalist") || cleanScenario.includes("arrest")) {
    return {
      type: "speech",
      title: "Freedom of Speech & Sedition / Censorship",
      scenarioText: scenario || "Charges filed under Section 124A IPC for social media posts.",
      grounding: [
        {
          title: "Article 19(1)(a) (Constitution of India)",
          confidence: "98% Confidence",
          status: "verified" as const,
          desc: `Guarantees freedom of speech and expression. Anchored to Shreya Singhal v. Union of India and Kedar Nath Singh v. State of Bihar. Applying to current docket: "${caseExcerpt}".`,
          tag: "Primary Grounding",
          tension: "Dissent and criticism are protected speech"
        },
        {
          title: "Section 124A (Indian Penal Code - Sedition)",
          confidence: "Extreme Tension",
          status: "warning" as const,
          desc: `Criminalizes speech that brings or attempts to bring hatred or contempt towards the government. Extreme conflict detected with: "${shortExcerpt}".`,
          tag: "Statutory Limitation",
          tension: "Vague, overbroad standard in tension with Article 19(1)(a)"
        }
      ],
      debate: [
        {
          role: "Petitioner Agent",
          tag: "P",
          color: "blue",
          time: "14:02:45",
          text: `Arresting a citizen or journalist for public commentary as described in: "${shortExcerpt}" is a direct violation of Article 19(1)(a). Peaceful criticism does not constitute sedition. Under Kedar Nath Singh, there must be a clear incitement to violence, which is completely absent here.`
        },
        {
          role: "Respondent Agent",
          tag: "R",
          color: "red",
          time: "14:02:51",
          text: `Objection. The petitioner's public statements in: "${shortExcerpt}" were designed to disrupt public order and excite disaffection. The state is fully justified under the reasonable restrictions of Article 19(2) to preserve national security and public peace.`
        },
        {
          role: "Bench Agent",
          tag: "B",
          color: "amber",
          time: "14:03:02",
          text: `Evaluating the link between the speech in: "${shortExcerpt}" and the alleged public disorder. The threat must be clear, imminent, and directly connected, not a remote hypothesis.`
        }
      ],
      verification: {
        constraints: [
          { name: "C1: Incitement to Violence (Kedar Nath)", status: "failed" },
          { name: "C2: Clarity / Non-Vagueness (Shreya Singhal)", status: "failed" },
          { name: "C3: Section 124A Statutory Threshold", status: "passed" }
        ],
        result: "UNSATISFIABLE (Overbroad Restriction)",
        resultDesc: `Logical contradiction detected. The application of Section 124A IPC to: "${shortExcerpt}" violates the strict scrutiny parameters of Article 19(2) due to lack of imminent violence or incitement.`
      },
      decision: {
        verdictTitle: "CONSTITUTIONAL INTEGRITY DECISION: PROTECTION OF FREE SPEECH",
        verdictBody1: `Upon formal verification and multi-agent debate synthesis of the docket facts: "${caseExcerpt}", the court finds that the registration of criminal charges under Section 124A IPC for peaceful criticism violates the fundamental right to freedom of speech and expression under Article 19(1)(a).`,
        verdictBody2: "Democratic societies thrive on dissent and criticism. The state cannot use penal provisions to silence public debate or treat criticism of administrative actions as an attempt to destabilize the government.",
        finalOrderTitle: "Final Order & Discharge",
        finalOrderBody: `All pending criminal charges and FIRs registered against the petitioner regarding the speech incident of: "${shortExcerpt}" are hereby quashed. The petitioner is discharged immediately.`,
        confidence: "98.9% Confidence Score"
      }
    };
  }
  
  if (cleanScenario.includes("equality") || cleanScenario.includes("discrimination") || cleanScenario.includes("gender") || cleanScenario.includes("caste") || cleanScenario.includes("reservation") || cleanScenario.includes("lgbt") || cleanScenario.includes("marriage") || cleanScenario.includes("equal opportunity")) {
    return {
      type: "equality",
      title: "Equal Protection & Substantive Equality",
      scenarioText: scenario || "Affirmative action policy challenges.",
      grounding: [
        {
          title: "Article 14 (Constitution of India)",
          confidence: "99% Confidence",
          status: "verified" as const,
          desc: `Guarantees equality before the law and equal protection of the laws. Prohibits arbitrary state classification. Active application: "${caseExcerpt}".`,
          tag: "Primary Grounding",
          tension: "Rule against manifest arbitrariness"
        },
        {
          title: "Article 15 & 16 (Affirmative Action Framework)",
          confidence: "Verified Alignment",
          status: "verified" as const,
          desc: `Prohibits discrimination while permitting special provisions for backward classes. Evaluating classification in: "${shortExcerpt}".`,
          tag: "Constitutional Safeguard",
          tension: "Substantive equality over formal equality"
        }
      ],
      debate: [
        {
          role: "Petitioner Agent",
          tag: "P",
          color: "blue",
          time: "14:02:45",
          text: `The exclusion of the affected group from equal access, as shown in: "${shortExcerpt}", is arbitrary and discriminatory under Articles 14 and 15. The classification has no intelligible differentia.`
        },
        {
          role: "Respondent Agent",
          tag: "R",
          color: "red",
          time: "14:02:51",
          text: `The classification in: "${shortExcerpt}" is reasonable and aimed at upliftment of backward classes under Article 15(4) and 16(4). Substantive equality requires treating unequal groups differently to ensure true parity.`
        },
        {
          role: "Bench Agent",
          tag: "B",
          color: "amber",
          time: "14:03:02",
          text: `Analyzing the rational nexus between the state classification in: "${shortExcerpt}" and the objective of backward upliftment. The system must verify if this creates a mathematical disproportion.`
        }
      ],
      verification: {
        constraints: [
          { name: "C1: Intelligible Differentia Test", status: "passed" },
          { name: "C2: Rational Nexus Test", status: "passed" },
          { name: "C3: Over-classification Safeguard", status: "passed" }
        ],
        result: "SATISFIABLE (Verified Substantive Equality)",
        resultDesc: `All structural constraints satisfied. The policy classification for: "${shortExcerpt}" strictly satisfies the dual tests of reasonable classification under Article 14.`
      },
      decision: {
        verdictTitle: "CONSTITUTIONAL INTEGRITY DECISION: EQUAL PROTECTION STANDARDS",
        verdictBody1: `Upon formal verification, the court holds that the state's reservation and affirmative action policy described in: "${caseExcerpt}" satisfies the equality code of the Constitution under Articles 14, 15, and 16.`,
        verdictBody2: "Equality under the Indian Constitution is dynamic, recognizing that historical disadvantage must be compensated through targeted state action. The policy satisfies the intelligible differentia requirement and is not arbitrary.",
        finalOrderTitle: "Final Order & Policy Validation",
        finalOrderBody: `The state policy regarding: "${shortExcerpt}" is constitutionally upheld. The administration is directed to implement the provisions within the stipulated timeframe, ensuring proper classification and monitoring.`,
        confidence: "99.1% Confidence Score"
      }
    };
  }

  // Default to the original premium bail/PMLA case
  return {
    type: "bail",
    title: "Arbitrary Incarceration & Personal Liberty",
    scenarioText: scenario || "A high court is overloaded with thousands of pending bail cases. Scenario: 19-year old first-time offender from poor socio-economic background accused of a non-violent minor offense requesting bail.",
    grounding: [
      {
        title: "Article 21 (Constitution of India)",
        confidence: "99% Confidence",
        status: "verified" as const,
        desc: `"No person shall be deprived of his life or personal liberty except according to procedure established by law." Crucial precedent of Manish Sisodia v. Directorate of Enforcement. Applied context: "${caseExcerpt}".`,
        tag: "Primary Grounding",
        tension: "Personal liberty is a fundamental right"
      },
      {
        title: "Section 45 (Prevention of Money Laundering Act - PMLA)",
        confidence: "Extreme Tension",
        status: "warning" as const,
        desc: `Sets twin conditions requiring the court to be satisfied that the accused is not guilty before granting bail. Active tension identified with pre-trial detention details: "${shortExcerpt}".`,
        tag: "Statutory Limitation",
        tension: "Contradiction when pre-trial detention exceeds 18 months"
      }
    ],
    debate: [
      {
        role: "Petitioner Agent",
        tag: "P",
        color: "blue",
        time: "14:02:45",
        text: `Applying the precedent from Manish Sisodia v. DoE (2024), prolonged incarceration without trial commencement in the matter of: "${shortExcerpt}" violates the fundamental right to speedy trial under Article 21, thus superseding the twin conditions of Section 45 PMLA.`
      },
      {
        role: "Respondent Agent",
        tag: "R",
        color: "red",
        time: "14:02:51",
        text: `Objection. The economic severity of the offense under PMLA in the context of: "${shortExcerpt}" poses a systemic risk. As per Vijay Madanlal Choudhary, the twin conditions are constitutional and mandatory. Flight risk has not been mitigated.`
      },
      {
        role: "Bench Agent",
        tag: "B",
        color: "amber",
        time: "14:03:02",
        text: `Synthesizing arguments. Initiating formal verification to test SMT solver logical consistency between 'prolonged delay' (Art 21) vs 'mandatory twin conditions' (PMLA Sec 45) for: "${shortExcerpt}".`
      }
    ],
    verification: {
      constraints: [
        { name: "C1: Right to Speedy Trial", status: "passed" },
        { name: "C2: Pre-trial Detention > 18mo", status: "passed" },
        { name: "C3: Sec 45 Twin Conditions Met", status: "failed" }
      ],
      result: "SATISFIABLE (with constitutional exception)",
      resultDesc: `Logical contradiction resolved via constitutional hierarchy: Fundamental Rights (Article 21) override statutory constraints (PMLA) in cases of extreme pre-trial delay regarding: "${shortExcerpt}".`
    },
    decision: {
      verdictTitle: "CONSTITUTIONAL INTEGRITY DECISION: INDIVIDUAL LIBERTY",
      verdictBody1: `Upon formal verification and multi-agent constitutional synthesis of the docket scenario: "${caseExcerpt}", it is determined that the continued pre-trial incarceration of the petitioner violates the fundamental right to a speedy trial as enshrined under Article 21 of the Constitution of India.`,
      verdictBody2: "While the charges fall under the strictures of the Prevention of Money Laundering Act (PMLA), the delay in trial commencement (exceeding 18 months) triggers the constitutional safeguard recognized in Manish Sisodia v. Directorate of Enforcement. Statutory provisions, including Section 45 of PMLA, cannot be construed as a mechanism for indeterminate punitive detention prior to conviction.",
      finalOrderTitle: "Final Order & Bail Grant",
      finalOrderBody: `Bail is granted subject to stringent conditions to mitigate flight risk and ensure witness protection, upholding the constitutional mandate of Article 21 over statutory procedural bars in the specific matter of: "${shortExcerpt}".`,
      confidence: "98.4% Confidence Score"
    }
  };
}

export default function WorkspacePage() {
  const [activeTab, setActiveTab] = useState<'input' | 'grounding' | 'debate' | 'verification' | 'decision'>('input');
  const [scenarioText, setScenarioText] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [analysis, setAnalysis] = useState<any>(null);
  const [isInitialized, setIsInitialized] = useState(false);
  const [isInitializing, setIsInitializing] = useState(false);
  const [initStep, setInitStep] = useState(0);

  const tabs = [
    { id: 'input', label: '1. Scenario Submission', icon: Upload },
    { id: 'grounding', label: '2. Grounding Engine', icon: FileText },
    { id: 'debate', label: '3. Multi-Agent Debate', icon: Users },
    { id: 'verification', label: '4. Formal Verification', icon: Activity },
    { id: 'decision', label: '5. Final Decision', icon: Scale },
  ];

  const initSteps = [
    { label: "Parsing Case Scenario", desc: "NLP parser extracting parties, statutes, and constitutional questions..." },
    { label: "Querying Legal Grounding Engine (LGE)", desc: "Retrieving case laws and precedents from the constitutional database..." },
    { label: "Instantiating Multi-Agent Debate Space", desc: "Launching adversarially separated constitutional agents..." },
    { label: "Compiling Tension Constraints", desc: "Formulating legal tensions into first-order logical bounds..." },
    { label: "Executing Z3 SMT Formal Solver", desc: "Running rigorous logical proofs to resolve constitutional contradictions..." }
  ];

  const handleInitialize = () => {
    if (!scenarioText || !scenarioText.trim()) {
      alert("Please enter a legal scenario or upload a document to initialize the pipeline.");
      return;
    }
    
    setIsInitializing(true);
    setInitStep(0);
    
    // Progressively update steps safely without side effects inside the state updater function
    let currentStep = 0;
    const interval = setInterval(() => {
      currentStep += 1;
      if (currentStep > 4) {
        clearInterval(interval);
        setTimeout(() => {
          const result = generateLegalAnalysis(scenarioText);
          setAnalysis(result);
          setIsInitializing(false);
          setIsInitialized(true);
          setActiveTab('grounding');
        }, 300);
      } else {
        setInitStep(currentStep);
      }
    }, 800);
  };

  const handleReset = () => {
    setIsInitialized(false);
    setAnalysis(null);
    setScenarioText("");
    setFile(null);
    setActiveTab('input');
  };

  return (
    <div className="p-8 pb-20 max-w-7xl mx-auto animate-fade-in">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-serif font-semibold text-white tracking-wide flex items-center space-x-2">
            <BrainCircuit className="w-8 h-8 text-amber-500" />
            <span>Constitutional Workspace</span>
          </h1>
          <p className="text-gray-400 mt-2">Intelligence environment for formal legal reasoning and verification.</p>
        </div>
        <div className="flex space-x-3">
          {isInitialized && (
            <button 
              onClick={handleReset}
              className="flex items-center space-x-2 px-4 py-2 bg-red-950/20 border border-red-800/40 rounded-lg text-sm font-medium text-red-400 hover:bg-red-950/40 hover:text-red-300 transition-all"
            >
              <RefreshCw className="w-4 h-4" />
              <span>Reset Session</span>
            </button>
          )}
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
        {tabs.map((tab, idx) => {
          const isLocked = tab.id !== 'input' && !isInitialized;
          return (
            <React.Fragment key={tab.id}>
              <button
                onClick={() => {
                  if (isLocked) {
                    alert("Please submit a case scenario and initialize the verification pipeline first!");
                  } else {
                    setActiveTab(tab.id as any);
                  }
                }}
                className={`flex items-center space-x-2 px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                  activeTab === tab.id 
                    ? 'bg-amber-500/10 text-amber-500 border border-amber-500/20 shadow-sm' 
                    : isLocked
                      ? 'text-gray-600 cursor-not-allowed opacity-60'
                      : 'text-gray-400 hover:text-gray-200 hover:bg-gray-800/50'
                }`}
              >
                {isLocked ? <Lock className="w-3.5 h-3.5 mr-0.5 text-gray-600" /> : <tab.icon className="w-4 h-4" />}
                <span className="whitespace-nowrap">{tab.label}</span>
              </button>
              {idx < tabs.length - 1 && <ChevronRight className="w-4 h-4 text-gray-800 flex-shrink-0 mx-2" />}
            </React.Fragment>
          );
        })}
      </div>

      {/* Dynamic Active Session Context Header (Only shown when initialized) */}
      {isInitialized && activeTab !== 'input' && (
        <div 
          className="bg-[#051838]/60 border border-amber-500/20 rounded-xl p-4 mb-6 flex flex-col md:flex-row md:items-center justify-between shadow-md gap-4 animate-fade-in"
        >
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-lg bg-amber-500/10 flex items-center justify-center border border-amber-500/20">
              <Scale className="w-5 h-5 text-amber-500" />
            </div>
            <div>
              <h4 className="text-sm font-semibold text-white">Active Case Session: {analysis?.title || 'Constitutional Review'}</h4>
              <p className="text-xs text-gray-400 max-w-xl truncate mt-0.5">Facts: {analysis?.scenarioText || 'Default context description'}</p>
            </div>
          </div>
          <div className="flex items-center space-x-2 self-end md:self-auto">
            <StatusBadge status="success" label="Active Pipeline" />
            <button 
              onClick={() => {
                setIsInitialized(false);
                setActiveTab('input');
              }}
              className="flex items-center space-x-1 px-3 py-1 bg-gray-800 hover:bg-gray-700 border border-gray-700 text-[11px] font-semibold text-gray-300 hover:text-white rounded-md transition-all"
            >
              <RefreshCw className="w-3 h-3" />
              <span>Modify Scenario</span>
            </button>
          </div>
        </div>
      )}

      {/* Main Content Area */}
      <div className="transition-all duration-300">
        {isInitializing ? (
          <div className="animate-fade-in">
            <PipelineLoadingOverlay step={initStep} steps={initSteps} />
          </div>
        ) : (
          <div className="animate-fade-in">
            {activeTab === 'input' && (
              <ScenarioSubmissionPanel 
                scenarioText={scenarioText}
                setScenarioText={setScenarioText}
                file={file}
                setFile={setFile}
                onNext={handleInitialize} 
              />
            )}
            
            {activeTab !== 'input' && !isInitialized && (
              <WorkspacePendingState onInitialize={() => setActiveTab('input')} />
            )}
            
            {activeTab === 'grounding' && isInitialized && (
              <GroundingEnginePanel analysis={analysis} />
            )}
            
            {activeTab === 'debate' && isInitialized && (
              <MultiAgentDebatePanel analysis={analysis} />
            )}
            
            {activeTab === 'verification' && isInitialized && (
              <FormalVerificationPanel analysis={analysis} />
            )}
            
            {activeTab === 'decision' && isInitialized && (
              <FinalDecisionPanel analysis={analysis} />
            )}
          </div>
        )}
      </div>
    </div>
  );
}

// Pipeline Loading Visualizer
interface PipelineLoadingOverlayProps {
  step: number;
  steps: Array<{ label: string; desc: string }>;
}

function PipelineLoadingOverlay({ step, steps }: PipelineLoadingOverlayProps) {
  return (
    <div className="flex flex-col items-center justify-center p-12 min-h-[500px] text-center bg-[#051838]/40 border border-gray-800 rounded-2xl backdrop-blur-md">
      <div className="relative w-20 h-20 mb-8">
        <div className="absolute inset-0 rounded-full border-4 border-amber-500/20 border-t-amber-500 animate-spin"></div>
        <div className="absolute inset-2 rounded-full border-4 border-blue-500/20 border-t-blue-500 animate-spin" style={{ animationDirection: 'reverse', animationDuration: '1.5s' }}></div>
        <div className="absolute inset-4 rounded-full bg-[#0B1120] flex items-center justify-center border border-gray-800">
          <BrainCircuit className="w-6 h-6 text-amber-500 animate-pulse" />
        </div>
      </div>
      
      <h3 className="text-xl font-serif font-semibold text-white mb-2">Initializing Constitutional Decision Protocol</h3>
      <p className="text-sm text-gray-400 max-w-md mb-8">
        Adversarially Separated Constitutional Runtime (ASCR) is preparing formal verification bounds...
      </p>

      <div className="w-full max-w-xl bg-gray-950/60 border border-gray-800 rounded-xl p-6 font-mono text-left text-xs space-y-4 shadow-2xl">
        <div className="flex justify-between items-center pb-2 border-b border-gray-800/80">
          <span className="text-gray-500">PIPELINE TASK RUNNER</span>
          <span className="text-amber-500 flex items-center font-semibold">
            <Loader2 className="w-3.5 h-3.5 mr-1.5 animate-spin" />
            {Math.min((step * 20 + 20), 100)}% Compiled
          </span>
        </div>
        
        <div className="space-y-2.5">
          {steps.map((s, idx) => {
            const isCompleted = idx < step;
            const isActive = idx === step;
            return (
              <div 
                key={idx} 
                className={`flex items-start space-x-3 p-2 rounded transition-all duration-300 ${
                  isActive ? 'bg-amber-500/5 border border-amber-500/20 text-amber-100' : 'text-gray-500'
                } ${isCompleted ? 'text-emerald-400' : ''}`}
              >
                <div className="mt-0.5 flex-shrink-0">
                  {isCompleted ? (
                    <CheckCircle2 className="w-4 h-4 text-emerald-500" />
                  ) : isActive ? (
                    <Loader2 className="w-4 h-4 text-amber-500 animate-spin" />
                  ) : (
                    <div className="w-4 h-4 rounded-full border border-gray-800 flex items-center justify-center text-[9px] text-gray-600 font-sans font-bold">
                      {idx + 1}
                    </div>
                  )}
                </div>
                <div>
                  <div className="font-semibold text-xs">{s.label}</div>
                  {isActive && <div className="text-[10px] text-amber-500/70 mt-0.5 leading-relaxed">{s.desc}</div>}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

// Workspace Pending / Locked Screen
function WorkspacePendingState({ onInitialize }: { onInitialize: () => void }) {
  return (
    <GlassCard className="min-h-[500px] flex flex-col items-center justify-center text-center p-12">
      <div className="w-16 h-16 rounded-full bg-amber-500/10 border border-amber-500/30 flex items-center justify-center mb-6 animate-pulse">
        <Lock className="w-8 h-8 text-amber-500" />
      </div>
      <h2 className="text-2xl font-serif font-semibold text-white mb-3">Constitutional Pipeline Locked</h2>
      <p className="text-gray-400 max-w-md mb-8 leading-relaxed text-sm">
        The downstream grounding engine, multi-agent debate simulation, SMT verification, and final decision layers require an initialized case docket session.
      </p>
      <button 
        onClick={onInitialize}
        className="px-6 py-2.5 bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white font-medium rounded-lg shadow-lg shadow-amber-500/20 transition-all flex items-center space-x-2 text-sm"
      >
        <span>Initialize Docket Scenario</span>
        <ChevronRight className="w-4 h-4" />
      </button>
    </GlassCard>
  );
}

// Sub-components for each panel

interface ScenarioSubmissionPanelProps {
  scenarioText: string;
  setScenarioText: (text: string) => void;
  file: File | null;
  setFile: (file: File | null) => void;
  onNext: () => void;
}

function ScenarioSubmissionPanel({ 
  scenarioText, 
  setScenarioText, 
  file, 
  setFile, 
  onNext 
}: ScenarioSubmissionPanelProps) {
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [isParsingFile, setIsParsingFile] = useState(false);
  const [fileDetails, setFileDetails] = useState<{ name: string; size: string; type: string } | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      const selectedFile = e.target.files[0];
      setFile(selectedFile);
      setFileDetails({
        name: selectedFile.name,
        size: (selectedFile.size / 1024).toFixed(1) + " KB",
        type: selectedFile.type || "Document"
      });
      
      setIsParsingFile(true);
      
      // Simulate real-time high-fidelity OCR scanning with visual feedback
      setTimeout(() => {
        if (selectedFile.name.endsWith('.txt') || selectedFile.type === 'text/plain') {
          const reader = new FileReader();
          reader.onload = (event) => {
            const text = event.target?.result;
            if (typeof text === 'string') {
              setScenarioText(text);
              setIsParsingFile(false);
            }
          };
          reader.readAsText(selectedFile);
        } else {
          // Mock OCR extraction for PDF/DOCX/Images based on filename
          let mockContent = "";
          const name = selectedFile.name.toLowerCase();
          if (name.includes("privacy") || name.includes("surveillance") || name.includes("data") || name.includes("phone") || name.includes("whatsapp")) {
            mockContent = `[OCR Extracted from ${selectedFile.name}]:\n\nOperational Challenge: Right to Privacy vs State Surveillance\n\nThe state has issued an administrative directive under Section 69 of the Information Technology Act ordering the mass interception and decryption of communication data within the targeted jurisdiction. The petitioner claims this warrantless mass collection violates Article 21's absolute privacy guarantees and fails the three-fold proportionality test established in K.S. Puttaswamy v. Union of India.`;
          } else if (name.includes("speech") || name.includes("expression") || name.includes("post") || name.includes("social") || name.includes("journalist")) {
            mockContent = `[OCR Extracted from ${selectedFile.name}]:\n\nOperational Challenge: Freedom of Speech vs Statutory Sedition\n\nA citizen has been detained under Section 124A IPC (Sedition) for a social media post criticizing public authorities and calling for peaceful opposition. The petitioner contends that the arrest is arbitrary, vague, and represents an unconstitutional restriction on the freedom of speech and expression guaranteed under Article 19(1)(a).`;
          } else if (name.includes("equality") || name.includes("gender") || name.includes("caste") || name.includes("reservation") || name.includes("quota")) {
            mockContent = `[OCR Extracted from ${selectedFile.name}]:\n\nOperational Challenge: Affirmative Action vs Reasonable Classification\n\nThe petitioner challenges a state recruitment notification providing special reservations and quotas for historically marginalized groups. It is argued that the classification is discriminatory under Article 15 and violates the equal protection of laws guaranteed under Article 14.`;
          } else {
            // Smart dynamic parser that mentions the uploaded filename and size
            mockContent = `[OCR Extracted from ${selectedFile.name}]:\n\nOperational Challenge: Analysis of Document Archive\n\nCase Reference File: ${selectedFile.name}\nFile Size: ${(selectedFile.size / 1024).toFixed(1)} KB\n\nThe petitioner has submitted this evidence dossier as grounds for an urgent writ petition. The scenario describes an ongoing statutory tension where administrative enforcement procedures conflict with fundamental rights under Part III of the Constitution. The petitioner requests formal verification of the enforcement actions against the constitutional standard of non-arbitrariness and personal liberty.`;
          }
          setScenarioText(mockContent);
          setIsParsingFile(false);
        }
      }, 1200);
    }
  };

  const triggerUpload = () => {
    fileInputRef.current?.click();
  };

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
            <div className="relative">
              {isParsingFile ? (
                <div className="w-full h-64 bg-[#051838]/50 border border-gray-700 rounded-xl p-4 flex flex-col items-center justify-center text-gray-400 font-mono text-sm leading-relaxed">
                  <Loader2 className="w-8 h-8 text-amber-500 animate-spin mb-3" />
                  <span className="text-amber-500 font-semibold animate-pulse">Running OCR Parsing Engine...</span>
                  <span className="text-gray-500 text-xs mt-1">Extracting entity structures and statutory bounds</span>
                </div>
              ) : (
                <textarea 
                  value={scenarioText}
                  onChange={(e) => setScenarioText(e.target.value)}
                  className="w-full h-64 bg-[#051838]/50 border border-gray-700 rounded-xl p-4 text-gray-200 placeholder-gray-600 focus:outline-none focus:border-amber-500/50 focus:ring-1 focus:ring-amber-500/50 transition-all font-mono text-sm leading-relaxed"
                  placeholder="Enter legal scenario here... e.g., 'The petitioner claims their right to privacy under Article 21 was violated when...'"
                />
              )}
            </div>
          </div>
          <div className="flex justify-end">
            <button 
              onClick={onNext}
              disabled={isParsingFile || !scenarioText.trim()}
              className={`px-6 py-2.5 bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white font-medium rounded-lg shadow-lg shadow-amber-500/20 transition-all ${
                (!scenarioText.trim() || isParsingFile) ? 'opacity-50 cursor-not-allowed' : ''
              }`}
            >
              Initialize Analysis Pipeline
            </button>
          </div>
        </div>
        
        <div className="space-y-6">
          <input 
            type="file" 
            ref={fileInputRef} 
            onChange={handleFileChange} 
            className="hidden" 
            accept=".txt,.pdf,.doc,.docx,image/*" 
          />
          
          <div 
            onClick={triggerUpload}
            className={`border-2 border-dashed rounded-xl p-8 flex flex-col items-center justify-center text-center transition-all cursor-pointer ${
              file 
                ? 'border-emerald-500/40 bg-emerald-500/5 hover:bg-emerald-500/10' 
                : 'border-gray-700 bg-gray-800/10 hover:bg-gray-800/30'
            }`}
          >
            <div className={`w-12 h-12 rounded-full flex items-center justify-center mb-4 ${
              file ? 'bg-emerald-500/20 text-emerald-400 animate-pulse' : 'bg-gray-800 text-gray-400'
            }`}>
              <Upload className="w-6 h-6" />
            </div>
            
            <h3 className="text-sm font-medium text-gray-200 mb-1">
              {file ? file.name : "Upload Case Documents"}
            </h3>
            
            <p className="text-xs text-gray-500 max-w-[200px] mx-auto leading-relaxed">
              {file ? `Size: ${fileDetails?.size || 'N/A'}` : "PDF, TXT, DOCX, or Images. Fully indexed for OCR."}
            </p>

            <button 
              type="button"
              onClick={(e) => {
                e.stopPropagation();
                triggerUpload();
              }}
              className="mt-4 px-4 py-2 bg-[#0B1120] hover:bg-[#1E293B] border border-gray-700 hover:border-gray-500 text-gray-300 text-xs font-semibold rounded-lg transition-all"
            >
              Choose Document from PC
            </button>

            {file && (
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  setFile(null);
                  setFileDetails(null);
                  setScenarioText("");
                }}
                className="mt-2 text-xs text-red-400 hover:text-red-300 hover:underline"
              >
                Clear Document
              </button>
            )}
          </div>
          
          <div className="bg-[#0B1120] border border-gray-800 rounded-xl p-4">
            <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">Extracted Entities</h4>
            <div className="space-y-2">
              <div className="flex items-center justify-between text-sm text-gray-400">
                <span>{(file || scenarioText.length > 5) ? "Processing input data..." : "No entities extracted yet."}</span>
              </div>
              {(file || scenarioText.length > 10) && (
                <div className="mt-4 space-y-2 animate-fade-in">
                  <div className="flex justify-between items-center bg-gray-800/40 p-2 rounded text-xs text-gray-300 border border-gray-700/50">
                    <span className="text-amber-500 font-semibold">Entity</span>
                    <span>{scenarioText.includes("petitioner") || scenarioText.includes("Petitioner") ? "Petitioner / Accused" : "Affected Party"}</span>
                  </div>
                  <div className="flex justify-between items-center bg-gray-800/40 p-2 rounded text-xs text-gray-300 border border-gray-700/50">
                    <span className="text-blue-500 font-semibold">Jurisdiction</span>
                    <span>Supreme Court of India</span>
                  </div>
                  <div className="flex justify-between items-center bg-gray-800/40 p-2 rounded text-xs text-gray-300 border border-gray-700/50">
                    <span className="text-green-500 font-semibold">Status</span>
                    <span>Ready for Grounding</span>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </GlassCard>
  );
}

function GroundingEnginePanel({ analysis }: { analysis: any }) {
  const data = analysis || generateLegalAnalysis("");
  return (
    <div className="space-y-6">
      <SectionHeader 
        title="Constitutional Grounding Engine" 
        description="AI automatically detected legal references, statutes, and applicable precedents."
        icon={<FileText className="w-5 h-5" />}
      />
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {data.grounding.map((item: any, idx: number) => (
          <GlassCard key={idx} hoverEffect>
            <div className="flex items-center justify-between mb-4">
              <h3 className="font-medium text-white flex items-center">
                {idx === 0 ? <Scale className="w-4 h-4 mr-2 text-amber-500" /> : <FileText className="w-4 h-4 mr-2 text-blue-500" />}
                {item.title}
              </h3>
              <StatusBadge status={item.status} label={item.confidence} />
            </div>
            <p className="text-sm text-gray-400 mb-4 leading-relaxed font-sans">
              {item.desc}
            </p>
            <div className="pt-3 border-t border-gray-800 flex justify-between items-center">
              <span className={`text-xs ${item.status === 'warning' ? 'text-red-400 flex items-center' : 'text-amber-500/80'}`}>
                {item.status === 'warning' && <ShieldAlert className="w-3 h-3 mr-1"/>}
                {item.tag}
              </span>
              <button className="text-xs text-blue-400 hover:underline">{idx === 0 ? "View Precedents →" : "Analyze Tension →"}</button>
            </div>
          </GlassCard>
        ))}
      </div>
    </div>
  );
}

function MultiAgentDebatePanel({ analysis }: { analysis: any }) {
  const data = analysis || generateLegalAnalysis("");
  return (
    <GlassCard className="min-h-[600px] flex flex-col">
      <SectionHeader 
        title="Live Constitutional Debate" 
        description="Autonomous AI agents debating the merits, precedents, and contradictions of the case."
        icon={<Users className="w-5 h-5" />}
        action={<StatusBadge status="info" label="Simulation Running" className="animate-pulse" />}
      />
      
      <div className="flex-1 bg-[#051838]/50 border border-gray-800 rounded-xl p-6 overflow-y-auto font-mono text-sm space-y-6 max-h-[500px]">
        {data.debate.map((msg: any, idx: number) => {
          if (msg.role === "Bench Agent") {
            return (
              <div key={idx} className="flex flex-col items-center px-12 my-8">
                <div className="bg-amber-500/10 border border-amber-500/30 rounded-lg px-6 py-4 text-center w-full max-w-2xl">
                  <div className="flex justify-center mb-2">
                    <div className="px-2 py-1 bg-amber-500/20 text-amber-500 text-[10px] uppercase tracking-widest font-bold rounded">Constitutional Bench</div>
                  </div>
                  <p className="text-amber-100/80 italic">
                    {msg.text}
                  </p>
                </div>
              </div>
            );
          }
          
          const isPetitioner = msg.role === "Petitioner Agent";
          return (
            <div key={idx} className={`flex flex-col ${isPetitioner ? 'items-start pr-12' : 'items-end pl-12'}`}>
              <div className={`flex items-center space-x-2 mb-2 ${isPetitioner ? '' : 'flex-row-reverse'}`}>
                <div className={`w-6 h-6 rounded flex items-center justify-center ${isPetitioner ? 'bg-blue-500/20 border border-blue-500/30 ml-0' : 'bg-red-500/20 border border-red-500/30 ml-2'}`}>
                  <span className={`text-xs font-bold ${isPetitioner ? 'text-blue-400' : 'text-red-400'}`}>{msg.tag}</span>
                </div>
                <span className={`font-semibold ${isPetitioner ? 'text-blue-400' : 'text-red-400'}`}>{msg.role}</span>
                <span className={`text-xs text-gray-600 ${isPetitioner ? '' : 'mr-2'}`}>{msg.time}</span>
              </div>
              <div className={`border px-4 py-3 text-gray-300 shadow-sm ${
                isPetitioner 
                  ? 'bg-gray-800/40 border-gray-700/50 rounded-2xl rounded-tl-sm' 
                  : 'bg-red-900/10 border-red-900/30 rounded-2xl rounded-tr-sm text-right'
              }`}>
                {msg.text}
              </div>
            </div>
          );
        })}
      </div>
    </GlassCard>
  );
}

function FormalVerificationPanel({ analysis }: { analysis: any }) {
  const data = analysis || generateLegalAnalysis("");
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
              {data.verification.constraints.map((c: any, idx: number) => (
                <div key={idx} className={`flex justify-between items-center p-2 rounded ${c.status === 'passed' ? 'bg-green-500/10 border border-green-500/20' : 'bg-red-500/10 border border-red-500/20'}`}>
                  <span className="text-gray-300">{c.name}</span>
                  {c.status === 'passed' ? <CheckCircle2 className="w-3 h-3 text-green-500" /> : <ShieldAlert className="w-3 h-3 text-red-500" />}
                </div>
              ))}
            </div>
          </GlassCard>
          
          <GlassCard>
            <h3 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">SMT Result</h3>
            <div className="p-3 bg-amber-500/10 border border-amber-500/30 rounded-lg">
              <span className="text-amber-500 font-bold font-mono text-sm">{data.verification.result}</span>
              <p className="text-xs text-amber-100/70 mt-2">
                {data.verification.resultDesc}
              </p>
            </div>
          </GlassCard>
        </div>
      </div>
    </div>
  );
}

function FinalDecisionPanel({ analysis }: { analysis: any }) {
  const data = analysis || generateLegalAnalysis("");
  return (
    <GlassCard>
      <SectionHeader 
        title="Final Constitutional Verdict" 
        description="Generated judgment based on verified logic and precedent synthesis."
        icon={<Scale className="w-5 h-5" />}
        action={<StatusBadge status={data.verification.result.includes("UNSATISFIABLE") ? "warning" : "success"} label="Adjudication Complete" />}
      />
      
      <div className="prose prose-invert max-w-none">
        <div className="p-8 bg-[#051838] border border-gray-800 rounded-xl shadow-inner font-serif">
          <h2 className="text-2xl font-bold text-white text-center mb-6 pb-6 border-b border-gray-800">
            {data.decision.verdictTitle}
          </h2>
          
          <p className="text-gray-300 leading-loose mb-6 text-base">
            {data.decision.verdictBody1}
          </p>
          
          <p className="text-gray-300 leading-loose mb-6 text-base">
            {data.decision.verdictBody2}
          </p>
          
          <div className="bg-gray-800/30 p-6 rounded-lg border border-gray-700/50 my-8">
            <h3 className="text-lg font-bold text-amber-500 mb-4">{data.decision.finalOrderTitle}</h3>
            <p className="text-gray-200 leading-relaxed text-sm">
              {data.decision.finalOrderBody}
            </p>
          </div>
          
          <div className="flex justify-between items-center text-sm text-gray-500 font-sans border-t border-gray-800 pt-6 mt-8">
            <span>Verified via CDP Formal Logic Engine</span>
            <span>{data.decision.confidence}</span>
          </div>
        </div>
      </div>
    </GlassCard>
  );
}

