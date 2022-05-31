from sigil.domain import mocks
from sigil.domain.campaign.entities import Campaign, Party, PlayerCharacter


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


def test_party(mock_campaign):
    player_characters = mocks.mock_player_characters(mock_campaign, 4)
    party = mocks.mock_party(mock_campaign, player_characters)

    assert party
    assert party.uuid
    assert isinstance(party, Party)
    for pc in player_characters:
        assert pc in party.player_characters
