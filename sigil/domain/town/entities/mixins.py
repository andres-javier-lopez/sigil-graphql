from typing import List

from pydantic import BaseModel

from .base import Hub, Relationship


class CampaignTownMixin(BaseModel):
    hubs: List[Hub] = []


class PlayerCharacterTownMixin(BaseModel):
    relationships: List[Relationship] = []
