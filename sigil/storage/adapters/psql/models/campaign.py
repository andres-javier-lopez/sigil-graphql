from __future__ import annotations

import enum

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import ENUM, TEXT, UUID
from sqlalchemy.orm import relationship

from sigil.domain.campaign.entities import Campaign, PlayerCharacter
from sigil.domain.town.entities.base import RelationshipStatus

from .base import Base, EntityModel


class CampaignModel(Base, EntityModel):
    __tablename__ = "campaigns"

    uuid = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    name = Column(String, nullable=False)
    description = Column(TEXT)
    notes = Column(TEXT)

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
    campaign = relationship("CampaignModel", lazy="selectin")

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


class Character(enum.Enum):
    PlayerCharacter = "PlayerCharacter"
    NPC = "NPC"


class RelationshipModel(Base):
    __tablename__ = "player_character_relationships"

    player_character_id = Column(
        UUID(as_uuid=True),
        ForeignKey("player_characters.uuid"),
        nullable=False,
        primary_key=True,
    )
    character_id = Column(UUID(as_uuid=True), nullable=False, primary_key=True)
    character_entity = Column(ENUM(Character, name="character_enum"), nullable=False)
    status = Column(
        ENUM(RelationshipStatus, name="relationship_status_enum"), nullable=False
    )
    notes = Column(TEXT)
