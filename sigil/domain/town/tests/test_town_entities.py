from sigil.domain import mocks
from sigil.domain.town.entities import Hub


def test_hub(mock_campaign):
    hub = mocks.mock_hub(mock_campaign)

    assert hub
    assert hub.uuid
    assert isinstance(hub, Hub)
