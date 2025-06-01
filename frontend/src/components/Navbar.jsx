  // src/components/Navbar.jsx
  import React from 'react';
  import './Navbar.css';

  function Navbar() {
    return (
      <nav className="navbar">
        <div className="navbar-container">
          <div className="navbar-brand">
            <h1>NBA Prop Analytics</h1>
          </div>
          
          <ul className="navbar-menu">
            <li className="navbar-item">
              <a href="#home" className="navbar-link">Home</a>
            </li>
            <li className="navbar-item">
              <a href="#teams" className="navbar-link">Teams</a>
            </li>
            <li className="navbar-item">
              <a href="#players" className="navbar-link">Players</a>
            </li>
            <li className="navbar-item">
              <a href="#analytics" className="navbar-link">Analytics</a>
            </li>
            <li className="navbar-item">
              <a href="http://localhost:8000/docs" className="navbar-link" target="_blank" rel="noopener noreferrer">
                API Docs
              </a>
            </li>
          </ul>
          
          <div className="navbar-toggle" id="mobile-menu">
            <span className="bar"></span>
            <span className="bar"></span>
            <span className="bar"></span>
          </div>
        </div>
      </nav>
    );
  }

  export default Navbar;