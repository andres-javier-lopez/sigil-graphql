import pytest

from sigil.domain.entities import Hub
from sigil.storage.domain.town import BaseHubStorage


@pytest.mark.parametrize(
    "adapter",
    [pytest.param("psql", marks=pytest.mark.database)],
    indirect=True,
)
@pytest.mark.usefixtures("current_campaign")
async def test_hub_storage(
    hub_storage: BaseHubStorage, mock_hub: Hub, mock_hubs: list[Hub]
):
    hubs = await hub_storage.list()
    assert len(hubs) == 0

    await hub_storage.save(mock_hub)
    hubs = await hub_storage.list()
    assert len(hubs) == 1

    await hub_storage.save_all(mock_hubs)
    hubs = await hub_storage.list()
    assert len(hubs) == len(mock_hubs)

    hub = await hub_storage.get(mock_hub.uuid)
    assert hub == mock_hub

    hub.name = "New Name"
    await hub_storage.save(hub)
    hub = await hub_storage.get(hub.uuid)
    assert hub.name == "New Name"

    await hub_storage.delete(hub.uuid)
    assert await hub_storage.get(hub.uuid) is None
    hubs = await hub_storage.list()
    assert hub not in hubs
