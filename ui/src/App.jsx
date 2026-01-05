import { useState } from "react";
import { submitIntent } from "./api/client";

function App() {
  const [intent, setIntent] = useState("");
  const [status, setStatus] = useState(null);
  const [txHash, setTxHash] = useState(null);
  const [loading, setLoading] = useState(false);

  const submitIntent = async () => {
    setLoading(true);
    setStatus(null);
    setTxHash(null);

    try {
      const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}/payments/intent`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ intent }),
      });

      const data = await res.json();
      setStatus(data.status);
      setTxHash(data.tx_hash || null);
    } catch (err) {
      setStatus("ERROR");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Autonomous On-Chain Payment Agent</h2>

      <input
        style={{ width: "400px", padding: "8px" }}
        placeholder="Enter payment intent"
        value={intent}
        onChange={(e) => setIntent(e.target.value)}
      />

      <br /><br />

      <button onClick={submitIntent} disabled={loading}>
        {loading ? "Processing..." : "Submit Intent"}
      </button>

      <br /><br />

      {status && <p>Status: <b>{status}</b></p>}
      {txHash && <p>Transaction Hash: {txHash}</p>}
    </div>
  );
}

export default App;
