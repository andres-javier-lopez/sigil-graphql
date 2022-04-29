from __future__ import annotations

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import TEXT, UUID

from sigil.domain.campaign.entities import Campaign

from .base import Base


class CampaignModel(Base):
    __tablename__ = "campaigns"

    uuid = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    description = Column(TEXT)
    notes = Column(TEXT)

    # Required fields when getting from pydantic
    db_fields = {"uuid", "name", "description", "notes"}

    @classmethod
    def from_entity(cls, entity: Campaign) -> CampaignModel:
        return cls(**entity.dict(include=cls.db_fields))

    def set_entity(self, entity: Campaign):
        for field in self.db_fields:
            if field == "uuid":
                continue
            setattr(self, field, getattr(entity, field))
