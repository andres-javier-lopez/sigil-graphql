from __future__ import annotations

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import TEXT, UUID
from sqlalchemy.orm import relationship

from sigil.domain.entities import Hub

from .base import Base, EntityModel


class HubModel(Base, EntityModel):
    __tablename__ = "hubs"

    uuid = Column(UUID(as_uuid=True), primary_key=True)
    campaign_id = Column(ForeignKey("campaigns.uuid"), nullable=False)
    campaign = relationship("CampaignModel", lazy="selectin")
    name = Column(String, nullable=False)
    description = Column(TEXT)
    notes = Column(TEXT)

    db_fields = {
        "uuid",
        "campaign_id",
        "name",
        "description",
        "notes",
    }

    @classmethod
    def from_entity(cls, entity: Hub) -> HubModel:
        return super().from_entity(entity)

    def set_entity(self, entity: Hub):
        return super().set_entity(entity)

    def get_entity(self) -> Hub:
        return Hub(
            uuid=self.uuid,
            campaign=self.campaign.get_entity(),
            name=self.name,
            description=self.description,
            notes=self.notes,
        )
