from __future__ import annotations
from typing import Optional
import uuid

from pydantic import BaseModel, UUID4, Field, HttpUrl


class Campaign(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    description: Optional[str]
    notes: Optional[str]
    parties: list[Party] = []
    player_characters: list[PlayerCharacter] = []


class Party(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    description: Optional[str]
    notes: Optional[str]
    campaign: Campaign
    player_characters: list[PlayerCharacter] = []


class PlayerCharacter(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    description: Optional[str]
    notes: Optional[str]
    player: Optional[str]
    uri: Optional[HttpUrl]
    campalgn: Campaign
    party: Optional[Party]
