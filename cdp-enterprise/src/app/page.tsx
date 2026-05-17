"use client";

import React from 'react';
import { motion } from 'framer-motion';
import { Shield, Brain, Scale, Search, Layers, FileText, ArrowRight, Lock, Database, ArrowDown, ChevronRight } from 'lucide-react';
import Link from 'next/link';

export default function LandingPage() {
  const fadeUp = {
    hidden: { opacity: 0, y: 30 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.6, ease: "easeOut" } }
  };

  const stagger = {
    hidden: { opacity: 0 },
    visible: { opacity: 1, transition: { staggerChildren: 0.1 } }
  };

  return (
    <div className="min-h-screen bg-[#FAFAFA] text-gray-900 overflow-hidden font-sans">
      
      {/* Navigation */}
      <nav className="fixed w-full top-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          <div className="text-2xl font-serif font-semibold tracking-tight">CDP</div>
          <div className="hidden md:flex space-x-8 text-sm font-medium text-gray-600">
            <Link href="#platform" className="hover:text-gray-900 transition-colors">Platform</Link>
            <Link href="#research" className="hover:text-gray-900 transition-colors">Research</Link>
            <Link href="#security" className="hover:text-gray-900 transition-colors">Security</Link>
          </div>
          <div className="flex items-center space-x-4">
            <Link href="/login" className="text-sm font-medium text-gray-600 hover:text-gray-900 transition-colors">
              Log in
            </Link>
            <Link href="/signup" className="px-5 py-2.5 bg-gray-900 text-white text-sm font-medium rounded-md hover:bg-gray-800 transition-colors">
              Request Demo
            </Link>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-40 pb-20 px-6 max-w-7xl mx-auto flex flex-col items-center text-center">
        <motion.div initial="hidden" animate="visible" variants={fadeUp} className="max-w-4xl">
          <h1 className="text-5xl md:text-7xl font-serif text-gray-900 leading-[1.1] mb-6">
            Computational Constitutional Intelligence for the Next Generation of <span className="text-gray-400">Legal Reasoning.</span>
          </h1>
          <p className="text-lg md:text-xl text-gray-500 mb-10 max-w-2xl mx-auto leading-relaxed">
            AI-powered constitutional analysis, legal reasoning, precedent grounding, and multi-agent formal verification systems designed for elite law firms and enterprises.
          </p>
          <div className="flex flex-col sm:flex-row items-center justify-center space-y-4 sm:space-y-0 sm:space-x-4">
            <Link href="/signup" className="px-8 py-4 bg-gray-900 text-white text-base font-medium rounded-md hover:bg-gray-800 transition-all shadow-lg hover:shadow-xl flex items-center group">
              Get Started <ArrowRight className="ml-2 w-4 h-4 group-hover:translate-x-1 transition-transform" />
            </Link>
            <Link href="#platform" className="px-8 py-4 bg-white text-gray-900 border border-gray-200 text-base font-medium rounded-md hover:bg-gray-50 transition-all flex items-center">
              Explore Platform
            </Link>
          </div>
        </motion.div>

        {/* Abstract Visualization */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.3 }}
          className="mt-20 w-full max-w-5xl h-64 md:h-96 rounded-2xl bg-gradient-to-br from-gray-50 to-gray-100 border border-gray-200 relative overflow-hidden flex items-center justify-center"
        >
          {/* Mock Node Diagram */}
          <div className="absolute w-[800px] h-[800px] border border-gray-200 rounded-full opacity-20 animate-[spin_60s_linear_infinite]" />
          <div className="absolute w-[600px] h-[600px] border border-gray-300 rounded-full opacity-30 animate-[spin_40s_linear_infinite_reverse]" />
          <div className="z-10 text-center">
            <div className="w-16 h-16 bg-white rounded-xl shadow-sm border border-gray-200 flex items-center justify-center mx-auto mb-4">
              <Brain className="text-gray-800 w-8 h-8" />
            </div>
            <p className="text-sm font-medium text-gray-500 uppercase tracking-widest">Grounding Engine Active</p>
          </div>
        </motion.div>
      </section>

      {/* Platform Features Section */}
      <section id="platform" className="py-24 bg-white border-y border-gray-100">
        <div className="max-w-7xl mx-auto px-6">
          <motion.div initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUp} className="mb-16">
            <h2 className="text-3xl md:text-4xl font-serif text-gray-900 mb-4">Advanced Infrastructure.</h2>
            <p className="text-gray-500 text-lg max-w-2xl">Purpose-built modules for constitutional reasoning and formal verification.</p>
          </motion.div>

          <motion.div 
            initial="hidden" whileInView="visible" viewport={{ once: true }} variants={stagger}
            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
          >
            {[
              { icon: <Scale />, title: "Legal Grounding Engine", desc: "Anchors LLM outputs strictly to verifiable statutory and constitutional axioms." },
              { icon: <Brain />, title: "Multi-Agent Verification", desc: "Adversarial separation of powers between generative and adjudicative neural models." },
              { icon: <Layers />, title: "Formal Verification Layer", desc: "Z3 Theorem Prover integration guaranteeing mathematical bounds on generated policy." },
              { icon: <Search />, title: "Precedent Intelligence", desc: "Semantic retrieval architecture comparing novel queries against historical case law." },
              { icon: <FileText />, title: "Explainable AI Decisions", desc: "Cryptographically bound reasoning graphs mapping decisions back to source material." },
              { icon: <Shield />, title: "Conflict Detection", desc: "Automated analysis of regulatory contradictions across jurisdictional boundaries." }
            ].map((feature, idx) => (
              <motion.div key={idx} variants={fadeUp} className="p-8 rounded-xl bg-[#FAFAFA] border border-gray-100 hover:bg-white hover:shadow-xl hover:border-gray-200 transition-all duration-300 group cursor-pointer">
                <div className="w-12 h-12 rounded-lg bg-white border border-gray-200 flex items-center justify-center text-gray-800 mb-6 group-hover:scale-110 transition-transform">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-3 font-serif">{feature.title}</h3>
                <p className="text-gray-500 leading-relaxed text-sm">{feature.desc}</p>
              </motion.div>
            ))}
          </motion.div>
        </div>
      </section>

      {/* Architecture Visualization Section */}
      <section className="py-32 bg-[#FAFAFA]">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <h2 className="text-3xl md:text-4xl font-serif text-gray-900 mb-16">System Architecture Flow</h2>
          
          <div className="flex flex-col md:flex-row items-center justify-between max-w-5xl mx-auto relative">
            {/* Connecting Line */}
            <div className="hidden md:block absolute top-1/2 left-0 w-full h-0.5 bg-gray-200 -z-10 -translate-y-1/2"></div>
            
            {["Scenario Input", "Legal Grounding", "LLM Candidate Gen", "Formal Verification", "Final Decision"].map((step, idx) => (
              <div key={idx} className="flex flex-col items-center mb-8 md:mb-0 relative group">
                <div className="w-4 h-4 rounded-full bg-gray-300 border-4 border-white shadow-sm mb-4 group-hover:bg-gray-800 transition-colors z-10"></div>
                <div className="bg-white px-4 py-3 rounded-lg border border-gray-200 shadow-sm text-sm font-medium text-gray-700 w-40">
                  {step}
                </div>
                {idx < 4 && <ArrowDown className="md:hidden w-5 h-5 text-gray-300 my-4" />}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Comparison & Trust */}
      <section className="py-24 bg-gray-900 text-white">
        <div className="max-w-7xl mx-auto px-6 grid md:grid-cols-2 gap-16 items-center">
          <div>
            <h2 className="text-3xl md:text-4xl font-serif mb-6">Why CDP is Different.</h2>
            <p className="text-gray-400 text-lg mb-8 leading-relaxed">
              Generic LLMs hallucinate case law. Traditional research is manually bottlenecked. The Constitutional Decision Protocol bridges the gap with deterministic AI.
            </p>
            <ul className="space-y-4">
              {["Traditional Legal Research vs CDP", "Manual Analysis vs AI-Augmented", "Generic LLMs vs Grounded Intelligence"].map((item, i) => (
                <li key={i} className="flex items-center text-gray-300 border-b border-gray-800 pb-4">
                  <ChevronRight className="w-5 h-5 mr-3 text-gray-500" />
                  {item}
                </li>
              ))}
            </ul>
          </div>
          <div className="bg-gray-800 rounded-xl p-8 border border-gray-700">
            <div className="flex items-center space-x-4 mb-6 text-gray-400">
              <Database className="w-6 h-6" />
              <span className="font-medium tracking-wide uppercase text-sm">Research-Grade Infrastructure</span>
            </div>
            <p className="text-sm text-gray-400 leading-relaxed mb-6">
              Powered by Next.js, Postgres, Prisma, and robust Python computation. Architected for zero-retention, SOC2 compliant enterprise environments.
            </p>
            <div className="grid grid-cols-2 gap-4">
              <div className="p-4 bg-gray-900 rounded border border-gray-700">
                <div className="text-2xl font-serif">99.9%</div>
                <div className="text-xs text-gray-500 uppercase mt-1">Uptime SLA</div>
              </div>
              <div className="p-4 bg-gray-900 rounded border border-gray-700">
                <div className="text-2xl font-serif">256-bit</div>
                <div className="text-xs text-gray-500 uppercase mt-1">Encryption</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-100 py-12 text-sm text-gray-500">
        <div className="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8">
          <div>
            <div className="font-serif font-semibold text-gray-900 text-lg mb-4">CDP</div>
            <p>Enterprise Legal OS</p>
          </div>
          <div>
            <h4 className="font-medium text-gray-900 mb-4">Platform</h4>
            <ul className="space-y-2">
              <li><Link href="#" className="hover:text-gray-900">Features</Link></li>
              <li><Link href="#" className="hover:text-gray-900">Security</Link></li>
              <li><Link href="#" className="hover:text-gray-900">API Access</Link></li>
            </ul>
          </div>
          <div>
            <h4 className="font-medium text-gray-900 mb-4">Research</h4>
            <ul className="space-y-2">
              <li><Link href="#" className="hover:text-gray-900">Documentation</Link></li>
              <li><Link href="#" className="hover:text-gray-900">Whitepapers</Link></li>
              <li><Link href="#" className="hover:text-gray-900">GitHub</Link></li>
            </ul>
          </div>
          <div>
            <h4 className="font-medium text-gray-900 mb-4">Company</h4>
            <ul className="space-y-2">
              <li><Link href="#" className="hover:text-gray-900">Contact</Link></li>
              <li><Link href="#" className="hover:text-gray-900">Privacy</Link></li>
              <li><Link href="#" className="hover:text-gray-900">Terms</Link></li>
            </ul>
          </div>
        </div>
      </footer>
    </div>
  );
}
