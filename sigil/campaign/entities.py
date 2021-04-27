from typing import Optional
import uuid

from pydantic import BaseModel, UUID4, HttpUrl


class Campaign(BaseModel):
    uuid: UUID4
    name: str
    description: Optional[str]

    @staticmethod
    def generate_uuid():
        return uuid.uuid4()


class Party(BaseModel):
    id: str
    name: str
    description: Optional[str]
    campaign: Campaign


class PlayerCharacter(BaseModel):
    id: str
    name: str
    uri: HttpUrl
    campalgn: Campaign
    party: Optional[Party]
