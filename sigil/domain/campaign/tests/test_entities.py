from sigil.domain.campaign.entities import Campaign
from sigil.settings import ANON_UUID


def test_campaign():
    campaign = Campaign(
        name="Test",
        user_id=ANON_UUID,
        description="This is a test",
        notes="notes",
        parties=[],
        player_characters=[],
    )

    assert campaign
    assert campaign.uuid
    assert campaign.name == "Test"
