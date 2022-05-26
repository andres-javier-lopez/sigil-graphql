import pytest

from sigil.domain.entities import Campaign, Party, PlayerCharacter
from sigil.storage.adapters.psql.storages.campaign import (
    CampaignStorage,
    PartyStorage,
    PlayerCharacterStorage,
)


@pytest.mark.database
async def test_campaign_storage(psql_session, mock_campaign: Campaign):
    storage = CampaignStorage(psql_session)

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


@pytest.fixture
async def current_campaign(psql_session, mock_campaign):
    storage = CampaignStorage(psql_session)
    await storage.save(mock_campaign)
    await psql_session.commit()
    return mock_campaign


@pytest.mark.database
async def test_player_character_storage(
    psql_session,
    current_campaign: Campaign,
    mock_player_character: PlayerCharacter,
    mock_player_characters: list[PlayerCharacter],
):
    storage = PlayerCharacterStorage(psql_session)

    player_characters = await storage.list()
    assert len(player_characters) == 0

    await storage.save(mock_player_character)
    player_characters = await storage.list()
    assert len(player_characters) == 1

    await storage.save_all(mock_player_characters)
    player_characters = await storage.list()
    assert len(player_characters) == len(mock_player_characters)

    player_character = await storage.get(mock_player_character.uuid)
    assert player_character == mock_player_character

    player_character.name = "New Name"
    await storage.save(player_character)
    player_character = await storage.get(player_character.uuid)
    assert player_character.name == "New Name"

    await storage.delete(player_character.uuid)
    assert await storage.get(player_character.uuid) is None
    player_characters = await storage.list()
    assert player_character not in player_characters


@pytest.fixture
async def current_player_characters(
    psql_session, current_campaign, mock_player_characters
):
    storage = PlayerCharacterStorage(psql_session)
    await storage.save_all(mock_player_characters)
    return mock_player_characters


@pytest.mark.database
async def test_party_storage(
    psql_session,
    current_campaign: Campaign,
    current_player_characters: list[PlayerCharacter],
    mock_party: Party,
    mock_parties: list[Party],
):
    storage = PartyStorage(psql_session)
    player_storage = PlayerCharacterStorage(psql_session)

    for party in mock_parties:
        await player_storage.save_all(party.player_characters)

    parties = await storage.list()
    assert len(parties) == 0

    await storage.save(mock_party)
    parties = await storage.list()
    assert len(parties) == 1

    await storage.save_all(mock_parties)
    parties = await storage.list()
    assert len(parties) == len(mock_parties)

    party = await storage.get(mock_party.uuid)
    party.player_characters = await player_storage.list(
        filter={player_storage.FILTER.PARTY: party.uuid}
    )
    assert party == mock_party

    party.name = "New Name"
    await storage.save(party)
    party = await storage.get(party.uuid)
    assert party.name == "New Name"

    await storage.delete(party.uuid)
    assert await storage.get(party.uuid) is None
    parties = await storage.list()
    assert party not in parties
    assert (
        await player_storage.list(filter={player_storage.FILTER.PARTY: party.uuid})
        == []
    )
