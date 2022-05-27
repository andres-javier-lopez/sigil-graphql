from sigil.domain.campaign.entities.base import Campaign as BaseCampaign
from sigil.domain.campaign.entities.base import Party, PlayerCharacter
from sigil.domain.town.entities.base import Hub
from sigil.domain.town.entities.mixins import CampaignTownMixin


class Campaign(BaseCampaign, CampaignTownMixin):
    pass
