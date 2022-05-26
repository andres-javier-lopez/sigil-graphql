from unittest import mock

import pytest

from sigil.storage.adapters.psql.commands import include_storages
from sigil.storage.adapters.psql.storages import CampaignStorage
from sigil.storage.seed import seed


@pytest.mark.database
async def test_database_seed(db_session):
    async with db_session.begin():
        # run the session in a transaction to avoid errors in the seed command
        campaigns = await CampaignStorage(db_session).list()
        assert len(campaigns) == 0

    with mock.patch(
        "sigil.storage.adapters.psql.commands.async_session",
        return_value=db_session,
    ):
        # redecorate the function to avoid any misconfiguration
        psql_seed = include_storages(seed.__wrapped__)
        await psql_seed()

    campaigns = await CampaignStorage(db_session).list()
    assert len(campaigns) > 0
