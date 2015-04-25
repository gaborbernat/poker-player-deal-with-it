class Player(object):
    VERSION = "Default Python folding player"

    def __init__(self, game_state):
        self.game_state = game_state

    def bet_request(self):
        return 0

    def showdown(self):
        pass

