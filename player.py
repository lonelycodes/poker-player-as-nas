import itertools

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            call_amount = game_state['current_buy_in'] - game_state['players'][game_state['in_action']]['bet']
            my_player = game_state['players'][game_state['in_action']]
            my_cards = my_player['hole_cards']
            community_cards = game_state['community_cards']
            current_round = game_state['round']
            print('current_round:', current_round)
            print('my_cards:', my_cards)
            print('community_cards:', community_cards)

            if (self.is_pair(my_cards[0], my_cards[1])):
                if self.is_high_card(my_cards[0]):
                    print('bet (is high pair): 1000')
                    return my_player['stack']
                else:
                    if(call_amount < 500): 
                        return call_amount + 1
                    else:
                        return 0

            if self.is_high_card(my_cards[0]) and self.is_high_card(my_cards[1]):
                if(call_amount < 300): 
                        return call_amount + 1

            if self.is_high_card(my_cards[0]) or self.is_high_card(my_cards[1]):
                if(call_amount < 200): 
                        return call_amount + 1

            if len(community_cards) == 0 and len(my_cards) == 2:
                self.round_1_strategy(game_state)
            
            if len(community_cards) == 3:
                self.round_2_strategy(game_state)

            if len(community_cards) == 4:
                self.round_3_strategy(game_state)

            if len(community_cards) == 5:
                self.round_4_strategy(game_state)

            if len(community_cards) == 0:
                print('bet: ', game_state['small_blind'] * 2)
                return game_state['small_blind'] * 2

            if(call_amount > 100):    
                print('bet (call amount larger than 100): 0')
                return 0

            print('bet (call_amount): ', call_amount)
            return call_amount
        except:
            return 1

    def round_1_strategy(self, game_state):
        pass

    def round_2_strategy(self, game_state):
        pass

    def round_3_strategy(self, game_state):
        pass

    def round_4_strategy(self, game_state):
        pass

    def round_5_strategy(self, game_state):
        pass

    def showdown(self, game_state):
        pass

    # def has_triplet_with_my_card(my_cards, all_cards):
    #     card_groups = dict()
    #     for card in all_cards:
    #         card_groups[]

    #     # returncards.GroupBy(card=> card.Rank).Count(group=> group.Count() == 2) == 1;
    #     x = dict((k, list(g)))
        


    def is_pair(self, card1, card2):
        return card1['rank'] == card2['rank']

    def is_high_card(self, card):
        return card['rank'] in ['A', 'K', 'Q', 'J', '10']


    

