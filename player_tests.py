import unittest
from player import Player

class PlayerTests(unittest.TestCase):
    def test_is_pair_bets_1k(self):
        player = Player()
        game_state = {
            'in_action': 0,
            'players': [
                { 'hole_cards': [
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
            'players': [
                { 
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
        
        self.assertEqual(player.betRequest(game_state), 10)

if __name__ == '__main__':
    unittest.main()