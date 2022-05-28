from sigil.domain.town.actions import HubManager
from sigil.settings import ANON_UUID


async def test_hub_manager(mock_hub_storage, mock_campaign):
    manager = HubManager(mock_hub_storage, ANON_UUID)
    await manager.list_for_campaign(mock_campaign)
    mock_hub_storage.list.assert_called()
    mock_hub_storage.list.call_args.kwargs["filter"][
        mock_hub_storage.FILTER.CAMPAIGN
    ] == mock_campaign.uuid
