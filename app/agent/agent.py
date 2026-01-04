from app.agent.states import AgentState


class AutonomousPaymentAgent:
    def __init__(self):
        self.state = AgentState.IDLE
        self.context = {}

    def run(self, intent: str):
        print(f"[AGENT] Received intent: {intent}")

        self.context["intent"] = intent
        self.state = AgentState.VALIDATE

        while True:
            print(f"[AGENT] Current state: {self.state.value}")

            if self.state == AgentState.VALIDATE:
                self._validate()

            elif self.state == AgentState.EXECUTE:
                self._execute()

            elif self.state == AgentState.VERIFY:
                self._verify()

            elif self.state == AgentState.RECOVER:
                self._recover()

            elif self.state == AgentState.CONFIRM:
                print("[AGENT] Payment confirmed")
                return {"status": "SUCCESS"}

            elif self.state == AgentState.FAIL:
                print("[AGENT] Payment failed")
                return {"status": "FAILED"}

    def _validate(self):
        print("[AGENT] Validating intent")
        if not self.context.get("intent"):
            self.state = AgentState.FAIL
        else:
            self.state = AgentState.EXECUTE

    def _execute(self):
        print("[AGENT] Executing payment (on-chain)")
        try:
            from app.blockchain.x402_client import send_payment
            from web3 import Web3

            # Controlled test recipient (burn address)
            recipient = "0x000000000000000000000000000000000000dEaD"
            amount_wei = Web3.to_wei(0.001, "ether")

            tx_hash = send_payment(recipient, amount_wei)
            print(f"[AGENT] Transaction sent: {tx_hash}")

            self.context["tx_hash"] = tx_hash
            self.state = AgentState.VERIFY

        except Exception as e:
            print("[AGENT][ERROR] Execution failed:", str(e))
            self.state = AgentState.RECOVER

    def _verify(self):
        print("[AGENT] Verifying transaction (on-chain)")
        try:
            from app.blockchain.verifier import verify_transaction

            tx_hash = self.context.get("tx_hash")
            verified = verify_transaction(tx_hash)

            if verified:
                self.state = AgentState.CONFIRM
            else:
                self.state = AgentState.RECOVER

        except Exception as e:
            print("[AGENT][ERROR] Verification failed:", str(e))
            self.state = AgentState.RECOVER

    def _recover(self):
        print("[AGENT] Recovering from failure")
        self.state = AgentState.FAIL
