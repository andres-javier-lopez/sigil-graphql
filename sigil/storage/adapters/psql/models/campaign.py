from __future__ import annotations

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import TEXT, UUID
from sqlalchemy.orm import relationship

from sigil.domain.campaign.entities import Campaign
from sigil.domain.campaign.entities.base import PlayerCharacter

from .base import Base, EntityModel


class CampaignModel(Base, EntityModel):
    __tablename__ = "campaigns"

    uuid = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String, nullable=False)
    description = Column(TEXT)
    notes = Column(TEXT)
    player_characters = relationship(
        "PlayerCharacterModel", back_populates="campaign", lazy="noload"
    )

    # Required fields when getting from pydantic
    db_fields = {"uuid", "user_id", "name", "description", "notes"}

    @classmethod
    def from_entity(cls, entity: Campaign) -> CampaignModel:
        return super().from_entity(entity)

    def set_entity(self, entity: Campaign):
        super().set_entity(entity)


class PlayerCharacterModel(Base, EntityModel):
    __tablename__ = "player_characters"

    uuid = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String, nullable=False)
    description = Column(TEXT)
    notes = Column(TEXT)
    player = Column(String)
    uri = Column(String)
    campaign_id = Column(
        UUID(as_uuid=True),
        ForeignKey("campaigns.uuid"),
        nullable=False,
    )
    campaign = relationship(
        "CampaignModel", back_populates="player_characters", lazy="selectin"
    )

    # Required fields when getting from pydantic
    db_fields = {
        "uuid",
        "user_id",
        "name",
        "description",
        "notes",
        "player",
        "uri",
        "campaign_id",
    }

    @classmethod
    def from_entity(cls, entity: PlayerCharacter) -> PlayerCharacterModel:
        return super().from_entity(entity)

    def set_entity(self, entity: PlayerCharacter):
        super().set_entity(entity)
