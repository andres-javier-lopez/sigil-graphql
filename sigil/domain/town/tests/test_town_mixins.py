from sigil.domain.entities import Campaign
from sigil.domain.mocks import mock_hub
from sigil.domain.town.entities.mixins import CampaignTownMixin
from sigil.settings import ANON_UUID


def test_campaign_with_hubs():
    campaign = Campaign(
        name="Test",
        user_id=ANON_UUID,
    )
    assert isinstance(campaign, CampaignTownMixin)

    assert campaign.hubs == []

    hub = mock_hub(campaign)
    campaign.hubs.append(hub)

    assert hub in campaign.hubs
