import unittest
from player import Player

class PlayerTests(unittest.TestCase):
    def test_is_pair_bets_1k(self):
        player = Player()
        game_state = {
            'in_action': 0,
            'small_blind': 3,
            'current_buy_in': 10,
            'players': [
                { 
                    'bet': 10,
                    'hole_cards': [
                        {
                            'rank': '2',
                            'suit': 'hearts'
                        },
                        {
                            'rank': '2',
                            'suit': 'spades'
                        }
                    ] }
            ]
                
            }
        
        self.assertEqual(player.betRequest(game_state), 1000)

    def test_no_pair_checks(self):
        player = Player()
        game_state = {
            'in_action': 0,
            'small_blind': 3,
            'current_buy_in': 10,
            'players': [
                { 
                    'bet': 10,
                    'hole_cards': [
                        {
                            'rank': '2',
                            'suit': 'hearts'
                        },
                        {
                            'rank': '3',
                            'suit': 'spades'
                        }
                    ]
                }
            ]
                
            }
        
        self.assertEqual(player.betRequest(game_state), 3)

    def test_call_amount_larger_100_checks(self):
        player = Player()
        game_state = {
            'in_action': 0,
            'small_blind': 3,
            'current_buy_in': 10,
            'players': [
                { 
                    'bet': 100,
                    'hole_cards': [
                        {
                            'rank': '2',
                            'suit': 'hearts'
                        },
                        {
                            'rank': '3',
                            'suit': 'spades'
                        }
                    ]
                }
            ]
                
            }
        
        self.assertEqual(player.betRequest(game_state), 0)

if __name__ == '__main__':
    unittest.main()