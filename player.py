class Player(object):
    VERSION = "Deal With It - Super awesomeness"

    def __init__(self, game_state):
        self.game_state = game_state

    def bet_request(self):
        bet = int(int(self.game_state['current_buy_in']) + int(self.game_state['minimum_raise']))
        print('we bet {} for {}'.format(bet, self.game_state))
        return bet

    def showdown(self):
        print('showdown {}'.format(self.game_state))

