from enum import Enum
from typing import Optional, Union
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field

from sigil.domain.campaign.entities.base import Campaign, PlayerCharacter


class RelationshipStatus(str, Enum):
    FRIENDLY = "FRIENDLY"
    NEUTRAL = "NEUTRAL"
    HOSTILE = "HOSTILE"


class Hub(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid4)
    campaign: Campaign


class NPC(BaseModel):
    pass


class Relationship(BaseModel):
    character: Union[PlayerCharacter, NPC]
    status: RelationshipStatus
    notes: Optional[str]
