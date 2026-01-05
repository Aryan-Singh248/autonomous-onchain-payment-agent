const API_BASE = import.meta.env.VITE_API_BASE_URL;

export async function submitIntent(intent) {
  const res = await fetch(`${API_BASE}/payments/intent`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ intent }),
  });

  if (!res.ok) {
    throw new Error("Request failed");
  }

  return res.json();
}
