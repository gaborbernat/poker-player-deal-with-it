import random

from rank import Rank, Ranks


def r(w, i, d):
    x = w
    found = False
    for k in i:
        if k in x:
            x = x[k]
            found = True
    return x if found else d


class Player(object):
    VERSION = "[DWI] No chance"

    team_name = "Deal With It"

    def __init__(self, game_state):
        self.game_state = game_state

    def bet_request(self):
        # FOLD in the first X round of the sit n go
        fold_until_round = 2
        hand = self.get_cards(self.get_our_player())
        if r(self.game_state, ['round'], 0) < fold_until_round:
            return 0
        if self.is_pref_flop():
            same_rank = hand[0]["rank"] == hand[1]["rank"]
            really_high_card = hand[0]["rank"] in Rank.really_high_card
            if really_high_card and same_rank:
                bet = self.action_all_in()
            else:
                bet = self.bet_amount()
        else:
            bet = self.bet_amount()
        if bet >= int(0.9 * self.get_our_money()):
            rank = Rank(hand, self.get_community_cards()).getRank()
            if rank in [Ranks.pair]:
                if hand[0]['rank'] in Rank.really_high_card \
                        and hand[1]['rank'] in Rank.really_high_card:
                    bet = self.action_all_in()
                else:
                    bet = 0
        return bet

    def bet_amount(self):
        if self.should_we_fold(self.get_cards(self.get_our_player()), self.get_community_cards()):
            bet = 0
        else:
            if len(self.get_active_players()) == 2:
                bet = self.action_raise(int(self.get_our_money() * 0.3))
            else:
                bet = self.action_raise(random.randint(0, 3))
        return bet

    def get_current_bet(self):
        return r(self.game_state, ['pot'], 0)

    def get_our_money(self):
        return self.get_our_player().get("stack", 0)

    def get_our_bet(self):
        return self.get_our_player().get("bet", 0)

    def action_check(self):
        # current buy in - our chips = check (or fold is there is another raise)
        return r(self.game_state, ['current_buy_in'], 0) - self.get_our_player().get("bet", 0)

    def action_all_in(self):
        # current buy in + all the money we still have
        return r(self.game_state, ['current_buy_in'], 0) + self.get_our_player().get("stack", 0)

    def action_raise(self, amount=0):
        # current buy in + minimal raise + raise you want to do
        return r(self.game_state, ['current_buy_in'], 0) - self.get_our_player().get("bet", 0) + r(self.game_state,
                                                                                                   ['minimum_raise'],
                                                                                                   0) + amount

    def get_active_players(self):
        players = []
        for player in self.game_state['players']:
            if player["status"] == 'active':
                players += player

        return players

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

    def is_pref_flop(self):
        return len(self.get_community_cards()) == 0

    def should_we_fold(self, hand, community):
        if self.is_pref_flop():
            same_rank = hand[0]["rank"] == hand[1]["rank"]
            high_card_first = hand[0]["rank"] in Rank.high_card
            high_card_second = hand[1]["rank"] in Rank.high_card

            if hand[0]['rank'] == 'A':
                if hand[1]['rank'] in Rank.high_enough_card:
                    return False

            if hand[1]['rank'] == 'A':
                if hand[0]['rank'] in Rank.high_enough_card:
                    return False

            return not any([same_rank and hand[0]["rank"] in Rank.high_enough_card,
                            high_card_second and high_card_first])
        else:
            rank = Rank(hand, community).getRank()
            if rank in [Ranks.poker, Ranks.full, Ranks.flush, Ranks.straight, Ranks.drill, Ranks.two_pair]:
                return False
            if rank in [Ranks.pair] and hand[0]['rank'] in Rank.high_enough_card:
                return False
            if rank in [Ranks.open_straight, Ranks.open_flush]:
                return False
        return True

    def showdown(self):
        print('showdown {}'.format(self.game_state))

