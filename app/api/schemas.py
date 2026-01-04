from pydantic import BaseModel


class PaymentIntentRequest(BaseModel):
    intent: str


class PaymentIntentResponse(BaseModel):
    status: str
