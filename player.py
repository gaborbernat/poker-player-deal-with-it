def r(w, i, d):
    x = w
    found = False
    for k in i:
        if k in x:
            x = x[k]
            found = True
    return x if found else d


class Player(object):
    VERSION = "[DWI] Okay, no more all in :)"

    team_name = "Deal With It"

    def __init__(self, game_state):
        self.game_state = game_state

    def bet_request(self):

        # get our cards
        ourHand = self.get_cards(self.get_our_player())

        # should we fold
        if self.should_we_fold(ourHand):
            bet = 0
        else:
            mb = r(self.game_state, ['minimum_raise'], 0)
            cb = r(self.game_state, ['current_buy_in'], 0)
            bet = mb + cb
            print('we bet {} for {}'.format(bet, self.game_state))

        return bet


    # Return OUR player
    def get_our_player(self):
        for player in self.game_state['players']:
            if player["name"] == self.team_name:
                return player


    # Returns cards for a player json object
    def get_cards(self, player):
        return player['hole_cards']


    def is_pair_in_hand(self, hand):
        return hand[0]["rank"] == hand[1]["rank"]

    def should_we_fold(self, hand):
        return hand[0]["suit"] != hand[1]["suit"] and hand[0]["rank"] != hand[1]["rank"] and hand[0]["rank"] not in ["J", "K", "Q", "A"] and hand[1]["rank"] not in ["J", "K", "Q", "A"]


    def showdown(self):
        print('showdown {}'.format(self.game_state))

