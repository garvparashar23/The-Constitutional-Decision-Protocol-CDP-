import React from 'react';

const LandingPage = ({ onNavigate }) => {
  return (
    <>
      {/* Hero Section */}
      <section className="hero-section animate-fade-in">
        <h1 className="hero-title">
          The AI OS for <span className="text-gradient">Legendary Lawyers</span>
        </h1>
        <p className="hero-subtitle delay-100 animate-fade-in">
          Built for top-tier law firms and in-house teams. Unprecedented capabilities in semantic diff analysis, multi-agent debate, and constitutional reasoning.
        </p>
        <div className="hero-actions delay-200 animate-fade-in">
          <button className="btn-primary" onClick={() => onNavigate('signup')}>Request Access</button>
          <button className="btn-secondary" onClick={() => onNavigate('login')}>Sign In</button>
        </div>
      </section>

      {/* App Preview Mockup */}
      <section className="preview-section delay-300 animate-fade-in">
        <div className="preview-window glass-panel">
          <div className="preview-header">
            <div className="preview-dot red"></div>
            <div className="preview-dot yellow"></div>
            <div className="preview-dot green"></div>
          </div>
          <div className="preview-body" style={{ padding: 0 }}>
            <iframe 
              src="http://localhost:8501/?embed=true" 
              title="ACCAIS Platform Preview"
              style={{ width: '100%', height: '100%', border: 'none', background: '#051838' }}
            />
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="features-section">
        <div className="feature-card glass-panel">
          <div className="feature-icon">⚖️</div>
          <h3 className="feature-title">Legal Diff Engine</h3>
          <p className="feature-desc">Autonomous semantic differential analysis of statutory amendments and complex regulatory changes.</p>
        </div>
        <div className="feature-card glass-panel">
          <div className="feature-icon">🧠</div>
          <h3 className="feature-title">Multi-Agent Debate</h3>
          <p className="feature-desc">Deploy adversarial AI models to stress-test arguments and unearth constitutional contradictions.</p>
        </div>
        <div className="feature-card glass-panel">
          <div className="feature-icon">🛡️</div>
          <h3 className="feature-title">Enterprise Security</h3>
          <p className="feature-desc">SOC2 compliance, rigorous access controls, and zero-retention policies for absolute confidentiality.</p>
        </div>
      </section>
    </>
  );
};

export default LandingPage;
