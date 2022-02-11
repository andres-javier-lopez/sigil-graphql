from sigil.domain.campaign.entities import Campaign
from sigil.store.campaign.psql.store import CampaingStorePsql


async def test_campaign_store(mock_campaign: Campaign):
    store = CampaingStorePsql()
    campaigns = await store.list()
    assert campaigns is not None

    await store.save(mock_campaign)

    campaign = await store.get(mock_campaign.uuid)

    await store.save([mock_campaign])

    await store.delete(mock_campaign.uuid)
