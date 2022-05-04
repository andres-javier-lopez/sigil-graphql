import pytest

from sigil.domain import mocks


@pytest.fixture
def mock_campaign():
    return mocks.mock_campaign()
