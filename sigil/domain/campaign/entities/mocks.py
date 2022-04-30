from uuid import UUID

from faker import Faker

from sigil.settings import ANON_UUID

from . import Campaign, PlayerCharacter

fake = Faker()


def mock_campaign(i=0) -> Campaign:
    return Campaign(
        name=f"Test Campaign #{i}",
        user_id=UUID(ANON_UUID),
        description=fake.paragraph(),
        notes=fake.paragraph(),
    )


def mock_campaigns(number=1) -> list[Campaign]:
    return [mock_campaign(i) for i in range(number)]


def mock_player_character(campaign: Campaign, i=0) -> PlayerCharacter:
    return PlayerCharacter(
        user_id=UUID(ANON_UUID),
        name=f"Test Character #{i}",
        description=fake.paragraph(),
        notes=fake.paragraph(),
        player=fake.name(),
        uri=fake.uri(),
        campaign=campaign,
    )


def mock_player_characters(campaign: Campaign, number=1) -> list[PlayerCharacter]:
    return [mock_player_character(i) for i in range(number)]
