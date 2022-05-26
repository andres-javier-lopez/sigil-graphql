from __future__ import annotations

from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.dialects.postgresql import TEXT, UUID
from sqlalchemy.orm import relationship

from sigil.domain.entities import Campaign, Party, PlayerCharacter

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

    def get_entity(self) -> Campaign:
        return Campaign(
            uuid=self.uuid,
            user_id=self.user_id,
            name=self.name,
            description=self.description,
            notes=self.notes,
        )


player_character_party_table = Table(
    "player_character_party",
    Base.metadata,
    Column(
        "player_character_id", ForeignKey("player_characters.uuid"), primary_key=True
    ),
    Column("party_id", ForeignKey("parties.uuid"), primary_key=True),
)


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
        ForeignKey("campaigns.uuid"),
        nullable=False,
    )
    campaign = relationship("CampaignModel", lazy="selectin")
    parties = relationship(
        "PartyModel",
        secondary=player_character_party_table,
        back_populates="player_characters",
        lazy="noload",
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

    def get_entity(self) -> PlayerCharacter:
        return PlayerCharacter(
            uuid=self.uuid,
            user_id=self.user_id,
            name=self.name,
            description=self.description,
            notes=self.notes,
            player=self.player,
            uri=self.uri,
            campaign=self.campaign.get_entity(),
        )


class PartyModel(Base, EntityModel):
    __tablename__ = "parties"

    uuid = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    description = Column(TEXT)
    notes = Column(TEXT)
    campaign_id = Column(
        ForeignKey("campaigns.uuid"),
        nullable=False,
    )
    campaign = relationship("CampaignModel", lazy="selectin")
    player_characters = relationship(
        "PlayerCharacterModel",
        secondary=player_character_party_table,
        back_populates="parties",
        lazy="noload",
    )

    db_fields = {
        "uuid",
        "name",
        "description",
        "notes",
        "campaign_id",
    }

    @classmethod
    def from_entity(cls, entity: Party) -> PartyModel:
        return super().from_entity(entity)

    def set_entity(self, entity: Party):
        return super().set_entity(entity)

    def get_entity(self) -> Party:
        return Party(
            uuid=self.uuid,
            name=self.name,
            description=self.description,
            notes=self.notes,
            campaign=self.campaign.get_entity(),
        )
