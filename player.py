class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        my_player = game_state['players'][game_state['in_action']]
        my_cards = my_player['hole_cards']
        if (self.is_pair(my_cards[0], my_cards[1])):
            return 1000

        return 10

    def showdown(self, game_state):
        pass

    def is_pair(self, card1, card2):
        return card1['rank'] == card2['rank']

    

