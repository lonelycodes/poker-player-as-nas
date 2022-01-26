class Player:
    VERSION = "Default Python folding player"

    def is_pair(card1, card2):
        return card1['rank'] == card2['rank']

    def betRequest(self, game_state):
        return 1000
        # my_player = game_state['players']['in_action']
        # my_cards = my_player['hole_cards']
        # if (is_pair(my_cards[0], my_cards[1])):
        #     return 1000

        # return 0

    def showdown(self, game_state):
        pass

    

