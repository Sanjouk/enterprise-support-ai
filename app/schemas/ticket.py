from pydantic import BaseModel, Field
from typing import Optional, Literal


class TicketAnalyzeRequest(BaseModel):
    ticket_id: Optional[str] = Field(
        default=None,
        description="The ID of the ticket to analyze.",
        examples=["TICKET-1001"],
    )
    customer_id: Optional[str] = Field(
        default=None,
        description="The ID of the customer associated with the ticket.",
        examples=["CUST-1234"],
    )
    message: str = Field(
        ...,
        description="The content of the ticket message to analyze.",
        min_length=10,
        examples=["I was charged twice and want a refund."],
    )


class TicketAnalyzeResponse(BaseModel):
    ticket_summary: str
    category: Literal["billing", "login", "subscription", "incident", "other"]
    priority: Literal["low", "medium", "high", "urgent"]
    suggested_reply: str
