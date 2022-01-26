import itertools

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        try:
            call_amount = game_state['current_buy_in'] - game_state['players'][game_state['in_action']]['bet']
            my_player = game_state['players'][game_state['in_action']]
            my_cards = my_player['hole_cards']
            community_cards = game_state['community_cards']
            all_cards =  my_cards + community_cards
            current_round = game_state['round']
            print('current_round:', current_round)
            print('my_cards:', my_cards)
            print('community_cards:', community_cards)
            print('call_amount:', call_amount)

            if (self.has_n_tuple_with_my_card(my_cards, all_cards, 4)):
                return my_player['stack']

            if (self.has_n_tuple_with_my_card(my_cards, all_cards, 3)):
                return my_player['stack']

            if (self.is_pair(my_cards[0], my_cards[1])):
                if self.is_high_card(my_cards[0]):
                    return my_player['stack']
                else:
                    if(call_amount < 500): 
                        return call_amount + game_state['minimum_raise'] + 1
                    else:
                        return 0

            if self.is_high_card(my_cards[0]) and self.is_high_card(my_cards[1]):
                if(call_amount < 300): 
                        print('betting for 2 high cards: ', call_amount + game_state['minimum_raise'] + 10)
                        return call_amount + game_state['minimum_raise'] + 10

            if self.is_high_card(my_cards[0]) or self.is_high_card(my_cards[1]):
                if(call_amount < 200):
                    print('betting for at least 1 high cards: ', call_amount + game_state['minimum_raise'] + 11)
                    return call_amount + game_state['minimum_raise'] + 1

            # if len(community_cards) == 0 and len(my_cards) == 2:
            #     self.round_1_strategy(game_state)
            
            # if len(community_cards) == 3:
            #     self.round_2_strategy(game_state)

            # if len(community_cards) == 4:
            #     self.round_3_strategy(game_state)

            # if len(community_cards) == 5:
            #     self.round_4_strategy(game_state)

            if len(community_cards) == 0:
                return game_state['small_blind'] * 2

            if(call_amount > 100):    
                return 0

            return call_amount
        except:
            return 1

    # def round_1_strategy(self, game_state):
    #     pass

    # def round_2_strategy(self, game_state):
    #     pass

    # def round_3_strategy(self, game_state):
    #     pass

    # def round_4_strategy(self, game_state):
    #     pass

    # def round_5_strategy(self, game_state):
    #     pass

    def showdown(self, game_state):
        pass

    def has_n_tuple_with_my_card(self, my_cards, all_cards, n):
        card_groups = dict()
        my_values = [card['value'] for card in my_cards]

        for card in all_cards:
            if card['value'] in card_groups.keys():
                card_groups[card['value']] += 1
            else:
                card_groups[card['value']] = 1

        for key in card_groups.keys():
            if card_groups[key] == n and key in my_values:
                return True

        return False

    # def has_flush_with_one_of_my_cards(self, my_cards, all_cards):
    #     suits = { 'clubs': 0, 'spades': 0, 'hearts': 0, 'diamonds': 0 }
    #     my_suits = [card['suit'] for card in my_cards]
    #     for card in all_cards:
    #         if card['suit'] in my_suits:
    #             return True
    #     return False
        
    def is_pair(self, card1, card2):
        return card1['rank'] == card2['rank']

    def is_high_card(self, card):
        return card['rank'] in ['A', 'K', 'Q', 'J', '10']


    

