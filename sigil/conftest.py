import pytest

from sigil.domain.campaign.entities import mocks as campaign_mocks


@pytest.fixture
def mock_campaign():
    return campaign_mocks.mock_campaign()
