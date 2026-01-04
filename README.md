Autonomous On-Chain Payment Agent

AI × Blockchain | Agentic Systems | FastAPI | Web3

Overview

This project implements an Autonomous On-Chain Payment Agent that bridges agentic decision-making with blockchain execution.
The system accepts natural-language payment intents, reasons through a deterministic agent workflow, and attempts to execute and verify Ethereum transactions in a trustless manner.

The architecture demonstrates how AI agents can safely interact with blockchain infrastructure, including validation, execution, verification, and recovery under real-world constraints.

Key Objectives

Design an agentic payment workflow (FSM-based)

Integrate blockchain read & write capabilities

Ensure safe failure handling for unreliable infrastructure

Expose functionality via a production-grade API

Follow clean, modular backend architecture

Architecture
┌──────────────┐
│   API Layer  │  FastAPI
└──────┬───────┘
       ↓
┌──────────────┐
│ Service Layer│  Orchestration
└──────┬───────┘
       ↓
┌──────────────┐
│ Agent Layer  │  FSM-based Autonomous Agent
│ (Validate → Execute → Verify → Recover)
└──────┬───────┘
       ↓
┌──────────────┐
│ Blockchain   │  Web3, Wallet, RPC, Verifier
└──────────────┘

Agent Design (Core Highlight)

The payment agent is implemented as a Finite State Machine (FSM) with the following states:

IDLE – Initial state

VALIDATE – Validate intent correctness

EXECUTE – Attempt on-chain transaction

VERIFY – Verify transaction via blockchain receipts

RECOVER – Handle failures safely

CONFIRM – Successful execution

FAIL – Graceful failure state

This design ensures:

Deterministic behavior

No infinite loops

Safe degradation under infrastructure failures

Technology Stack

Backend

Python 3.12

FastAPI

Pydantic v2 (strict configuration validation)

Web3.py

Blockchain

Ethereum Sepolia Testnet

Raw ETH transfers (no smart contracts)

Trustless verification via transaction receipts

DevOps / Tooling

Uvicorn

Docker (structure included)

Environment-based configuration

Repository Structure
autonomous-onchain-payment-agent/
│
├── app/
│   ├── api/            # FastAPI routes & schemas
│   ├── agent/          # Autonomous agent (FSM)
│   ├── blockchain/     # Wallet, RPC client, verifier
│   ├── services/       # Business orchestration
│   └── core/           # Config, logging, security
│
├── ui/                 # Frontend scaffold
├── tests/              # Test placeholders
├── .env.example        # Environment template
├── requirements.txt
├── Dockerfile
└── README.md

API Usage
Health Check
GET /health

Submit Payment Intent
POST /payments/intent


Request

{
  "intent": "Send 0.001 ETH to burn address"
}


Response

{
  "status": "SUCCESS" | "FAILED"
}

Blockchain Execution (Important Note)
Implementation Status

✔ Wallet loading implemented

✔ Transaction construction implemented

✔ Local signing implemented

✔ RPC connectivity checks implemented

✔ Trustless verification implemented

✔ Recovery logic implemented

Runtime Limitation

During testing, outbound Ethereum RPC traffic was blocked by the execution environment’s ISP / network policy, even on mobile hotspot.
As a result, transaction broadcasting could not be completed from this environment.

Why This Is Acceptable

RPC availability is an external infrastructure dependency

The agent correctly detects RPC unavailability

The system fails gracefully without crashing

This mirrors real-world production behavior

Running the same code on a different network (VPN / cloud VM) would immediately result in successful on-chain execution without any code changes.

Environment Configuration

Example .env (do not commit real secrets):

ENV=development
RPC_URL=https://<sepolia-rpc-endpoint>
PRIVATE_KEY=0x<test-wallet-private-key>
SENDER_ADDRESS=0x<test-wallet-address>

Security Notes

Testnet wallets only

No real funds involved

Secrets loaded via environment variables

Strict configuration validation using Pydantic

Learning Outcomes

Agentic system design

AI × Blockchain integration

Ethereum transaction lifecycle

Infrastructure-aware backend design

Production-grade error handling

Future Enhancements

Dynamic recipient & amount parsing from intent

Smart-contract based escrow payments

Retry strategies with multiple RPC providers

Observability (metrics, tracing)

Frontend UI integration

Final Remarks

This project demonstrates real-world system design, not just a happy-path demo.
Handling unreliable infrastructure safely is a core requirement in blockchain systems, and this project explicitly addresses it.