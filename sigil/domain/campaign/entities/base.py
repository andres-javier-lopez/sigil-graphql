from __future__ import annotations
from typing import ForwardRef, List, Optional
import uuid

from pydantic import BaseModel, UUID4, Field, HttpUrl


Party = ForwardRef('Party')
PlayerCharacter = ForwardRef('PlayerCharacter')


class Campaign(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    description: Optional[str]
    notes: Optional[str]
    parties: List[Party] = []
    player_characters: List[PlayerCharacter] = []


class Party(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    description: Optional[str]
    notes: Optional[str]
    campaign: Campaign
    player_characters: List[PlayerCharacter] = []


class PlayerCharacter(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    description: Optional[str]
    notes: Optional[str]
    player: Optional[str]
    uri: Optional[HttpUrl]
    campalgn: Campaign
    party: Optional[Party]


Campaign.update_forward_refs()
Party.update_forward_refs()
PlayerCharacter.update_forward_refs()
