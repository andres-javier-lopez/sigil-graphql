from sigil.domain.campaign.entities import Campaign, PlayerCharacter, mocks


def test_campaign():
    campaign = mocks.mock_campaign()

    assert campaign
    assert campaign.uuid
    assert isinstance(campaign, Campaign)


def test_player_character(mock_campaign):
    player_character = mocks.mock_player_character(mock_campaign)

    assert player_character
    assert player_character.uuid
    assert isinstance(player_character, PlayerCharacter)
