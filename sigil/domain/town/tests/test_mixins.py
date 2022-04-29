from sigil.domain.campaign.entities import Campaign
from sigil.domain.town.entities import Hub


def test_campaign_with_hubs():
    campaign = Campaign(
        name="Test",
    )

    assert campaign.hubs == []

    hub = Hub(
        campaign=campaign,
    )

    campaign.hubs.append(hub)

    assert hub in campaign.hubs
