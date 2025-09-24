import React, { useEffect, useState } from "react";
import { fetchHello } from "../services/api";

function Home() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchHello()
      .then((response) => {
        setData(response);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div style={{ padding: "2rem" }}>Fetching from backend...</div>;
  if (error) return <div style={{ padding: "2rem" }}>Error: {error}</div>;

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Welcome to Django + React 🚀</h1>
      
      {data && (
        <div>
          <h2>Backend Response:</h2>
          <div style={{ 
            backgroundColor: "#f5f5f5", 
            padding: "1rem", 
            borderRadius: "8px",
            fontFamily: "monospace"
          }}>
            <p><strong>Message:</strong> {data.message}</p>
            <p><strong>Timestamp:</strong> {data.timestamp}</p>
            <p><strong>Server:</strong> {data.server}</p>
            <p><strong>Status:</strong> {data.status}</p>
            
            <h3>Available Endpoints:</h3>
            <ul>
              {data.endpoints && Object.entries(data.endpoints).map(([name, url]) => (
                <li key={name}>
                  <strong>{name}:</strong> {url}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
      
      <div style={{ marginTop: "2rem", fontSize: "0.9em", color: "#666" }}>
        <p>💡 <strong>Try this:</strong> Make changes to the Django API in <code>api/views.py</code> and see them reflected here instantly!</p>
      </div>
    </div>
  );
}

export default Home;
