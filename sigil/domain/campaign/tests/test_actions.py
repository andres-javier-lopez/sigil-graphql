from sigil.domain.campaign.actions import (
    CampaignManager,
    PartyManager,
    PlayerCharacterManager,
)
from sigil.settings import ANON_UUID


async def test_campaign_manager(mock_campaign_storage):
    manager = CampaignManager(mock_campaign_storage, ANON_UUID)
    await manager.list_all()
    mock_campaign_storage.list.assert_called()
    mock_campaign_storage.list.call_args.kwargs["filter"][
        mock_campaign_storage.FILTER.USER
    ] == ANON_UUID


async def test_player_character_manager(
    mock_player_character_storage, mock_campaign, mock_party
):
    manager = PlayerCharacterManager(mock_player_character_storage, ANON_UUID)

    await manager.list_all()
    mock_player_character_storage.list.assert_called()
    mock_player_character_storage.list.call_args.kwargs["filter"][
        mock_player_character_storage.FILTER.USER
    ] == ANON_UUID

    await manager.list_for_campaign(mock_campaign)
    mock_player_character_storage.list.assert_called()
    mock_player_character_storage.list.call_args.kwargs["filter"][
        mock_player_character_storage.FILTER.CAMPAIGN
    ] == mock_campaign.uuid

    await manager.list_for_party(mock_party)
    mock_player_character_storage.list.assert_called()
    mock_player_character_storage.list.call_args.kwargs["filter"][
        mock_player_character_storage.FILTER.PARTY
    ] == mock_party.uuid


async def test_party_manager(mock_party_storage, mock_campaign, mock_player_character):
    manager = PartyManager(mock_party_storage, ANON_UUID)

    await manager.list_for_campaign(mock_campaign)
    mock_party_storage.list.assert_called()
    mock_party_storage.list.call_args.kwargs["filter"][
        mock_party_storage.FILTER.CAMPAIGN
    ] == mock_campaign.uuid

    await manager.list_for_player(mock_player_character)
    mock_party_storage.list.assert_called()
    mock_party_storage.list.call_args.kwargs["filter"][
        mock_party_storage.FILTER.PLAYER_CHARACTER
    ] == mock_player_character.uuid
