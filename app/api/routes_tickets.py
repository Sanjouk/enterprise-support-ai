from fastapi import APIRouter
from app.schemas.ticket import TicketAnalyzeRequest, TicketAnalyzeResponse


router = APIRouter(prefix="/api/v1/tickets", tags=["tickets"])


@router.post(
    "/analyze", response_model=TicketAnalyzeResponse, summary="Analyze a support ticket"
)
def analyze_ticket(payload: TicketAnalyzeRequest) -> TicketAnalyzeResponse:
    text = payload.message.lower()

    if "refund" in text or "charged" in text or "billing" in text:
        category = "billing"
        priority = "high"
        summary = (
            "Customer reports a billing-related issue and may be requesting a refund."
        )
        reply = (
            "Hello, thank you for contacting support. "
            "We have reviewed your billing issue and will verify the charge details."
        )
    elif "login" in text or "password" in text:
        category = "login"
        priority = "medium"
        summary = "Customer cannot access the account."
        reply = (
            "Hello, thank you for contacting support. "
            "We are reviewing your login issue and will guide you through account recovery steps."
        )
    else:
        category = "other"
        priority = "medium"
        summary = "General support request detected."
        reply = (
            "Hello, thank you for contacting support. "
            "We have received your request and will review it shortly."
        )

    return TicketAnalyzeResponse(
        ticket_summary=summary,
        category=category,
        priority=priority,
        suggested_reply=reply,
    )
