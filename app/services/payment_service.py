from app.agent.agent import AutonomousPaymentAgent


class PaymentService:
    def __init__(self):
        self.agent = AutonomousPaymentAgent()

    def process_intent(self, intent: str) -> dict:
        return self.agent.run(intent)
