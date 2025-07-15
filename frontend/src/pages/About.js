import React from 'react';
import '../App.css';
import Resume from './Resume';

export default function Home() {
  return (
    <div className="home-container">
      {/* Container for photo and text */}
      <div className="header-center">
        <img src="/your-photo.jpg" alt="Manuel Ruiz" className="profile-pic" />
        <div className="header-text">
          <h1>Hi, I'm Manuel Ruiz</h1>
          <div className="subtitle">Software Engineer · Portfolio & Bio</div>
          <a href="mailto:manuelruiz937@outlook.com" className="email-link">manuelruiz937@outlook.com</a>
        </div>
      </div>

      <h2>About Me</h2>
      <p>
        I'm a passionate Software Engineer with experience in full-stack development and a strong focus on building scalable,
        efficient, and user-friendly applications. Skilled in modern technologies including React, Python, and cloud platforms,
        I thrive on solving complex problems and delivering high-quality software solutions. With a collaborative mindset and a
        commitment to continuous learning, I aim to drive innovation and contribute to impactful projects that make a difference.
      </p>

      <Resume />
    </div>
  );
}
