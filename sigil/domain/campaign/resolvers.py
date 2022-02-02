from .entities import Campaign


async def campaigns_resolver(*_):
    return [
        Campaign(name='Test'),
    ]
