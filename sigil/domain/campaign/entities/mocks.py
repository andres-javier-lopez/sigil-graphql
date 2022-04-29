from faker import Faker

from .base import Campaign

fake = Faker()


def mock_campaign(i=0) -> Campaign:
    return Campaign(
        name=f"Test Campaign #{i}",
        description=fake.paragraph(),
        notes=fake.paragraph(),
    )


def mock_campaigns(number=1) -> list[Campaign]:
    return [mock_campaign(i) for i in range(number)]
