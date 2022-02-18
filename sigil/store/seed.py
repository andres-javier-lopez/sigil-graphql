import asyncio

from sigil.store.adapters.psql.seed import init_storage, seed_stores
from sigil.store.interfaces import CampaignStore
from sigil.store.domain.campaign import seed_campaigns


@seed_stores
async def seed(*, stores: dict = None):
    await seed_campaigns(stores[CampaignStore.__name__], number=5)


async def main():
    await init_storage()
    await seed()


if __name__ == '__main__':
    print('Seeding new database')
    asyncio.run(main())
    print('Finished')
