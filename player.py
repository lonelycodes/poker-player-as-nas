class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            call_amount = game_state['current_buy_in'] - game_state['players'][game_state['in_action']]['bet']
            my_player = game_state['players'][game_state['in_action']]
            my_cards = my_player['hole_cards']
            community_cards = game_state['community_cards']
            current_round = game_state['round']

            if (self.is_pair(my_cards[0], my_cards[1])):
                if self.is_high_card(my_cards[0]):
                    print('bet (is high pair): 1000')
                    return 1000
                else:
                    print('bet (is pair): 200')
                    return 200

            if current_round == 0:
                print('bet: ', game_state['small_blind'] * 2)
                return game_state['small_blind'] * 2

            print('call amount: ', call_amount)

            if(call_amount > 100):    
                print('bet (call amount larger than 100): 0')
                return 0

            print('bet (call_amount): ', call_amount)
            return call_amount
        except:
            return 1

    def showdown(self, game_state):
        pass

    def has_triplet(cards):
        return

    def is_pair(self, card1, card2):
        return card1['rank'] == card2['rank']

    def is_high_card(self, card):
        return card['rank'] in ['A', 'K', 'Q', 'J', '10']


    

