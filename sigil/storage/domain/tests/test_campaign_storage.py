import pytest

from sigil.domain.entities import Campaign, Party, PlayerCharacter
from sigil.storage.adapters.psql.storages.campaign import (
    CampaignStorage,
    PartyStorage,
    PlayerCharacterStorage,
)
from sigil.storage.adapters.psql.test_utils import psql_session


@pytest.fixture
async def db_session(request):
    if request.config.getoption("--use-database"):
        async with psql_session() as session:
            yield session


@pytest.fixture
def campaign_storage(db_session):
    return CampaignStorage(db_session)


@pytest.mark.database
async def test_campaign_storage(campaign_storage, mock_campaign: Campaign):
    await campaign_storage.save(mock_campaign)

    campaigns = await campaign_storage.list()
    assert campaigns is not None
    assert mock_campaign in campaigns

    campaign = await campaign_storage.get(mock_campaign.uuid)
    assert campaign == mock_campaign

    campaign.name = "New name"
    await campaign_storage.save(campaign)
    new_campaign = await campaign_storage.get(campaign.uuid)
    assert campaign == new_campaign

    await campaign_storage.save_all([mock_campaign])

    await campaign_storage.delete(campaign.uuid)
    campaigns = await campaign_storage.list()
    assert campaign not in campaigns


@pytest.fixture
async def current_campaign(campaign_storage, mock_campaign):
    await campaign_storage.save(mock_campaign)
    return mock_campaign


@pytest.fixture
def player_character_storage(db_session):
    return PlayerCharacterStorage(db_session)


@pytest.mark.database
async def test_player_character_storage(
    player_character_storage,
    current_campaign: Campaign,
    mock_player_character: PlayerCharacter,
    mock_player_characters: list[PlayerCharacter],
):
    player_characters = await player_character_storage.list()
    assert len(player_characters) == 0

    await player_character_storage.save(mock_player_character)
    player_characters = await player_character_storage.list()
    assert len(player_characters) == 1

    await player_character_storage.save_all(mock_player_characters)
    player_characters = await player_character_storage.list()
    assert len(player_characters) == len(mock_player_characters)

    player_character = await player_character_storage.get(mock_player_character.uuid)
    assert player_character == mock_player_character

    player_character.name = "New Name"
    await player_character_storage.save(player_character)
    player_character = await player_character_storage.get(player_character.uuid)
    assert player_character.name == "New Name"

    await player_character_storage.delete(player_character.uuid)
    assert await player_character_storage.get(player_character.uuid) is None
    player_characters = await player_character_storage.list()
    assert player_character not in player_characters


@pytest.fixture
async def current_player_characters(
    player_character_storage, current_campaign, mock_player_characters
):
    await player_character_storage.save_all(mock_player_characters)
    return mock_player_characters


@pytest.fixture
def party_storage(db_session):
    return PartyStorage(db_session)


@pytest.mark.database
async def test_party_storage(
    party_storage,
    player_character_storage,
    current_campaign: Campaign,
    current_player_characters: list[PlayerCharacter],
    mock_party: Party,
    mock_parties: list[Party],
):
    for party in mock_parties:
        await player_character_storage.save_all(party.player_characters)

    parties = await party_storage.list()
    assert len(parties) == 0

    await party_storage.save(mock_party)
    parties = await party_storage.list()
    assert len(parties) == 1

    await party_storage.save_all(mock_parties)
    parties = await party_storage.list()
    assert len(parties) == len(mock_parties)

    party = await party_storage.get(mock_party.uuid)
    party.player_characters = await player_character_storage.list(
        filter={player_character_storage.FILTER.PARTY: party.uuid}
    )
    assert party == mock_party

    party.name = "New Name"
    await party_storage.save(party)
    party = await party_storage.get(party.uuid)
    assert party.name == "New Name"

    await party_storage.delete(party.uuid)
    assert await party_storage.get(party.uuid) is None
    parties = await party_storage.list()
    assert party not in parties
    assert (
        await player_character_storage.list(
            filter={player_character_storage.FILTER.PARTY: party.uuid}
        )
        == []
    )
