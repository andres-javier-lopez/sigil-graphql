from sigil.domain.town.entities.mixins import CampaignTownMixin

from .base import Campaign as BaseCampaign
from .base import Party, PlayerCharacter


class Campaign(BaseCampaign, CampaignTownMixin):
    pass
