import pytest

from sigil.domain.campaign.entities import Campaign


@pytest.fixture
def mock_campaign():
    return Campaign(
        name='test',
    )
