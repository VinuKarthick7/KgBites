const API_BASE = "http://127.0.0.1:8000/api"; // Django API base

export async function fetchHello() {
  const res = await fetch(`${API_BASE}/hello/`);
  return res.json();
}
