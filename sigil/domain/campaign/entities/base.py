from __future__ import annotations

from typing import ForwardRef, List, Optional
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field, HttpUrl

Party = ForwardRef("Party")
PlayerCharacter = ForwardRef("PlayerCharacter")


class Campaign(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid4)
    user_id: UUID4
    name: str
    description: Optional[str]
    notes: Optional[str]
    parties: List[Party] = []
    player_characters: List[PlayerCharacter] = []

    class Config:
        orm_mode = True


class Party(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid4)
    name: str
    description: Optional[str]
    notes: Optional[str]
    campaign: Campaign
    player_characters: List[PlayerCharacter] = []


class PlayerCharacter(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid4)
    user_id: UUID4
    name: str
    description: Optional[str]
    notes: Optional[str]
    player: Optional[str]
    uri: Optional[HttpUrl]
    campaign: Campaign
    party: Optional[Party]

    class Config:
        orm_mode = True


Campaign.update_forward_refs()
Party.update_forward_refs()
PlayerCharacter.update_forward_refs()
