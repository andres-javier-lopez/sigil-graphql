from sigil.domain.campaign.entities import Campaign
from sigil.store.adapters.psql.stores.campaign import CampaingStorePsql


async def test_campaign_store(psql_session, mock_campaign: Campaign):
    store = CampaingStorePsql(psql_session)

    await store.save(mock_campaign)

    campaigns = await store.list()
    assert campaigns is not None
    assert mock_campaign in campaigns

    campaign = await store.get(mock_campaign.uuid)
    assert campaign == mock_campaign

    campaign.name = "New name"
    await store.save(campaign)
    new_campaign = await store.get(campaign.uuid)
    assert campaign == new_campaign

    await store.save_all([mock_campaign])

    await store.delete(campaign.uuid)
    campaigns = await store.list()
    assert campaign not in campaigns
