import React from 'react';
import Link from 'next/link';

export default function AuthLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-[#FAFAFA] flex flex-col justify-center py-12 sm:px-6 lg:px-8 relative overflow-hidden font-sans">
      
      {/* Background decorations */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <div className="absolute -top-40 -right-40 w-96 h-96 rounded-full bg-gray-100 blur-3xl opacity-50"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 rounded-full bg-gray-100 blur-3xl opacity-50"></div>
      </div>

      <div className="sm:mx-auto sm:w-full sm:max-w-md text-center">
        <Link href="/" className="inline-block text-3xl font-serif font-semibold tracking-tight text-gray-900 mb-6 hover:opacity-80 transition-opacity">
          CDP
        </Link>
        <h2 className="mt-2 text-center text-2xl font-serif text-gray-900">
          Enterprise Legal OS
        </h2>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white/80 backdrop-blur-md py-8 px-4 shadow-sm sm:rounded-xl border border-gray-100 sm:px-10">
          {children}
        </div>
        
        {/* Trust Indicators */}
        <div className="mt-8 text-center text-xs text-gray-400 space-y-2">
          <p>Protected by 256-bit encryption & SOC2 compliance.</p>
          <div className="flex justify-center space-x-4">
            <Link href="#" className="hover:text-gray-600 transition-colors">Privacy</Link>
            <Link href="#" className="hover:text-gray-600 transition-colors">Terms</Link>
            <Link href="#" className="hover:text-gray-600 transition-colors">Security</Link>
          </div>
        </div>
      </div>
    </div>
  );
}
