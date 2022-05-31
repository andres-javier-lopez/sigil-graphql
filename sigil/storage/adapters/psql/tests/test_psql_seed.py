from unittest import mock

import pytest

from sigil.storage.adapters.psql.storages import CampaignStorage
from sigil.storage.seed import seed


@pytest.mark.database
async def test_database_seed(db_session):
    async with db_session.begin():
        # run the session in a transaction to avoid errors in the seed command
        campaigns = await CampaignStorage(db_session).list()
        assert len(campaigns) == 0

    with mock.patch(
        "sigil.storage.adapters.psql.manager.async_session",
        return_value=db_session,
    ):
        await seed()

    campaigns = await CampaignStorage(db_session).list()
    assert len(campaigns) > 0
