import React from 'react';
import '../App.css'; // Use your global styles

export default function Home() {
  return (
    <div className="home-hero" style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      minHeight: "70vh",
      background: "none"
    }}>
      {/* Hero section */}
      <img
        src="/your-photo.jpg"
        alt="Manuel Ruiz"
        className="home-hero-photo"
        style={{
          width: 120,
          height: 120,
          borderRadius: "50%",
          border: "3px solid #5bc0de",
          marginBottom: 20,
          objectFit: "cover"
        }}
      />
      <h1 style={{
        fontSize: "2.7rem",
        fontWeight: "bold",
        marginBottom: 6,
        textAlign: "center"
      }}>
        Manuel Ruiz
      </h1>
      <h2 style={{
        fontSize: "1.4rem",
        color: "#555",
        marginBottom: 18,
        textAlign: "center"
      }}>
        Full Stack Software Engineer
      </h2>
      <p style={{
        maxWidth: 480,
        fontSize: "1.15rem",
        color: "#444",
        textAlign: "center",
        marginBottom: 30
      }}>
        Building modern, scalable, and user-friendly web applications. Passionate about learning, collaboration, and delivering high-quality solutions.
      </p>
      <div style={{ display: "flex", gap: 18, marginBottom: 40 }}>
        <a href="/about" className="btn btn-primary" style={{
          padding: "12px 28px",
          borderRadius: 24,
          background: "#007bff",
          color: "#fff",
          fontWeight: 600,
          textDecoration: "none",
          fontSize: "1.08rem",
        }}>
          About Me
        </a>
        <a href="/projects" className="btn btn-outline" style={{
          padding: "12px 28px",
          borderRadius: 24,
          background: "#fff",
          color: "#007bff",
          border: "2px solid #007bff",
          fontWeight: 600,
          textDecoration: "none",
          fontSize: "1.08rem",
        }}>
          See My Projects
        </a>
      </div>
      {/* (Optional: add featured projects or social links here) */}
    </div>
  );
}
