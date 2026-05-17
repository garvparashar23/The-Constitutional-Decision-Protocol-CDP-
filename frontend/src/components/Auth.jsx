import React, { useState } from 'react';

const Auth = ({ mode, onNavigate }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  const isLogin = mode === 'login';

  const handleSubmit = (e) => {
    e.preventDefault();
    // Redirect to the Streamlit CDP Dashboard
    alert(isLogin ? `Welcome back, ${email}! Redirecting to your workspace...` : `Access granted for ${email}. Redirecting to your workspace...`);
    window.location.href = 'http://localhost:8501';
  };

  return (
    <div className="auth-container animate-fade-in">
      <div className="auth-card glass-panel">
        <div className="auth-header">
          <h2 className="auth-title">{isLogin ? 'Welcome Back' : 'Request Access'}</h2>
          <p className="auth-subtitle">
            {isLogin ? 'Sign in to access your intelligence workspace.' : 'Join the elite echelon of legal professionals.'}
          </p>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label" htmlFor="email">Email Address</label>
            <input
              type="email"
              id="email"
              className="form-input"
              placeholder="name@firm.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              className="form-input"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn-primary auth-btn">
            {isLogin ? 'Sign In' : 'Submit Request'}
          </button>
        </form>

        <div className="auth-footer">
          {isLogin ? (
            <>
              Don't have an account?{' '}
              <span className="auth-link" onClick={() => onNavigate('signup')}>
                Request Access
              </span>
            </>
          ) : (
            <>
              Already have an account?{' '}
              <span className="auth-link" onClick={() => onNavigate('login')}>
                Sign In
              </span>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default Auth;
