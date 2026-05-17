import React, { useState } from 'react';
import './App.css';
import LandingPage from './components/LandingPage';
import Auth from './components/Auth';

function App() {
  const [currentView, setCurrentView] = useState('landing'); // 'landing', 'login', 'signup'

  const navigateTo = (view) => {
    window.scrollTo(0, 0);
    setCurrentView(view);
  };

  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="nav-brand" style={{ cursor: 'pointer' }} onClick={() => navigateTo('landing')}>
          ACCAIS
        </div>
        <div className="nav-links">
          {currentView !== 'landing' && (
            <span className="nav-item" onClick={() => navigateTo('landing')}>
              Platform
            </span>
          )}
          <span 
            className={`nav-item ${currentView === 'login' ? 'active' : ''}`}
            onClick={() => navigateTo('login')}
          >
            Sign In
          </span>
          <button className="btn-primary" onClick={() => navigateTo('signup')}>
            Request Access
          </button>
        </div>
      </nav>

      <main className="main-content">
        {currentView === 'landing' && <LandingPage onNavigate={navigateTo} />}
        {currentView === 'login' && <Auth mode="login" onNavigate={navigateTo} />}
        {currentView === 'signup' && <Auth mode="signup" onNavigate={navigateTo} />}
      </main>
    </div>
  );
}

export default App;
