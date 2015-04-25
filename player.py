def r(w, i, d):
    x = w
    found = False
    for k in i:
        if k in x:
            x = x[k]
            found = True
    return x if found else d


class Player(object):
    VERSION = "[DWI] YOLO"

    team_name = "Deal With It"

    def __init__(self, game_state):
        self.game_state = game_state

    def bet_request(self):
        # FOLD in the first X round of the sit n go
        fold_until_round = 5

        if r(self.game_state, ['round'], 0) < fold_until_round:
            return 0

        # get our cards
        our_hand = self.get_cards(self.get_our_player())

        # should we fold
        if self.should_we_fold(our_hand):
            bet = 0
        else:
            bet = self.action_raise(50)

        return bet

    def get_current_bet(self):
        """
        Sum of all the players bets
        :return:
        """
        return r(self.game_state, ['pot'], 0)

    def get_our_money(self):
        """
        Returns the money we haven't BET yet

        :return: int
        """
        return self.get_our_player().get("stack", 0)

    def get_our_bet(self):
        """
        Returns the money we BET so far
        :return:
        """
        return self.get_our_player().get("bet", 0)

    def action_check(self):
        """
        Checks

        :return:
        """
        # current buy in - our chips = check (or fold is there is another raise)
        return r(self.game_state, ['current_buy_in'], 0) - self.get_our_player().get("bet", 0)

    def action_all_in(self):
        """
        ALL IN
        :return:
        """
        # current buy in + all the money we still have
        return r(self.game_state, ['current_buy_in'], 0) + self.get_our_player().get("stack", 0)

    def action_raise(self, amount=0):
        """
        Calls minimal raise + the amouns you give

        :param amount: The amoun you want to raise (will be added to the minimal raise amount)
        :return:
        """
        # current buy in + minimal raise + raise you want to do
        return r(self.game_state, ['current_buy_in'], 0) - self.get_our_player().get("bet", 0) + r(self.game_state,
                                                                                                   ['minimum_raise'],
                                                                                                   0) + amount


    def get_our_player(self):
        for player in self.game_state['players']:
            if player["name"] == self.team_name:
                return player


    @staticmethod
    def get_cards(player):
        return player['hole_cards']

    def get_community_cards(self):
        return r(self.game_state, ['community_cards'], [])


    @staticmethod
    def is_pair_in_hand(hand):
        return hand[0]["rank"] == hand[1]["rank"]

    @staticmethod
    def should_we_fold(hand):
        high_cards = ["J", "K", "Q", "A"]
        # double_suit = hand[0]["suit"] == hand[1]["suit"]
        same_rank = hand[0]["rank"] == hand[1]["rank"]
        high_card_first = hand[0]["rank"] in high_cards
        high_card_second = hand[1]["rank"] in high_cards
        return not any([same_rank and hand[0]["rank"] in (high_cards + ['8', '9', '10']),
                        high_card_second and high_card_first])

    def showdown(self):
        print('showdown {}'.format(self.game_state))

