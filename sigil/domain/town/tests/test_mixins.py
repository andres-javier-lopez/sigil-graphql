from sigil.domain.campaign.entities import Campaign
from sigil.domain.town.entities import Hub
from sigil.settings import ANON_UUID


def test_campaign_with_hubs():
    campaign = Campaign(
        name="Test",
        user_id=ANON_UUID,
    )

    assert campaign.hubs == []

    hub = Hub(
        campaign=campaign,
    )

    campaign.hubs.append(hub)

    assert hub in campaign.hubs
