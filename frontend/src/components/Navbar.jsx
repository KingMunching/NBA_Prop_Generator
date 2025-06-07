  import React from 'react';
  import './Navbar.css';

  function Navbar() {
    return (
      <div>
      <nav className="w-full" >
        <div className="max-w-screen-xl  justify-between mx-auto ">          
          <ul className="flex flex-wrap items-center justify-center space-x-6 p-5 ">
            <li className="navbar-item">
              <a href="#home" className="me-4 hover:underline md:me-6">Home</a>
            </li>
            <li className="navbar-item">
              <a href="#teams" className="me-4 hover:underline md:me-6">Teams</a>
            </li>
            <li className="navbar-item">
              <a href="#players" className="me-4 hover:underline md:me-6">Players</a>
            </li>
            <li className="navbar-item">
              <a href="#analytics" className="me-4 hover:underline md:me-6">Analytics</a>
            </li>
            <li className="navbar-item">
              <a href="http://localhost:8000/docs" className="me-4 hover:underline md:me-6" target="_blank" rel="noopener noreferrer">
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
      </div>
    );
  }

  export default Navbar;