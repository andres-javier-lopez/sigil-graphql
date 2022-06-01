import pytest

from sigil.storage.adapters.psql.manager import StorageManager
from sigil.storage.adapters.psql.test_utils import psql_session


@pytest.fixture
def adapter(request):
    return request.param


@pytest.fixture
async def storages(adapter):
    if adapter == "psql":
        async with psql_session() as session:
            yield StorageManager(session)
        return

    raise Exception(f"no storage manager for {adapter} adapter")


@pytest.fixture
def campaign_storage(storages):
    return storages.campaign_storage


@pytest.fixture
def player_character_storage(storages):
    return storages.player_character_storage


@pytest.fixture
def party_storage(storages):
    return storages.party_storage


@pytest.fixture
def hub_storage(storages):
    return storages.hub_storage


@pytest.fixture
async def current_campaign(campaign_storage, mock_campaign):
    await campaign_storage.save(mock_campaign)
    return mock_campaign


@pytest.fixture
@pytest.mark.usefixtures("current_campaign")
async def current_player_characters(player_character_storage, mock_player_characters):
    await player_character_storage.save_all(mock_player_characters)
    return mock_player_characters
