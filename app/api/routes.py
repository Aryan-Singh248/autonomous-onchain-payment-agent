from fastapi import APIRouter
from app.api.schemas import PaymentIntentRequest, PaymentIntentResponse
from app.services.payment_service import PaymentService

router = APIRouter(prefix="/payments", tags=["Payments"])

payment_service = PaymentService()


@router.post("/intent", response_model=PaymentIntentResponse)
def submit_payment_intent(request: PaymentIntentRequest):
    result = payment_service.process_intent(request.intent)
    return PaymentIntentResponse(status=result["status"])
