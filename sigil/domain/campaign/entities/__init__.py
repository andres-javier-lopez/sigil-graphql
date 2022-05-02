from sigil.domain.town.entities.mixins import (
    CampaignTownMixin,
    PlayerCharacterTownMixin,
)

from .base import Campaign as BaseCampaign
from .base import Party
from .base import PlayerCharacter as BasePlayerCharacter


class Campaign(BaseCampaign, CampaignTownMixin):
    pass


class PlayerCharacter(BasePlayerCharacter, PlayerCharacterTownMixin):
    pass
