import itertools

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print(game_state)
        my_player = game_state['players'][game_state['in_action']]
        call_amount = game_state['current_buy_in'] - my_player['bet']
        my_cards = my_player['hole_cards']
        community_cards = game_state['community_cards']
        all_cards =  my_cards + community_cards
        current_round = game_state['round']
        print('current_round:', current_round)
        print('my_cards:', my_cards)
        print('community_cards:', community_cards)
        print('call_amount:', call_amount)
        print('minimum_raise', game_state['minimum_raise']) 
    

        if (self.has_n_tuple_with_my_card(my_cards, all_cards, 4) != None):
            return my_player['stack']

        if (self.has_flush_with_both_of_my_cards(my_cards, all_cards)):
            return my_player['stack']

        if (self.has_n_tuple_with_my_card(my_cards, all_cards, 3) != None):
            return my_player['stack']

        if (self.is_pair(my_cards[0], my_cards[1])):
            if self.is_high_card(my_cards[0]):
                return my_player['stack']
            else:
                if(call_amount < 500) and my_player['bet'] < 0.2 * my_player['stack']: 
                    return call_amount + game_state['minimum_raise'] + 1
                else:
                    return 0

        if len(community_cards) == 0 and my_player['bet'] > 0.1 * my_player['stack']:
            return 0

        if self.is_high_card(my_cards[0]) and self.is_high_card(my_cards[1]):
            if(call_amount < 300): 
                print('betting for 2 high cards: ', call_amount + game_state['minimum_raise'] + 10)
                return call_amount + game_state['minimum_raise'] + 10

        # if self.is_high_card(my_cards[0]) or self.is_high_card(my_cards[1]):
        #     if(call_amount < 200):
        #         print('betting for at least 1 high cards: ', call_amount + game_state['minimum_raise'] + 1)
        #         return call_amount + game_state['minimum_raise'] + 1

        my_card_contributing_to_pair = self.has_n_tuple_with_my_card(my_cards, all_cards, 2)
        if (my_card_contributing_to_pair != None and call_amount < 200):
            if self.is_high_card(my_card_contributing_to_pair):
                return call_amount + game_state['minimum_raise'] + 1

        if my_player['bet'] > 0.1 * my_player['stack']:
            return 0

        return call_amount


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
        my_values = [card['rank'] for card in my_cards]

        for card in all_cards:
            if card['rank'] in card_groups.keys():
                card_groups[card['rank']] += 1
            else:
                card_groups[card['rank']] = 1

        for key in card_groups.keys():
            if card_groups[key] == n and key in my_values:
                for card in my_cards:
                    if card['rank'] == key:
                        return card

        return None

    def has_flush_with_one_of_my_cards(self, my_cards, all_cards):
        suits_group = { 'clubs': 0, 'spades': 0, 'hearts': 0, 'diamonds': 0 }
        my_suits = [card['suit'] for card in my_cards]

        for card in all_cards:
            suits_group[card['suit']] += 1

        for key in suits_group.keys():
            if suits_group[key] is 5 and key in my_suits:
                return True
        return False

    def has_flush_with_both_of_my_cards(self, my_cards, all_cards):
        suits_group = { 'clubs': 0, 'spades': 0, 'hearts': 0, 'diamonds': 0 }
        my_suits = [card['suit'] for card in my_cards]

        for card in all_cards:
            suits_group[card['suit']] += 1

        for key in suits_group.keys():
            if suits_group[key] is 5 and key in my_suits and self.is_pair(my_cards[0], my_cards[1]):
                return True
        return False

    def has_straight(slef, my_cards, all_cards):
        pass
        
    def is_pair(self, card1, card2):
        return card1['rank'] == card2['rank']

    def is_high_card(self, card):
        is_high_card = card['rank'] in ['A', 'K', 'Q', 'J', '10']
        print("HIGH CARD DETECTOR: ", card['rank'], is_high_card)
        return is_high_card


    

