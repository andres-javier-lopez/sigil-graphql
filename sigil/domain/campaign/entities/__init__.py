from .base import Campaign as BaseCampaign, Party, PlayerCharacter

from sigil.domain.town.entities.mixins import CampaignTownMixin


class Campaign(BaseCampaign, CampaignTownMixin):
    pass
