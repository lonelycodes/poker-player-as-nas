class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            call_amount = game_state['current_buy_in'] - game_state['players'][game_state['in_action']]['bet']
            my_player = game_state['players'][game_state['in_action']]
            my_cards = my_player['hole_cards']
            current_round = game_state['round']

            if current_round == 0:
                return game_state['small_blind'] * 2

            if(call_amount > 100):
                return 0

            if (self.is_pair(my_cards[0], my_cards[1])):
                return 200

            return game_state['small_blind']
        except:
            return 1

    def showdown(self, game_state):
        pass

    

    def is_pair(self, card1, card2):
        return card1['rank'] == card2['rank']

    

