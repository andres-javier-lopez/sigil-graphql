import pytest

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
    else:
        yield None


@pytest.fixture
def adapter(request):
    return request.param


@pytest.fixture
def campaign_storage(adapter, db_session):
    if adapter == "psql":
        return CampaignStorage(db_session)


@pytest.fixture
def player_character_storage(adapter, db_session):
    if adapter == "psql":
        return PlayerCharacterStorage(db_session)


@pytest.fixture
def party_storage(adapter, db_session):
    if adapter == "psql":
        return PartyStorage(db_session)


@pytest.fixture
async def current_campaign(campaign_storage, mock_campaign):
    await campaign_storage.save(mock_campaign)
    return mock_campaign


@pytest.fixture
@pytest.mark.usefixtures("current_campaign")
async def current_player_characters(player_character_storage, mock_player_characters):
    await player_character_storage.save_all(mock_player_characters)
    return mock_player_characters
