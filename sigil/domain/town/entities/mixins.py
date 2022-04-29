from typing import List

from pydantic import BaseModel

from .base import Hub


class CampaignTownMixin(BaseModel):
    hubs: List[Hub] = []
