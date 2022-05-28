from unittest.mock import Mock

import pytest

from sigil.domain import mocks
from sigil.storage.domain.campaign import (
    BaseCampaignStorage,
    BasePartyStorage,
    BasePlayerCharacterStorage,
)


def _pop_or_none(lst: list):
    try:
        return lst.pop()
    except IndexError:
        return None


@pytest.fixture
def mock_campaign():
    return mocks.mock_campaign()


@pytest.fixture
def mock_campaigns(mock_campaign, n=2):
    return [mock_campaign, *mocks.mock_campaigns(n)]


@pytest.fixture
def mock_campaign_storage(mock_campaigns):
    storage = Mock(spec=BaseCampaignStorage)
    storage.list.return_value = mock_campaigns
    storage.get.side_effect = lambda uuid: _pop_or_none(
        [c for c in mock_campaigns if c.uuid == uuid]
    )
    return storage


@pytest.fixture
def mock_player_character(mock_campaign):
    return mocks.mock_player_character(mock_campaign)


@pytest.fixture
def mock_player_characters(mock_campaign, mock_player_character, n=4):
    return [mock_player_character, *mocks.mock_player_characters(mock_campaign, n)]


@pytest.fixture
def mock_player_character_storage(mock_player_characters):
    storage = Mock(spec=BasePlayerCharacterStorage)
    storage.list.return_value = mock_player_characters
    storage.get.side_effect = lambda uuid: _pop_or_none(
        [pc for pc in mock_player_characters if pc.uuid == uuid]
    )
    return storage


@pytest.fixture
def mock_party(mock_campaign, mock_player_characters):
    return mocks.mock_party(mock_campaign, mock_player_characters)


@pytest.fixture
def mock_parties(mock_campaign, mock_party, n=2):
    return [
        mock_party,
        *[
            mocks.mock_party(
                mock_campaign, mocks.mock_player_characters(mock_campaign, 3)
            )
            for _ in range(n)
        ],
    ]


@pytest.fixture
def mock_party_storage(mock_parties):
    storage = Mock(spec=BasePartyStorage)
    storage.list.return_value = mock_parties
    storage.get.side_effect = lambda uuid: _pop_or_none(
        [p for p in mock_parties if p.uuid == uuid]
    )
    return storage


@pytest.fixture
def mock_hub(mock_campaign):
    return mocks.mock_hub(mock_campaign)


@pytest.fixture
def mock_hubs(mock_campaign, mock_hub):
    return [mock_hub, *mocks.mock_hubs(mock_campaign, number=2)]
