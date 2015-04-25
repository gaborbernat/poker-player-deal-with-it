def r(w, i, d):
    x = w
    found = False
    for k in i:
        if k in x:
            x = x[k]
            found = True
    return x if found else d


class Player(object):
    VERSION = "Deal With It - Super awesomeness"

    team_name = "Deal With It"

    def __init__(self, game_state):
        self.game_state = game_state

    def bet_request(self):
        mb = r(self.game_state, ['minimum_raise'], 0)
        cb = r(self.game_state, ['current_buy_in'], 0)
        bet = mb + cb
        print('we bet {} for {}'.format(bet, self.game_state))
        # get our cards
        us = self.getCards(self.getOurPlayer())
        return bet


    # Return OUR player
    def getOurPlayer(self):
        for player in self.game_state['players']:
            if player["name"] == self.team_name:
                return player


    # Returns cards for a player json object
    def getCards(self, player):
        return player['hole_cards']

    def showdown(self):
        print('showdown {}'.format(self.game_state))

