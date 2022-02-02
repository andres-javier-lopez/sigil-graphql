from uuid import uuid4

from pydantic import UUID4, BaseModel, Field

from sigil.domain.campaign.entities.base import Campaign


class Hub(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid4)
    campaign: Campaign
