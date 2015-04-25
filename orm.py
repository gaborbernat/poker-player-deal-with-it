class P(object):
    def __init__(self, name=None, stack=None, status=None, bet=None, version=None, pid=None):
        self.name = name
        self.stack = stack
        self.status = status
        self.bet = bet
        self.version = version
        self.pid = pid


class GameState(object):
    def __init__(self, pid=None, gid=None, round_at=None, bet_index=None, small_blind=None, orbits=None, dealer=None,
                 community_cards=None, current_buy_in=None, pot=None, players=None):
        self.pid = pid
        self.gid = gid
        self.round_at = round_at
        self.bet_index = bet_index
        self.small_blind = small_blind
        self.orbits = orbits
        self.dealer = dealer
        self.community_cards = community_cards
        self.current_buy_in = current_buy_in
        self.pot = pot
        self.players = players

