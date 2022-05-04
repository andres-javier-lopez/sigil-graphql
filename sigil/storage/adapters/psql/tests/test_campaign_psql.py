import pytest

from sigil.domain.entities import Campaign
from sigil.storage.adapters.psql.storages.campaign import CampaignStoragePsql


@pytest.mark.database
async def test_campaign_storage(psql_session, mock_campaign: Campaign):
    storage = CampaignStoragePsql(psql_session)

    await storage.save(mock_campaign)

    campaigns = await storage.list()
    assert campaigns is not None
    assert mock_campaign in campaigns

    campaign = await storage.get(mock_campaign.uuid)
    assert campaign == mock_campaign

    campaign.name = "New name"
    await storage.save(campaign)
    new_campaign = await storage.get(campaign.uuid)
    assert campaign == new_campaign

    await storage.save_all([mock_campaign])

    await storage.delete(campaign.uuid)
    campaigns = await storage.list()
    assert campaign not in campaigns
