import unittest
from player import Player

class PlayerTests(unittest.TestCase):
    def test_is_pair_bets_1k(self):
        player = Player()
        cards = [ {'rank': '2', 'suit': 'hearts'}, {'rank': '2', 'suit': 'spades'} ]
        game_state = self.get_game_state_mock(hole_cards=cards)
        self.assertEqual(player.betRequest(game_state), 1000)

    def test_no_pair_checks(self):
        player = Player()
        cards = [{'rank': '2', 'suit': 'hearts'}, {'rank': '3', 'suit': 'hearts'}]
        game_state = self.get_game_state_mock(hole_cards=cards)
        self.assertEqual(player.betRequest(game_state), 1)

    def get_game_state_mock(self, currentRound = 0, in_action = 0, small_blind = 3, current_buy_in = 10, hole_cards = [
                        {
                            'rank': '2',
                            'suit': 'hearts'
                        },
                        {
                            'rank': '2',
                            'suit': 'spades'
                        }
                    ]):
                    return {
                        'round': currentRound,
                        'in_action': in_action,
                        'small_blind': small_blind,
                        'current_buy_in': current_buy_in,
                        'players': [
                            { 
                                'bet': 10,
                                'hole_cards': hole_cards
                            }
                        ] 
                    }


if __name__ == '__main__':
    unittest.main()