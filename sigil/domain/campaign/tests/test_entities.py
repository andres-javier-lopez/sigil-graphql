from sigil.domain.campaign.entities import Campaign


def test_campaign():
    campaign = Campaign(
        name="Test",
        description="This is a test",
        notes="notes",
        parties=[],
        player_characters=[],
    )

    assert campaign
    assert campaign.uuid
    assert campaign.name == "Test"
