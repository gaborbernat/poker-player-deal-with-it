class Player(object):
    VERSION = "Deal With It - Super awesomeness"

    team_name = "Deal With It"

    def __init__(self, game_state):
        self.game_state = game_state

    def bet_request(self):
        bet = int(self.game_state['pot'])*2
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

